# helper script to implement modal CLI.
# Can also use terminal commands directly, e.g.
# modal volume put my-video-storage ./my_video.mp4 /video.mp4

import subprocess
from pathlib import Path


def upload_videos(local_dir: str, remote_path: str = "/"):
    for p in Path(local_dir).glob("*"):
        subprocess.run(
            [
                "modal",
                "volume",
                "put",
                "my-video-storage",
                str(p),
                f"{remote_path}/{p.name}",
            ]
        )


if __name__ == "__main__":
    upload_videos("./videos", "/test-upload-location")
