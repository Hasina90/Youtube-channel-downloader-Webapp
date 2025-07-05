async function downloadVideos() {
  const url = document.getElementById("channelUrl").value;
  const message = document.getElementById("statusMessage");

  if (!url) {
    message.textContent = "Please enter a channel URL.";
    return;
  }

  message.textContent = "Downloading... Please wait.";

  const formData = new FormData();
  formData.append("channel_url", url);

  try {
    const response = await fetch("/download/", {
      method: "POST",
      body: formData,
    });

    const result = await response.json();

    if (response.ok) {
      message.textContent = result.message;
    } else {
      message.textContent = result.error || "Download failed.";
    }
  } catch (error) {
    message.textContent = "Error connecting to the server.";
  }
  console.log("Downloading from URL:", url);

}
async function stopDownload() {
  const message = document.getElementById("statusMessage");

  try {
    const response = await fetch("/stop-download/", {
      method: "POST",
    });

    const result = await response.json();
    message.textContent = result.message;
  } catch (error) {
    message.textContent = "Failed to stop the download.";
  }
}
