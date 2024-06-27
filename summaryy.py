from dotenv import load_dotenv
load_dotenv()
import os
import google.generativeai as genai
genai.configure(api_key= "apikey"
)





prompt="you are a text sumamrizer. your job is to take the text and provide the summary in point-wise fashion. the etxt is as follow:"
def generate_gemini_content(text,prompt):
    model =genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt+text)
    return response.text


if __name__ == "__main__":
    text = r"D:\practise\transcribe-project\output\cafb4a61-2bc4-4a3e-b0cc-a7f1a7c1d367.txt"
    generate_gemini_content(text,prompt)

