import streamlit as st
import requests
from PIL import Image
import io

# Function to query the API and generate image
def generate_image(prompt):
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
    headers = {"Authorization": "Bearer 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"}

    # Query API with the provided prompt
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    
    # Check if the request was successful
    if response.status_code == 200:
        # Decode image bytes and return PIL image
        image_bytes = response.content
        image = Image.open(io.BytesIO(image_bytes))
        return image
    else:
        st.error("Failed to generate image. Please try again.")

# Streamlit App
def main():
    st.title("Image Generation from Prompt")
    st.write("Enter a prompt to generate an image.")

    # Input prompt from user
    prompt = st.text_input("Enter a prompt:")

    # Check if prompt is provided
    if prompt:
        # Generate image upon button click
        if st.button("Generate Image"):
            with st.spinner("Generating Image..."):
                # Call function to generate image
                generated_image = generate_image(prompt)
            # Display generated image
            st.image(generated_image, caption='Generated Image', use_column_width=True)

if __name__ == "__main__":
    main()
