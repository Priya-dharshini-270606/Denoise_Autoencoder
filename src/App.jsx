import React, { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [psnr, setPsnr] = useState(null);
  const [noise, setNoise] = useState(null);
  const [status, setStatus] = useState("");

  const uploadImage = async () => {
    if (!file) {
      alert("Please select an image");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("http://127.0.0.1:8000/denoise", {
      method: "POST",
      body: formData
    });

    const data = await res.json();

    setResult(`data:image/png;base64,${data.image}`);
    setPsnr(data.psnr);
    setNoise(data.noise_level);
    setStatus(data.status);
  };

  const downloadImage = () => {
    const link = document.createElement("a");
    link.href = result;
    link.download = "denoised.png";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <div className="container">
      <h2>DnCNN Image Denoising</h2>

      <input
        type="file"
        accept="image/*"
        onChange={e => setFile(e.target.files[0])}
      />

      <button onClick={uploadImage}>Denoise</button>

      {status && <p><b>Status:</b> {status}</p>}
      {noise !== null && <p><b>Noise Level:</b> {noise}</p>}
      {psnr !== null && <p><b>PSNR:</b> {psnr} dB</p>}

      {result && (
        <>
          <img src={result} alt="Denoised" />
          <button onClick={downloadImage}>Download</button>
        </>
      )}
    </div>
  );
}

export default App;
