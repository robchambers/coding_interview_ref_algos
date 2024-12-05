"""
Non-maximum suppression 
"""

import numpy as np
from typing import List
import unittest
from typing import NamedTuple


class Box(NamedTuple):
    cx: int
    cy: int
    w: int
    l: int


def iou(box1: Box, box2: Box) -> float:
    """Compute Intersection over Union (IoU) between two bounding boxes."""
    # Convert center coordinates to corner coordinates
    x1_1 = box1.cx - box1.w / 2
    y1_1 = box1.cy - box1.l / 2
    x2_1 = box1.cx + box1.w / 2
    y2_1 = box1.cy + box1.l / 2

    x1_2 = box2.cx - box2.w / 2
    y1_2 = box2.cy - box2.l / 2
    x2_2 = box2.cx + box2.w / 2
    y2_2 = box2.cy + box2.l / 2

    # Calculate intersection coordinates
    x1 = max(x1_1, x1_2)
    y1 = max(y1_1, y1_2)
    x2 = min(x2_1, x2_2)
    y2 = min(y2_1, y2_2)

    # Calculate the area of intersection
    intersection_area = max(0, x2 - x1) * max(0, y2 - y1)

    # Calculate the area of both bounding boxes
    box1_area = box1.w * box1.l
    box2_area = box2.w * box2.l

    # Calculate IoU
    if box1_area + box2_area - intersection_area == 0:
        return 0.0
    iou_value = intersection_area / float(box1_area + box2_area - intersection_area)
    return iou_value


def nms(boxes: List[Box], scores: List[float], thresh: float) -> List[int]:
    """Perform Non-Maximum Suppression (NMS) on bounding boxes."""
    # Sort boxes by their confidence scores in descending order
    inds = np.argsort(scores)[::-1]

    sel: List[int] = []
    while len(inds):
        # Select the box with the highest score
        ind = inds[0]
        sel.append(ind)

        # Compare IoU of this box with the rest, keeping any with low/no overlap.
        inds = [i for i in inds[1:] if iou(boxes[ind], boxes[i]) < thresh]

    return sel


# Unit tests
class TestNMS(unittest.TestCase):

    def test_no_overlap(self):
        boxes = [Box(100, 100, 50, 50), Box(300, 300, 50, 50)]
        scores = [0.9, 0.8]
        iou_threshold = 0.5
        selected = nms(boxes, scores, iou_threshold)
        self.assertEqual(selected, [0, 1])

    def test_complete_overlap(self):
        boxes = [Box(100, 100, 50, 50), Box(100, 100, 50, 50)]
        scores = [0.9, 0.8]
        iou_threshold = 0.5
        selected = nms(boxes, scores, iou_threshold)
        self.assertEqual(selected, [0])

    def test_partial_overlap(self):
        boxes = [Box(100, 100, 50, 50), Box(105, 105, 50, 50)]
        scores = [0.9, 0.8]
        iou_threshold = 0.5
        selected = nms(boxes, scores, iou_threshold)
        self.assertEqual(selected, [0])

    def test_different_scores(self):
        boxes = [Box(100, 100, 50, 50), Box(105, 105, 50, 50), Box(50, 50, 50, 50)]
        scores = [0.9, 0.75, 0.6]
        iou_threshold = 0.5
        selected = nms(boxes, scores, iou_threshold)
        self.assertEqual(selected, [0, 2])

    def test_high_iou_threshold(self):
        boxes = [Box(100, 100, 50, 50), Box(105, 105, 50, 50), Box(50, 50, 50, 50)]
        scores = [0.9, 0.75, 0.6]
        iou_threshold = 0.9
        selected = nms(boxes, scores, iou_threshold)
        self.assertEqual(selected, [0, 1, 2])


if __name__ == "__main__":
    unittest.main()
