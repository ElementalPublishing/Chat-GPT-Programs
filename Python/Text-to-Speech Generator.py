import os
import requests

# Replace YOUR_API_KEY with your actual API key
API_KEY = "YOUR_API_KEY"

# Replace YOUR_RHYME with your actual rhyme
rhyme = """
YOUR_RHYME
"""

# Set the text-to-speech parameters
params = {
    "input": {
        "text": rhyme
    },
    "voice": {
        "languageCode": "en-US",
        "name": "en-US-Standard-B"
    },
    "audioConfig": {
        "audioEncoding": "LINEAR16",
        "sampleRateHertz": 16000
    }
}

# Send the request to the Google Text-to-Speech API
response = requests.post(
    "https://texttospeech.googleapis.com/v1/text:synthesize",
    json=params,
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
)

# Save the audio data to a .wav file
with open("rhyme.wav", "wb") as f:
    f.write(response.content)

# Print a message to confirm that the .wav file was saved
print("Rhyme saved as rhyme.wav")