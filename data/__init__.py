# from .voc import VOCDetection, AnnotationTransform, detection_collate, VOC_CLASSES
from .voc0712 import VOCDetection, AnnotationTransform, detection_collate, VOC_CLASSES
# from .coco import COCODetection
from .license_plate import ANPRDetection, ANPRAnnotationTransform, ANPR_CLASSES
from .data_augment import *
from .config import *
