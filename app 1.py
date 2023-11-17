import streamlit as st
import requests  # If your API uses HTTP requests


def fetch_api_data(input_data):
    # Replace with actual API call
    # response = requests.get(f'YourAPIEndpoint?data={input_data}')
    response = "This is the summary"
    return response  # or response.text based on API response

st.title("Formal Letter Generator")

# Collecting user inputs

col1, col2 = st.columns(2)
with col1:     
    input1 = st.text_input("record_id")
    input2 = st.text_input("Date")
    input3 = st.text_input("short_desc")
    input6 = st.text_input("country")
with col2:
    input4 = st.text_input("product")
    input5 = st.text_input("batch_no")
    api_input = st.text_input("investigation_summary_ind")
    


letter_template = f"""
Dear {input1},

I am writing to discuss {input2}. We have recently {input3} and require your assistance.

Based on your expertise in {input4}, we believe you can provide valuable insights. Additionally, our recent findings are: {api_input}.

Please let us know your availability to discuss this further.

Sincerely,
{input5}
"""
if st.button("Generate Letter"):
    api_response = fetch_api_data(api_input)
    # Generate and display the letter
    generated_letter = letter_template.format(
        input1=input1,
        input2=input2,
        input3=input3,
        input4=input4,
        api_response=api_response,
        input5=input5
    )
    st.text(generated_letter)
