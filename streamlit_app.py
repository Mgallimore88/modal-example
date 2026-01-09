import streamlit as st
from pathlib import Path

st.title("Video Player on Modal")

videos = list(Path("/data/galaxy").glob("*.mp4"))
if videos:
    selected = st.selectbox(
        "Select a video to play", videos, format_func=lambda x: x.name
    )
    st.video(str(selected))
else:
    st.write("No videos found in the volume.")
