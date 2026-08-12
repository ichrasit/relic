"""Geometric (keypoint-based) similarity scoring.

Perceptual hashing alone is fragile against crops, rotations, watermarks,
and partial re-uploads, which are extremely common among Google Lens
candidates. ORB keypoint matching complements pHash by checking whether
the two images actually share structural/geometric content, not just a
similar overall "shape" of pixels.
"""


from dataclasses import dataclass
from pathlib import Path

import cv2
import numpy as np


MAX_FEATURES = 500
LOWE_RATIO = 0.75

@dataclass(frozen=True)
class GeometricMatch:
    good_matches: int
    total_keypoint: int
    score: float


def _load_grayscale(path: Path) -> np.ndarray:
    image = cv2.imread(str(path)), cv2.IMREAD_GRAYSCALE
    if image is None:
        raise ValueError(f"Could not read image for ORB matching : {path}")
    return image

def orb_similarity(source_path: Path, candidate_path: Path) -> GeometricMatch:
    source_image = _load_grayscale(source_path)
    candidate_image = _load_grayscale(candidate_path)

    orb = cv2.ORB_create(nfeatures=MAX_FEATURES)
    source_keypoints, source_descriptors = orb.detectAndCompute(source_image, None)
    candidate_keypoints, candidate_descriptors = orb.detectAndCompute(candidate_image, None)

    if source_descriptors is None or candidate_descriptors is None:
        return GeometricMatch(good_matches=0, total_keypoint=0, score=0)

    matcher = cv2.BFMatcher(cv2.NORM_HAMMING)
    raw_matches = matcher.knnMatch(source_descriptors, candidate_descriptors, k=2)

    good_matches = [
        m for m, n in raw_matches
        if len(raw_matches) > 0 and m.distance < LOWE_RATIO * n.distance
    ]

    total_keypoints = min(len(source_keypoints), len(candidate_keypoints))

    if total_keypoints == 0:
        return GeometricMatch(good_matches=0, total_keypoint=0, score=0)

    score = min(len(good_matches) / total_keypoints, 1.0)

    return GeometricMatch(
        good_matches=len(good_matches),
        total_keypoints=total_keypoints,
        score=score,
        )

