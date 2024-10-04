# PitchPerfect_interview_bot
Interview &amp; Pitch preparation assistent powered by OpenAI API - Feedback on your answers and non-verbal communications.

<iframe width="560" height="315" src="https://www.youtube.com/embed/xA9jZJjejWQ?si=exaujM2cwe3FUaRx" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

# Introduction
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
