import streamlit as st

# Function to set background image using an online image URL
def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Use a hosted image URL for background (Replace with your actual image URL)
background_url = "https://your-image-hosting.com/background.png"  # Change this to your actual image link
set_background(background_url)

# Dictionary mapping names to image URLs
person_images = {
    "Saroj Kumar Das": "https://your-image-hosting.com/saroj.jpg",
    "Kuni": "https://your-image-hosting.com/kuni.jpg",
    "Deepak Kumar Das": "https://your-image-hosting.com/deepak.jpg",
    "Sanjib Das": "https://your-image-hosting.com/sanjib.jpg",
    "Priyanka Priyadarshini Das": "https://your-image-hosting.com/priyanka.jpg",
    "Samapika Das": "https://your-image-hosting.com/samapika.jpg",
    "Sasmita Das": "https://your-image-hosting.com/sasmita.jpg",
    "Madhusudan Das": "https://your-image-hosting.com/madhusudan.jpg",
    "Chiranjib Das": "https://your-image-hosting.com/chiranjib.jpg",
    "Bhabani Sankar Das": "https://your-image-hosting.com/bhabani.jpg",
    "Prasant Das": "https://your-image-hosting.com/prasant.jpg",
    "Hitanshu Sekhar Das": "https://your-image-hosting.com/hitanshu.jpg",
    "Chittaranjan Das": "https://your-image-hosting.com/chittaranjan.jpg",  # Your photo URL
    "Subhashree Das": "https://your-image-hosting.com/subhashree.jpg",
    "Pihu": "https://your-image-hosting.com/pihu.jpg",
    "Som": "https://your-image-hosting.com/som.jpg",
    "Ayush": "https://your-image-hosting.com/ayush.jpg",
    "Goggle": "https://your-image-hosting.com/goggle.jpg"
}

st.title("Family Member Image Viewer")
st.write("Select a family member to see their image.")

# Dropdown to select a person
selected_person = st.selectbox("Select a person:", ["Select"] + list(person_images.keys()))

# Display the selected person's image if available
if selected_person != "Select":
    image_url = person_images.get(selected_person, "")

    if image_url:  # Ensure URL is not empty
        st.image(image_url, caption=selected_person, use_column_width=True)
    else:
        st.warning("No image available")
