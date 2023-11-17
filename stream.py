# Import Streamlit
import streamlit as st

# Set page config to wide mode for more space
st.set_page_config(layout="wide")

# Your long text
generated_text = "your very long text"

# Apply custom CSS with unsafe_allow_html to force wrapping
st.markdown("""
    <style>
    .stText {
        white-space: pre-wrap;
    }
    </style>
    """, unsafe_allow_html=True)

# Display text with wrapping
st.text(generated_text)