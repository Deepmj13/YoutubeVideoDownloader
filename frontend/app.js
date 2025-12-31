const BASE_URL = "http://127.0.0.1:8000";

const urlInput = document.getElementById("urlInput");
const fetchBtn = document.getElementById("fetchBtn");
const formatSelect = document.getElementById("formatSelect");
const downloadBtn = document.getElementById("downloadBtn");
const statusText = document.getElementById("status");

const videoBtn = document.getElementById("videoBtn");
const audioBtn = document.getElementById("audioBtn");
const videoSection = document.getElementById("videoSection");
const audioSection = document.getElementById("audioSection");
const audioSelect = document.getElementById("audioSelect");

let mode = "video";

/* Mode switching */
videoBtn.onclick = () => {
  mode = "video";
  videoBtn.classList.add("active");
  audioBtn.classList.remove("active");
  videoSection.classList.remove("hidden");
  audioSection.classList.add("hidden");
};

audioBtn.onclick = () => {
  mode = "audio";
  audioBtn.classList.add("active");
  videoBtn.classList.remove("active");
  audioSection.classList.remove("hidden");
  videoSection.classList.add("hidden");
};

/* Fetch formats */
fetchBtn.onclick = async () => {
  const url = urlInput.value;
  if (!url) return alert("Enter YouTube URL");

  statusText.innerText = "Fetching formats...";
  formatSelect.innerHTML = `<option value="">Select Video Quality</option>`;

  const res = await fetch(`${BASE_URL}/formats`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ url }),
  });

  const data = await res.json();

  data.forEach((f) => {
    const option = document.createElement("option");
    option.value = f.format_id;
    option.textContent = `${f.resolution} (${f.ext})`;
    formatSelect.appendChild(option);
  });

  statusText.innerText = "Formats loaded";
};

/* Download */
downloadBtn.onclick = async () => {
  const url = urlInput.value;
  if (!url) return alert("Enter YouTube URL");

  statusText.innerText = "Download started...";

  if (mode === "video") {
    const format_id = formatSelect.value;
    if (!format_id) return alert("Select video quality");

    await fetch(`${BASE_URL}/download/video`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url, format_id }),
    });
  } else {
    const codec = audioSelect.value;

    await fetch(`${BASE_URL}/download/audio`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url, codec }),
    });
  }

  statusText.innerText = "Download completed (saved on server)";
};
