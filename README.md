# 🖼️ Denoising Autoencoder for Image Restoration

A deep learning project that uses a **Denoising Autoencoder** to remove **Salt-and-Pepper noise** from images and reconstruct cleaner versions of the original images.

## 📌 Project Overview

Images can be affected by different types of noise, which can reduce their quality and make important features difficult to identify.

In this project, a **Denoising Autoencoder** is trained to learn how to reconstruct clean images from their noisy versions.

The images are resized to **64 × 64 pixels**, corrupted with Salt-and-Pepper noise, and then given to the model as input. The original clean images are used as the target output.

### Basic Workflow

```text
Original Image
      ↓
Add Salt-and-Pepper Noise
      ↓
Noisy Image
      ↓
     Encoder
      ↓
Latent Representation
      ↓
     Decoder
      ↓
Denoised Image
```

## 🎯 Objectives

* Remove Salt-and-Pepper noise from images.
* Learn useful image representations using an Autoencoder.
* Reconstruct clean images from noisy inputs.
* Understand the Encoder-Decoder architecture.
* Apply deep learning techniques to image restoration.

## 🧠 Denoising Autoencoder

A Denoising Autoencoder is a neural network that learns to reconstruct a clean image from a corrupted input image.

It consists of:

### Encoder

The Encoder extracts important features from the noisy image and compresses the information into a lower-dimensional representation.

### Latent Representation

The latent representation contains the important features learned by the Encoder.

### Decoder

The Decoder uses the learned representation to reconstruct the original clean image.

The model learns the mapping:

```text
Noisy Image → Clean Image
```

## 🧂 Noise Used

### Salt-and-Pepper Noise

Salt-and-Pepper noise randomly changes pixels in an image.

* **Salt noise** → white pixels
* **Pepper noise** → black pixels

The noisy image is used as the input, while the original image is used as the target.

## 🔄 Project Workflow

1. Load the image dataset.
2. Resize images to **64 × 64**.
3. Normalize the image pixel values.
4. Generate Salt-and-Pepper noise.
5. Create noisy versions of the images.
6. Train the Denoising Autoencoder.
7. Pass noisy images through the trained model.
8. Reconstruct the denoised images.
9. Compare original, noisy, and denoised images.

## 🛠️ Technologies Used

* **Python**
* **TensorFlow / Keras**
* **NumPy**
* **OpenCV**
* **Matplotlib**
* **Deep Learning**
* **Autoencoder**

## 📂 Project Structure

```text
Denoising-Autoencoder/
│
├── dataset/
├── model/
├── results/
├── train.py
├── test.py
├── requirements.txt
└── README.md
```

> The project structure above can be modified according to the actual files in the repository.

## 📊 Results

The model reconstructs cleaner images from images affected by Salt-and-Pepper noise.

The results can be evaluated by comparing:

```text
Original Image → Noisy Image → Denoised Image
```

### Example

Add your output/result image to the repository and display it here:

```markdown
![Denoising Autoencoder Results](results/result.png)
```

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

### 2. Open the Project

```bash
cd Denoising-Autoencoder
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Project

```bash
python app.py
```

## 🔮 Future Improvements

* Experiment with different noise levels.
* Support other types of image noise.
* Improve the Encoder-Decoder architecture.
* Evaluate the model using **PSNR** and **SSIM**.
* Compare different image denoising techniques.
* Deploy the model as a web application.

## 👩‍💻 Author

**Priyadharshini Venkatesan**

B.Tech – Artificial Intelligence & Data Science
Shiv Nadar University, Chennai
