from recording_modules import *
import streamlit as st
from gen_ai_modules import (
    text_prompt,
    encode_image,
    images_to_messages,
    fit_prompt_to_api_calls,
    gen_AI_call,
)


st.title("👀PitchPerfect🚀 - Let's practice a perfect pitch")

# Initialize session state for recording
if "recording" not in st.session_state:
    st.session_state["recording"] = False
# UIs

# Input your own questions
st.subheader("🧐How it works?")
st.write(
    "🧠Using Gen AI, (powered by OpenAI), it will provide detailed feecback taking your input information into consderation. 🎥It not only evaluate contents, but also give feedback about your posture, gesture, or eye contact through camera!!!"
)
st.write("🧪This version is very experimental, so open to ideas for improvement!")
st.subheader("What is your interview question to practice?")

question = st.text_area("🪄Put your own question", "Tell me about yourself")

st.subheader("💼Which Job / Position?")
role = st.text_input("Put a job role you are interviewing", "Data Scientist")

st.subheader("🏢Any target company?")
company = st.text_input("Just casually put lists of them!", "Amazon, Google, Meta")

st.subheader("⏱️Time limits")
time_option = st.selectbox(
    "Once you start, you should stay until end of time to see results",
    (10, 30, 60, 180, 300),
)

start_rec = st.button("Start!")

if start_rec and not st.session_state["recording"]:
    initialized_start_time = datetime.today().strftime("%Y-%m-%d_%H:%M:%S")

    response_text = start_recording(
        init_time=initialized_start_time, time_limit=time_option
    )

    path = f"record_{initialized_start_time}"
    images = [f"{path}/{i}" for i in os.listdir(path) if i.split(".")[-1] == "jpg"]

    print(images)

    call = fit_prompt_to_api_calls(
        text_prompt.format(question, role, company, response_text),
        images,
    )

    with st.spinner("GenAI is producing results..."):
        try:
            feedback_response = gen_AI_call(call)

            st.balloons()
            st.success("Successfully provied you a feedback!", icon="✅")
            message = st.chat_message("assistant")
            message.write(feedback_response)
        except:
            message = st.chat_message("assistant")
            message.write("There was an error. Maybe try again later")


else:
    stop_recording()
