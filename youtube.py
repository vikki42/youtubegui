from pytube import YouTube

# Replace VIDEO_URL with the URL of the YouTube video you want to download
video_url = "VIDEO_URL"

# Create a YouTube object
yt = YouTube(video_url)

# Get the highest resolution stream
stream = yt.streams.get_highest_resolution()

# Replace FILE_PATH with the path and filename where you want to save the video
file_path = "FILE_PATH"

# Download the video
stream.download(file_path)
