import streamlit as st
from pathlib import Path

st.title("Video Player on Modal")

folders = [Path("/data")] + list(Path("/data").iterdir())
folders = [f for f in folders if f.is_dir()]

selected_folder = st.selectbox(
    "Select folder", folders, format_func=lambda x: x.name or "root"
)
videos = list(selected_folder.glob("*.mp4"))

if videos:
    selected = st.selectbox("Select a video", videos, format_func=lambda x: x.name)
    st.video(str(selected))
else:
    st.write("No videos in this folder")
