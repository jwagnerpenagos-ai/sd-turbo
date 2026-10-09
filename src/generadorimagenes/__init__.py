import torch
from diffusers import AutoPipelineForText2Image


def main():
    print("Cargando modelo ...")

    modelo = AutoPipelineForText2Image.from_pretrained(
        "stabilityai/sd-turbo",
        torch_dtype=torch.float32
        # FloatXX puede ser 32 o 16
        # (indica la cantidad de decimales de precisión con el que el modelo creará la imagen)
        # Si mi pc genera una imagen negra, cambiar a 16
    )

    modelo = modelo.to("cpu")
    # Le decimos que se ejecute con la CPU y RAM
    # Se puede cambiar a cuda - con NVIDIA
    # mps - Mac con procesador MX
    # xpu - Grfica Intel iris

    prompt = input("Escribe el prompt de la imagen: ")
    negative_prompt = "low quality, blurry, distorted, text, watermark, extra fingers, deformed, mutated, poorly drawn, ugly, bad anatomy, oversaturated, grainy, cropped, unrealistic colors"
    print("Generando la imagen...")

    imagen = modelo(
        prompt=prompt,
        negative_prompt=negative_prompt,
        num_inference_steps=10, # Número de veces que creará y corregirá la imagen
        guidance_scale=2.0, # Qué tan fiel será al prompt
        height=1024,
        width=1024
    ).images[0]

    imagen.save("pizza.png")
    print("Imagen guardada !!!")
