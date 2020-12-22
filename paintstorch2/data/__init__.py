from paintstorch2.data.color.base import ColorSimplifier
from paintstorch2.data.color.kmeans import kMeansColorSimplifier
from paintstorch2.data.color.quantize import QuantizeColorSimplifier
from paintstorch2.data.color.segmentation import SegmentationColorSimplifier

from paintstorch2.data.dataset.base import PaintsTorch2Dataset
from paintstorch2.data.dataset.modular import (
    ModularPaintsTorch2Dataset, Modules,
)

from paintstorch2.data.hints.base import Hints, HintsGenerator
from paintstorch2.data.hints.random import RandomHintsGenerator

from paintstorch2.data.lineart.base import LineartGenerator
from paintstorch2.data.lineart.xdog import xDoGLineartGenerator

from paintstorch2.data.mask.base import MaskGenerator
from paintstorch2.data.mask.kmeans import kMeansMaskGenerator
from paintstorch2.data.mask.patch import PatchMaskGenerator
from paintstorch2.data.mask.segmentation import SegmentationMaskGenerator


COLOR_SIMPLIFIERS = {
    "kmeans": kMeansColorSimplifier,
    "quantize": QuantizeColorSimplifier,
    "segmentation": SegmentationColorSimplifier,
}

HINTS_GENERATORS = {
    "random": RandomHintsGenerator,
}

LINEART_GENERATORS = {
    "xdog": xDoGLineartGenerator,
}

MASK_GENERATORS = {
    "kmeans": kMeansMaskGenerator,
    "patch": PatchMaskGenerator,
    "segmentation": SegmentationMaskGenerator,
}