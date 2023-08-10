# This file runs during container build time to get model weights built into the container
import os
import torch
from diffusers import DiffusionPipeline

MODEL_ID = os.environ.get("MODEL_ID")
HUGGINGFACE_TOKEN = os.environ.get("HUGGINGFACE_TOKEN")


def download_model():
    # do a dry run of loading the huggingface model, which will download weights
    base = DiffusionPipeline.from_pretrained(
        MODEL_ID,
        use_auth_token=HUGGINGFACE_TOKEN,
        torch_dtype=torch.float16,
        use_safetensors=True,
        variant="fp16"
    )
    # refiner = DiffusionPipeline.from_pretrained(
    #     "stabilityai/stable-diffusion-xl-refiner-1.0",
    #     text_encoder_2=base.text_encoder_2,
    #     vae=base.vae,
    #     torch_dtype=torch.float16,
    #     use_safetensors=True,
    #     variant="fp16",
    # )


if __name__ == "__main__":
    download_model()
