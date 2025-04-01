import streamlit as st
import base64
import os

# Function to set background image (supports both local file and URL)
def set_background(image_source):
    if image_source.startswith("http"):  # If it's a URL
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("{image_source}");
                background-size: cover;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    elif os.path.exists(image_source):  # If it's a local file
        with open(image_source, "rb") as f:
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

# Set background image
background_path = 'https://images2.alphacoders.com/123/1235143.png'  # URL instead of local path
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
    "Chittaranjan Das": "Pic.jpg",
    "Subhashree Das": "",
    "Pihu": "Pihu.png",
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
    
    if image_path:
        if image_path.startswith("http"):  # If the image is a URL
            st.image(image_path, caption=selected_person, use_container_width=True)
        elif os.path.exists(image_path):  # If it's a local file
            st.image(image_path, caption=selected_person, use_container_width=True)
        else:
            st.warning("No image available")
    else:
        st.warning("No image available")
