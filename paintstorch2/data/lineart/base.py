from PIL import Image


class LineartGenerator:
    def __call__(self, img: Image, *args, **kwargs) -> Image:
        raise NotImplementedError("__call__ method must be implemented.")