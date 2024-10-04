import cv2
import streamlit as st
import os
from datetime import datetime
import threading
import time
import sounddevice as sd
import numpy as np
import whisper
import scipy.io.wavfile as wav  # Correct import for wav.write

# initialized_start_time = datetime.today().strftime("%Y-%m-%d_%H:%M:%S")
filname = "audio.wav"


def start_recording(init_time, fps=30, interval=3, time_limit=60, filename="audio.wav"):
    dir_path = f"record_{init_time}"
    os.mkdir(dir_path)

    st.session_state["recording"] = True  # Change status
    cap = cv2.VideoCapture(0)

    countdown_placeholder = st.empty()
    stframe = st.empty()
    start_time = time.time()

    # Start recording audio in the background
    message = st.chat_message("assistant")
    message.write("Recording video and audio. Please speak...")
    audio_filename = os.path.join(dir_path, filename)

    audio_thread = threading.Thread(
        target=record_audio, args=(time_limit, audio_filename)
    )

    audio_thread.start()

    # record_audio(duration=time_limit, filename=audio_filename)
    # # Recording audio asynchronously
    frame_count = 0
    while st.session_state["recording"]:

        passed_time = time.time() - start_time
        remaining_time = time_limit - passed_time
        if remaining_time > 0:
            countdown_placeholder.markdown(
                f"## Time left: {int(remaining_time)} seconds"
            )
        else:
            message.write("Time limit reached. Stopping recording...")
            break

        ret, frame = cap.read()  # Capture frame
        if ret:
            stframe.image(frame, channels="BGR")
            # We show all frames of video, but for frame only save partial frames.
            # if frame_count % (fps * interval) == 0:
            if frame_count % (fps * interval) == 0:
                filename = f"{dir_path}/frame_{frame_count}.jpg"
                cv2.imwrite(filename, frame)

        frame_count += 1
    else:
        message = st.chat_message("assistant")
        message.write("Error occured")

    cap.release()

    ### Here, we give the output

    text = whisper_ai(audio_filename)
    message = st.chat_message("assistant")
    message.write("What you said is:")
    message.write(text["text"])

    return text["text"]


def stop_recording():
    st.session_state["recording"] = False
    message = st.chat_message("assistant")
    message.write("Recording has been stopped.")


def record_audio(duration, filename="audio.wav", fs=44100):
    message = st.chat_message("assistant")
    message.write(f"Audio Recording Started")
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype=np.int16)
    sd.wait()  # Wait until recording is finished
    wav.write(filename, fs, audio_data)  # Save as .wav file
    message = st.chat_message("assistant")
    message.write(f"Audio saved as {filename}")


def whisper_ai(audio_file):
    message = st.chat_message("assistant")
    message.write("Transcribing your response...")
    model = whisper.load_model("base")
    result = model.transcribe(audio_file)

    return result
