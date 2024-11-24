import streamlit as st
from PIL import Image
import base64
import io
import add
import sub
import mult
import divid

# Set the page config as the very first Streamlit command
st.set_page_config(page_title="My Calculator", page_icon=":wave:", layout="wide")

def get_image_base64(image_path):
    """Encodes an image to base64 for embedding."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

def display_round_image(image_path):
    """Displays an image with rounded borders."""
    try:
        image = Image.open(image_path)
        buffered = io.BytesIO()
        image.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        st.markdown(
            f'<img src="data:image/jpeg;base64,{img_str}" class="img-fluid" style="border-radius: 50%; width: 150px; height: 150px; object-fit: cover; display: block; margin-left: auto; margin-right: auto; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);">',
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.error("Error: Image file not found. Please check the path and try again.")

def main():
    st.sidebar.title("Navigation")
    choice = st.sidebar.selectbox("Go to", ["Calculator", "About Me"])

    if choice == "Calculator":
        run_calculator()
    elif choice == "About Me":
        run_about_me()

def run_calculator():
    """Function to run the calculator logic."""
    st.title("Simple Calculator")
    num1 = st.number_input("Enter First Number", format="%f")
    num2 = st.number_input("Enter Second Number", format="%f")
    operation = st.selectbox("Choose an operation", ["Add", "Subtract", "Multiply", "Divide"])

    if st.button("Calculate"):
        if operation == "Add":
            result = add.add(num1, num2)
        elif operation == "Subtract":
            result = sub.sub(num1, num2)
        elif operation == "Multiply":
            result = mult.multi(num1, num2)
        elif operation == "Divide":
            result = divid.divide(num1, num2)
        st.success(f"The result is {result}")

def run_about_me():
    """Function to run the About Me page."""
    st.subheader("Hello! I'm Muhammad")
    st.write("""
    I'm a Certified Cloud Applied Generative AI Engineer specializing in Full Stack Web Development 
    with a focus on MicroServices and GPT integration. I develop Web 2.0 applications with custom GPTs 
    and chatbots, and have experience with Smart Contracts in Generative AI.
    """)

    display_round_image("Portfolio-portrait-.jpeg")

    st.subheader("Watch My Short Film")
    video_url = "https://www.youtube.com/embed/QW9yOYjvlWc"
    st.markdown(f'<div class="video-container"><iframe src="{video_url}" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe></div>', unsafe_allow_html=True)

    st.subheader("Activities and Societies:")
    st.write("""
    - President, Junior Biological Club (2023-24)
    - Finance Secretary, Junior Biological Club (2022-23)
    - Parliamentary Debater, Formanites Debating Society (2022-24)
    - And More
    """)

    st.subheader("Technologies I've been working with recently:")
    techs = ["Python", "Custom GPTs", "Streamlit", "TypeScript", "Docker", "Cloud Computing", "Generative AI"]
    st.write(", ".join(techs))

    st.subheader("Connect With Me")
    st.write("""
    - [LinkedIn](https://www.linkedin.com/in/muhammad-bodla)
    - [Facebook](https://www.facebook.com/muhammadbodla)
    - [Instagram](https://www.instagram.com/muhammadbodla)
    - [GitHub](https://github.com/muhammadbodla)
    - [YouTube](https://www.youtube.com/muhammadbodla)
    - [Email](mailto:mianmuhammadbodla@gmail.com)
    """)

    st.write("Thank you for visiting my profile. Looking forward to connecting and collaborating on innovative projects!")

if __name__ == "__main__":
    main()









