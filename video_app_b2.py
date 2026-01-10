# Modal app to run a Streamlit web server that plays videos from a b2 Volume
import modal, subprocess, os


image = modal.Image.debian_slim(python_version="3.11").pip_install("streamlit")
image = image.add_local_file(
    local_path="streamlit_app.py", remote_path="/root/streamlit_app.py"
)

b2_secret = modal.Secret.from_name("b2-credentials")

app = modal.App("video-app")

b2_mount = modal.CloudBucketMount(
    "mike-test-bucket",
    secret=b2_secret,
    bucket_endpoint_url="https://s3.us-west-004.backblazeb2.com",
)


@app.function(image=image, volumes={"/data": b2_mount})
@modal.concurrent(max_inputs=100)
@modal.web_server(8000)
def run():
    subprocess.Popen(
        "streamlit run /root/streamlit_app.py --server.port 8000 --server.enableCORS=false --server.enableXsrfProtection=false",
        shell=True,
    )
