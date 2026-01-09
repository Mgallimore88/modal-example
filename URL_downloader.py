# Modal function to get a video from an online URL and store it in a Modal Volume
# Use modal run URL_downloader.py to execute

import modal

image = modal.Image.debian_slim().pip_install("requests")
app = modal.App("video-app")
volume = modal.Volume.from_name("my-video-storage", create_if_missing=True)


@app.function(image=image, volumes={"/data": volume})
def upload_video_from_url(url: str):
    import requests

    response = requests.get(url, stream=True)
    with open("/data/video.mp4", "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    volume.commit()
    return "Video uploaded to Modal Volume!"


@app.local_entrypoint()
def main():
    url = "https://www.dropbox.com/scl/fi/9s3vo9hst9okhbfb932v2/testvid.mp4?rlkey=b0ehpuzpnuxplw1byfw94wvpo&st=7iacxgxc&dl=1"
    print(upload_video_from_url.remote(url))
