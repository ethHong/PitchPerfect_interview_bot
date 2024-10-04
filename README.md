# PitchPerfect_interview_bot
Interview &amp; Pitch preparation assistent powered by OpenAI API - Feedback on your answers and non-verbal communications.

<img width="400" alt="Screenshot 2024-10-04 at 1 11 46 AM" src="https://github.com/user-attachments/assets/ac9f3934-bceb-4ab9-9bdd-e3f611b81e95">

# Introduction
## Demo Video

[![Demo Vide](https://img.youtube.com/vi/xA9jZJjejWQ/sddefault.jpg)](https://youtu.be/xA9jZJjejWQ?feature=shared)

* Gen AI powered (OpenAI AI API) job interview / pitch prep assistant.
* It transbribes your speech, or response and also captures your camera snapshot to give feedback about non-verbal communications (gestures, postures, eye contacts)

# Reqioremente
* This app requires OpenAI API, so you need to add your own API KEY in api.txt
* There are many required libraries, including Streamlit, PyAudio, OpenAI, Whisper. Recommend settin up virtual environment.
* On your local setting:

  ```
  pipenv --python 3.9
  pipenv shell
  pipenv install

  #Add your api.txt file

  streamlit run app.py #This will run app on your local setting
  ```
