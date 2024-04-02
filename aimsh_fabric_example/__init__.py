from __future__ import annotations
import re
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv, set_key

# requires pip install youtube-transcript-api

def get_video_id(url):
    # Extract video ID from URL
    pattern = r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})"
    match = re.search(pattern, url)
    return match.group(1) if match else None

def set_youtube_api_key(apikey: str):
    set_key(dotenv_path=".env", key_to_set="YOUTUBE_API_KEY", value_to_set=apikey)

def get_transcript(url: str) -> str:
    load_dotenv(".env")
    video_id = get_video_id(url)
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
    transcript_text = " ".join([item["text"] for item in transcript_list])
    transcript_text = transcript_text.replace("\n", " ")
    return transcript_text

def bind(binder):
    binder.bind_post("/set_youtube_api_key", set_youtube_api_key, "Set YouTube API key")
    binder.bind_post("/youtube_transcript", get_transcript, "Get transcript of video")
