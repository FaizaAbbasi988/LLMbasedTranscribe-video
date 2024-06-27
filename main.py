import os
import uuid
import sys
import timeit
import time
import whisper
import os
import google.generativeai as genai

from moviepy.editor import VideoFileClip
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key= "AIzaSyDxVTHSjlpSoJ1_uGMgAoszjSicT2LC4xs"
)

from transcribe import transcribe
from summaryy import generate_gemini_content

def video_audio(video_path):
    video = VideoFileClip(video_path)
    audio_path = f"./output/{uuid.uuid4()}.wav"
    video.audio.write_audiofile(audio_path)
    return audio_path

prompt="you are a text sumamrizer. your job is to take the text and provide the summary in point-wise fashion. the text is as follow:"


async def process_video_text(video_path):
    audio_path = video_audio(video_path)
    elapsed_time, transcript_path = transcribe(audio_path)
    print(f"Audio has been transcribed in {elapsed_time} seconds. Path: {transcript_path}")
    summary_text = generate_gemini_content(transcript_path, prompt)
    print(summary_text)
    summary_file_name = "summary.txt"
    summary_file_path = f"./output/summary.txt"
    with open(summary_file_path, "w", encoding="utf-8") as summary_file:
        summary_file.write(summary_text)

if __name__ == "__main__":
    video_path = r"D:\practise\transcribe-project\The Vision.mp4"
    import asyncio
    asyncio.run(process_video_text(video_path))
