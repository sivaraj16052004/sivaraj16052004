import speech_recognition as sr

# Create a speech recognition object
recognizer = sr.Recognizer()

# Function to recognize speech from the microphone
def recognize_speech():
    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)  # Optional: Adjust for ambient noise
        audio_data = recognizer.listen(source)

        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio_data)
            print(f"Google Web Speech Recognition: {text}")
        except sr.UnknownValueError:
            print("Google Web Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech Recognition service; {e}")

if __name__ == "__main__":
    recognize_speech()
