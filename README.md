#  Voice Assistant "Virat" | Python Project

Virat is a Python-based voice assistant that responds to voice commands for web browsing, app launching, system tasks, music playback, weather updates, and more. It uses speech recognition and text-to-speech to provide an interactive and intelligent user experience.

---

##  Features

-  **Wake Word Detection**: Responds to phrases like “hello Virat”, “hi Virat”, etc.
-  **Text-to-Speech (TTS)**: Replies using a human-like voice with `pyttsx3`
-  **Speech Recognition**: Converts voice to text using Google Speech API
-  **Web Control**:
       - Open websites like Google, YouTube, Gmail, ChatGPT, GitHub, Stack Overflow, Maps, WhatsApp
-  **Date and Time Reporting**:
       - “What’s the time?”, “What’s the date?”
-  **Google Search**: Say “Search Python list comprehension” to get results
-  **Wikipedia Summaries**: Ask “Who is Elon Musk?” or “What is ChatGPT?”
-  **Custom Music Library**:
       -  Plays YouTube music using your own `musiclibrary.py` ,you can add links of songs of your own choice in this library
-  **System Commands**:
       - Shutdown, Restart, Lock PC, Open Calculator, Notepad, VS Code
-  **Real-Time Weather Info**:
       - Asks city name and fetches weather using OpenWeatherMap API

---

## 📁 Project Structure

```
voice-assistant-virat/
│
├── virat.py # Main script
├── config.py # Stores API key for weather (excluded from GitHub)
├── musiclibrary.py # Song titles and their YouTube URLs
├── requirements.txt # Python dependencies
├── .gitignore # Excludes sensitive files
└── README.md # Project documentation
```

---

## 🛠 Tech Stack

- **Language**: Python 3.x
- **Libraries**:
  - `speechrecognition`
  - `pyttsx3`
  - `wikipedia`
  - `requests`
  - `pyaudio`
  - `webbrowser`, `os`, `subprocess`, `datetime`

---

## 🔐 Setup Instructions

1. **Clone or download the repo**

2. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Create a config.py file:**
   ```bash
      # config.py
   OPENWEATHER_API_KEY = "your_actual_api_key_here"
   ```
4. **Run the assistant:**
   ```bash
        python virat.py
   ```

---

## Example Voice Commands
- "Hello Virat"
- "Open YouTube"
- "Play Tum Hi Ho"
- "What’s the time?"
- "What is Python?"
- "Search artificial intelligence"
- "Shutdown the system"
- "What is the weather"
      - (then say: “Delhi”)

---

##  Notes
- config.py is excluded from GitHub using .gitignore — it contains private API key.
- Requires an internet connection for voice recognition, weather, and Wikipedia
- pyaudio may require manual installation for some systems (especially Windows)
- This is a learning-focused, personal voice assistant project

---

## Author
Created by Gourang Sharma
Feel free to connect for collaboration, feedback, or questions

---

## License
This project is open for educational and personal use. Use responsibly and avoid automating any unsafe or unauthorized tasks.


Added full project description and features to README

