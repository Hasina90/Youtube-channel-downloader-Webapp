# 🎬 YouTube Channel Downloader Web App

This is a full-stack web application that allows users to **download all videos from a public YouTube channel** by simply pasting the channel URL. The frontend is built using **HTML, CSS, and JavaScript**, while the backend is powered by **FastAPI** and `yt-dlp`.

---

## 🚀 Features

- 🔗 Paste any public YouTube **channel URL**
- ⬇️ Download **all videos** from that channel in `.mp4` format
- 🛑 Stop ongoing downloads with one click
- 🎨 Clean, responsive UI with icons and animated buttons
- 📂 Videos are stored locally in a `downloads/` folder

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, FastAPI
- **Video Downloader**: [`yt-dlp`](https://github.com/yt-dlp/yt-dlp)
- **Version Control**: Git + GitHub

---


## 📁 Folder Structure
youtube_downloader/
├── static/
│ ├── styles.css
│ └── script.js
├── templates/
│ └── index.html
├── downloads/ # ⛔️ Ignored in GitHub (videos not uploaded)
├── main.py # FastAPI backend
├── .gitignore
└── README.md


---

## 🧪 How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/YourUsername/youtube-downloader-webapp.git
cd youtube-downloader-webapp

2.Create and activate a virtual environment:
python -m venv venv
venv\Scripts\activate  # On Windows

3.Install dependencies:
pip install -r requirements.txt

4.Run the app:
uvicorn main:app --reload

5.Open your browser:
http://127.0.0.1:8000

⚠️ Notes
📁 downloads/ folder is excluded from Git using .gitignore to avoid large file errors on GitHub.

🚫 Video downloads may fail if YouTube restricts the channel or content.

🧩 You must have yt-dlp installed and added to your system PATH.

🙋‍♀️ Author
👤 Hasina Sheik
💻 Built with FastAPI + JavaScript + GitHub![Screenshot (289)](https://github.com/user-attachments/assets/fc9a8359-b021-4c33-aa16-ebbab327191a)

