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
--------------------------
import os
import azure.cognitiveservices.speech as speechsdk

def recognize_from_microphone():
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_translation_config = speechsdk.translation.SpeechTranslationConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
    speech_translation_config.speech_recognition_language="en-US"

    target_language="it"
    speech_translation_config.add_target_language(target_language)

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    translation_recognizer = speechsdk.translation.TranslationRecognizer(translation_config=speech_translation_config, audio_config=audio_config)

    print("Speak into your microphone.")
    translation_recognition_result = translation_recognizer.recognize_once_async().get()

    if translation_recognition_result.reason == speechsdk.ResultReason.TranslatedSpeech:
        print("Recognized: {}".format(translation_recognition_result.text))
        print("""Translated into '{}': {}""".format(
            target_language, 
            translation_recognition_result.translations[target_language]))
    elif translation_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(translation_recognition_result.no_match_details))
    elif translation_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = translation_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")

recognize_from_microphone()
----------------

import seamlessm4t as sm4t

# Replace 'your_mp3_file_path.mp3' with the path of your MP3 file
file_path = 'your_mp3_file_path.mp3'

# Upload the file using seamlessm4t
audio_data = sm4t.upload(file_path)
______________________

import torchaudio

def load_audio_from_mp3(file_path):
    """
    Load an audio sample from a given MP3 file.
    
    Args:
    file_path (str): The path to the MP3 file.

    Returns:
    Tuple[Tensor, int]: A tuple containing the audio waveform and the sampling rate.
    """
    waveform, sample_rate = torchaudio.load(file_path)
    return waveform, sample_rate

# Example usage
file_path = '/path/to/your/file.mp3'  # Replace with your MP3 file path
waveform, sample_rate = load_audio_from_mp3(file_path)

print(f"Sampling rate: {sample_rate}")
# You can now use 'waveform' and 'sample_rate' as needed in your application
--------------------

from pydub import AudioSegment
from pydub.playback import play
import io

# Load an MP3 file
def load_mp3(file_path):
    audio = AudioSegment.from_mp3(file_path)
    return audio

# Play the audio
def play_audio(audio):
    play(audio)

# Example usage
file_path = '/path/to/your/file.mp3'  # Replace with your MP3 file path
audio = load_mp3(file_path)
play_audio(audio)

