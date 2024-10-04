import speech_recognition as sr


def stt():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(
            source, duration=1
        )  # Adjust for ambient noise
        print("Being Recorded. Stop talking for 10 seconds will end session.")
        audio = recognizer.listen(source, timeout=10)  # Capture audio

    try:
        # Recognize speech using Google Web Speech API
        print("Processing")
        text = recognizer.recognize_google(audio)

    except sr.UnknownValueError:
        print("Could not recognize audio.")
    except sr.RequestError as e:
        print(f"Error with Google Speech Recognition service: {e}")


# Call the function to test speech recognition
stt()
