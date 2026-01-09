# Modal app to run a Streamlit web server that plays videos from a Modal Volume
import modal, subprocess

image = modal.Image.debian_slim(python_version="3.11").pip_install("streamlit")
image = image.add_local_file(
    local_path="streamlit_app.py", remote_path="/root/streamlit_app.py"
)

app = modal.App("video-app")
volume = modal.Volume.from_name("galaxy-video-storage", create_if_missing=True)


@app.function(image=image, volumes={"/data": volume})
@modal.concurrent(max_inputs=100)
@modal.web_server(8000)
def run():
    subprocess.Popen(
        "streamlit run /root/streamlit_app.py --server.port 8000 --server.enableCORS=false --server.enableXsrfProtection=false",
        shell=True,
    )
