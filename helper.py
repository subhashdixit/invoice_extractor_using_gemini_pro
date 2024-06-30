from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()  # take environment variables from .env.

# Configure the Generative AI model
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt, image, input_text):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input_text, image[0], input_prompt])
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
