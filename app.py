import streamlit as st
from PIL import Image
from helper import get_gemini_response, input_image_setup

# Initialize Streamlit app
st.set_page_config(page_title="Gemini Image Demo")

st.header("Invoice Extractor using Gemini Pro")

# Sidebar elements
uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
input_text = st.sidebar.text_input("Input Prompt: ", key="input")
submit = st.sidebar.button("Submit")

# Main screen layout
col1, col2 = st.columns([2, 3])  # Adjust column ratios as needed

with col1:
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

input_prompt = """
               You are an expert in understanding invoices.
               You will receive input images as invoices &
               you will have to answer questions based on the input image
               """

with col2:
    # If ask button is clicked
    if submit:
        if uploaded_file is not None:
            try:
                image_data = input_image_setup(uploaded_file)
                response = get_gemini_response(input_prompt, image_data, input_text)
                st.subheader("The Response is")
                st.write(response)
            except FileNotFoundError as e:
                st.error(str(e))
        else:
            st.error("Please upload an image.")
