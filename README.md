🎙️ My Own Alexa

My Own Alexa is a simple voice-controlled virtual assistant built using Python.
It uses speech recognition, text-to-speech conversion, and online APIs to perform tasks like playing YouTube videos, telling the time, searching Wikipedia, and even telling jokes — just like Alexa!

🚀 Features

✔️ Voice Recognition using speech_recognition
✔️ Text-to-Speech using pyttsx3
✔️ Play any song or video using YouTube
✔️ Wikipedia search and answers
✔️ Tell jokes for fun
✔️ Detect the keyword "Alexa" before executing commands
✔️ Hands-free use — continuous listening loop

🛠️ Technologies Used
Technology	Purpose
speech_recognition	- Converts voice to text
pyttsx3	- Converts text to speech
pywhatkit	- Plays YouTube videos
wikipedia	- Fetches summarized information
datetime	- Tells current time
pyjokes	- Generates random jokes

📁 How It Works

The assistant waits for a microphone input.

When you start speaking and include the word "Alexa", it processes the command.

Based on the command, it performs the requested task — such as:

"Alexa play Faded" → plays song

"Alexa time" → speaks current time

"Alexa who is Elon Musk" → speaks Wikipedia summary

📢 Future Improvements

🔹 Add wake-word detection without pressing Enter
🔹 Integrate ChatGPT API responses
🔹 Add more custom commands
🔹 GUI version (Desktop / Mobile)
