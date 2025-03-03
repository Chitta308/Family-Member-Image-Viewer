import streamlit as st
import base64
import os

# Function to set background image
def set_background(image_file):
    if os.path.exists(image_file):  # Ensure file exists before opening
        with open(image_file, "rb") as f:
            encoded_string = base64.b64encode(f.read()).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/png;base64,{encoded_string}");
                background-size: cover;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning("Background image not found!")

# Set background image (change to your actual file path)
background_path = "C:/Users/chitt/OneDrive/Pictures/Screenshots/Background.png"
set_background(background_path)

# Dictionary mapping names to image paths or URLs
person_images = {
    "Saroj Kumar Das": "",
    "Kuni": "",
    "Deepak Kumar Das": "",
    "Sanjib Das": "",
    "Priyanka Priyadarshini Das": "",
    "Samapika Das": "",
    "Sasmita Das": "",
    "Madhusudan Das": "",
    "Chiranjib Das": "",
    "Bhabani Sankar Das": "",
    "Prasant Das": "",
    "Hitanshu Sekhar Das": "",
    "Chittaranjan Das": "C:/Users/chitt/OneDrive/Pictures/image/Pic.jpg",
    "Subhashree Das": "",
    "Pihu": "",
    "Som": "",
    "Ayush": "",
    "Goggle": ""
}

st.title("Family Member Image Viewer")
st.write("Select a family member to see their image.")

# Dropdown to select a person
selected_person = st.selectbox("Select a person:", ["Select"] + list(person_images.keys()))

# Ensure "Select" does not cause an error
if selected_person != "Select":
    image_path = person_images.get(selected_person, "")
    
    if image_path and os.path.exists(image_path):  # Check if the image file exists
        st.image(image_path, caption=selected_person, use_container_width=True)
    else:
        st.warning("No image available")
