from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import torch
import numpy as np
import io
import base64

from model import DnCNN

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

device = torch.device("cpu")

model = DnCNN()
model.load_state_dict(
    torch.load("dncnn_denoising_model.pth", map_location=device)
)
model.eval()

def preprocess(image):
    image = image.resize((128, 128))
    image = np.array(image) / 255.0
    image = torch.tensor(image, dtype=torch.float32)
    image = image.permute(2, 0, 1).unsqueeze(0)
    return image

def postprocess(tensor):
    image = tensor.squeeze().permute(1, 2, 0).detach().numpy()
    image = np.clip(image * 255, 0, 255).astype(np.uint8)
    return Image.fromarray(image)

def add_noise(image, noise_factor=0.2):
    noise = torch.randn_like(image) * noise_factor
    noisy = image + noise
    return torch.clamp(noisy, 0.0, 1.0)

def estimate_noise_level(image):
    return torch.mean(torch.abs(image[:, :, :-1, :] - image[:, :, 1:, :]))

def calculate_psnr(original, denoised):
    mse = torch.mean((original - denoised) ** 2)
    if mse == 0:
        return torch.tensor(100.0)
    return 20 * torch.log10(1.0 / torch.sqrt(mse))

@app.post("/denoise")
async def denoise_image(file: UploadFile = File(...)):
    image = Image.open(file.file).convert("RGB")

    input_tensor = preprocess(image)

    noise_level = estimate_noise_level(input_tensor)
    NOISE_THRESHOLD = 0.01

    if noise_level < NOISE_THRESHOLD:
        output = input_tensor
        status = "Image already clean – denoising skipped"
    else:
        noisy_input = add_noise(input_tensor, 0.2)
        with torch.no_grad():
            output = model(noisy_input)
        status = "Denoising applied"

    psnr_value = calculate_psnr(input_tensor, output).item()

    output_image = postprocess(output)

    buffer = io.BytesIO()
    output_image.save(buffer, format="PNG")
    encoded_image = base64.b64encode(buffer.getvalue()).decode()

    return {
        "image": encoded_image,
        "psnr": round(psnr_value, 2),
        "noise_level": round(noise_level.item(), 5),
        "status": status
    }
