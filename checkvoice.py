import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Set the voice to an eSpeak voice
engine.setProperty('voice', 'en  en+f2')  # Replace 'en-us' with the desired eSpeak voice name

# Set other properties (optional)
engine.setProperty('rate', 150)  # Speech rate (words per minute)
engine.setProperty('volume', 0.8)  # Speech volume (0.0 to 1.0)

# Text to be spoken
text = "Hello, Alice!"

# Speak the text
engine.say(text)

# Run the engine
engine.runAndWait()
