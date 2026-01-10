# Modal video hosting demo

## Usage:

## Auth

`modal token new`  
Auth token appears in `~/.modal.toml`  
`ls ~/.modal.toml`

### b2

Secrets go in the .env file and are named
B2_KEY_NAME  
B2_KEY_ID  
B2_APP_KEY  
B2_BUCKET_NAME  
B2_ENDPOINT

## Create volume and upload videos

`modal volume create my-video-storage`  
`modal volume put my-video-storage ./videos/ /`  
where the final 2 args (`./videos`, and `/`) are the local path and the path inside the volume.

## Editing via terminal

unwanted files can be removed with `modal volume rm`:  
`modal volume rm my-video-storage "galaxy/.DS_Store"`

You can check contents with:  
`modal volume ls my-video-storage galaxy`

## Serve the app

`modal serve video_app.py`  
then open the URL printed in the terminal

### Note on speed:

Using the upload_videos.py script was around 60x faster than using the modal volume put command. The modal put command was ran first, so the speedup could be due to caching. Not tested further. If the speedup turns out to be real, try using thread pool execution for further upload speedup.
