# Imports
from pytube import YouTube
import certifi
import ssl
import urllib.request
import assemblyai as aai
import streamlit as st
from dotenv import load_dotenv
import os

# Video to Audio
def get_audio_file(url):
    try:
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        # Use the SSL context for urllib requests
        urllib.request.urlopen(url, context=ssl_context)
        video = YouTube(url)
        
        stream = video.streams.filter(only_audio=True).first()
        stream.download(filename="audio.mp3")
        print("Audio File downloaded in MP3")
    except KeyError:
        print("Unable to fetch video information. Please check the video URL or your network connection.")