import os
import sys
import timeit
import whisper
import uuid

def transcribe(audio_file):
    """
    Transcribes the given audio file using the Whisper model. Returns a tuple
    containing the transcription result and the elapsed time in seconds.
    """
    
    device = "cuda" 
    whisper_model = whisper.load_model("large-v3", device=device)

    start_time = timeit.default_timer()
    result = whisper_model.transcribe(audio_file)  # Call transcribe on the loaded model
    
    text_path = f"./output/{uuid.uuid4()}.txt"
    with open(text_path, "w") as file:
        file.write(result["text"])

    end_time = timeit.default_timer()
    elapsed_time = int(end_time - start_time)

    return elapsed_time, text_path

if __name__ == "__main__":
    
    audio_path = r"D:\practise\transcribe-project\output\89cc0eb8-56d3-414e-aec0-ba95bf8f5120.wav"
    elapsed_time, transcript_path = transcribe(audio_path)
    print(f"Audio has been transcribed in {elapsed_time} seconds. Path: {transcript_path}")
