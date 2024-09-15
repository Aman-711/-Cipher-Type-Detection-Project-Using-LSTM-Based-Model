import streamlit as st
from PIL import Image

# Set the page configuration
st.set_page_config(page_title="Cryptr", layout="wide")

# Custom CSS for the header, subheader, and other elements
st.markdown("""
    <style>
        /* Light blue header style */
        .header {
            background-color: lightblue;
            padding: 20px; /* Padding inside the header */
            border-bottom: 1px solid #ccc;
            box-shad
            ow: 0 2px 5px rgba(0, 0, 0, 0.1);
            position: fixed; /* Fix the position to the top */
            top: 0;
            left: 0;
            width: 100%;
            box-sizing: border-box; /* Ensure padding and border are included in the width */
            z-index: 100; /* Ensure it stays on top of other content */
            display: flex; /* Use flexbox to align items */
            align-items: center; /* Center items vertically */
            justify-content: space-between; /* Space between brand and links */
        }
        .header .brand {
            font-size: 24px; /* Font size for brand text */
            margin: 0;
            padding: 0 20px; /* Padding to ensure spacing from edges */
            font-family: sans-serif;
            color: #007bff;
            text-align: left; /* Align text to the left */
        }
        .header .nav-links {
            display: flex; /* Use flexbox for link alignment */
        }
        .header .nav-links a {
            margin-left: 30px; /* Increased spacing between links */
            font-size: 18px;
            color: #007bff;
            text-decoration: none;
            font-family: sans-serif;
        }
        .header .nav-links a:hover {
            text-decoration: underline;
        }
        .container {
            padding-top: 60px; /* Reduced padding to decrease the gap */
            max-width: 1200px; /* Limit the maximum width of the content */
            margin: 0 auto; /* Center the container */
            box-sizing: border-box; /* Ensure padding is included in the width */
        }
        /* Styling for subheaders and reducing gap between subheader and input box */
        .container .stSubheader {
            margin-bottom: 10px; /* Adjust this value to reduce the gap */
        }
        /* Styling for input area to make it larger */
        .stTextArea textarea {
            font-size: 16px; /* Increase font size */
            height: 250px; /* Increase height */
            width: 100%; /* Full width */
            box-sizing: border-box; /* Ensure padding and border are included in the width */
        }
        /* Styling for output area to look like an input box */
        .output-box {
            font-size: 16px; /* Match font size with input area */
            height: 80px; /* Set height to match the input box */
            width: 100%; /* Full width */
            background-color: #ffffff; /* White background to match input boxes */
            border: 2px solid #d0d0d0; /* Border color similar to input boxes */
            border-radius: 5px; /* Match border-radius of input boxes */
            resize: none; /* Prevent resizing */
            padding: 10px; /* Padding inside the box */
            box-sizing: border-box; /* Ensure padding is included in the width */
            color: #000000; /* Text color */
            overflow: hidden; /* Prevent scrollbars from appearing */
            cursor: not-allowed; /* Indicate that it's non-editable */
        }
    </style>
""", unsafe_allow_html=True)

# Light blue header area with clickable text
st.markdown("""
    <div class="header">
        <div class="brand">Diemos</div>
        <div class="nav-links">
            <a href="#Home">Home</a>
            <a href="#Encryptions">Encryptions</a>
            <a href="#AboutUs">About Us</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# Container to hold the rest of the content
st.markdown('<div class="container">', unsafe_allow_html=True)

# Manage page visibility based on user input
if 'page' not in st.session_state:
    st.session_state.page = 'Encryptions'

def show_encryptions():
    col1, col2 = st.columns([2, 1])  # Create two columns, with col1 being twice as wide as col2

    with col1:
        st.subheader("CipherText")
        st.text_area("", value="If he had anything confidential to say, he wrote it in cipher, that is, by so changing the order of the letters of the alphabet, that not a word could be made out.", height=250)

        # Add the Benchmark button with custom styling
        benchmark_button = st.button("Benchmark")

        if benchmark_button:
            st.write("Benchmark button clicked!")

        st.subheader("Encryption Method")

        # Using st.markdown with a preformatted block to display output
        st.markdown('<textarea class="output-box" readonly>Output. </textarea>', unsafe_allow_html=True)


def show_about_us():
    col1, col2 = st.columns([2, 1])  # Create two columns, with col1 being twice as wide as col2

    with col1:
        st.subheader("About Us")
        st.write("**Caesar cipher: Encode and decode online**")
        st.write("Method in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. The method is named after Julius Caesar, who used it in his private correspondence.")

    with col2:
        st.subheader("Visual Content")

        # Example for adding an image
        st.image("https://via.placeholder.com/300", caption="Example Image")

        # Example for adding a flowchart or any other visual content
        st.write("Here you can add your flowcharts or other visuals.")

# Check which section to display based on user clicks
if st.session_state.page == 'Encryptions':
    show_encryptions()
elif st.session_state.page == 'About Us':
    show_about_us()

# Close container div
st.markdown('</div>', unsafe_allow_html=True)
