from nodes import LoraLoader


class LoraLoaderWithImages(LoraLoader):
    RETURN_TYPES = (*LoraLoader.RETURN_TYPES, "STRING",)
    RETURN_NAMES = (
        *getattr(LoraLoader, "RETURN_NAMES", LoraLoader.RETURN_TYPES),
        "example",
    )

    @classmethod
    def INPUT_TYPES(cls):
        types = super().INPUT_TYPES()
        types["optional"] = {"prompt": ("STRING", {"hidden": True})}
        return types

    def load_lora(self, **kwargs):
        prompt = kwargs.pop("prompt", "")
        return (*super().load_lora(**kwargs), prompt)


NODE_CLASS_MAPPINGS = {
    "LoraLoader|pysssss": LoraLoaderWithImages,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LoraLoader|pysssss": "Lora Loader 🐍",
}

