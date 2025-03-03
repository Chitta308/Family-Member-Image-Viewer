import streamlit as st
import base64

# Function to set background image
def set_background(image_file):
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

# Set background image (change 'background.jpg' to your image file)
set_background("C:/Users/chitt/OneDrive/Pictures/Screenshots/Background.png")

# Dictionary mapping names to image paths or URLs
person_images = {
    "Saroj Kumar Das": "",
    "Kuni": "",
    "Deepak Kumar Das": "",
    "Sanjib Das": "",
    "Priyanka Priyadarshini Das": "",
    "Samapika Das":"",
    "Sasmita Das":"",
    "Madhusudan Das": "",
    "Chiranjib Das": "",
    "Bhabani Sankar Das": "",
    "Prasant Das": "",
    "Hitanshu Sekhar Das": "",
    "Chittaranjan Das": "Pic.jpg",
    "Subhashree Das":"",
    "Pihu": "",
    "Som": "",
    "Ayush": "",
    "Goggle": ""
    
}

st.title("Family Member Image Viewer")
st.write("In this app, when a family member selects their name, their own image will appear, creating a personalized and heartwarming experience. It’s a special way to celebrate our bond, making every interaction more meaningful and bringing the Das Family even closer together! 😊")

# Dropdown to select a person
selected_person = st.selectbox("Select a person:", ["Select"] + list(person_images.keys()))

# Display the image only if a valid person is selected
if person_images[selected_person]:
    st.image(person_images[selected_person], caption=selected_person, use_container_width=True)
else:
    st.warning("No image available for this person.")
