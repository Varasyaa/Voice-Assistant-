import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function for speaking the assistant's response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function for listening to user commands
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User said: {query}")
        return query.lower()
    except Exception as e:
        print("Sorry, I couldn't understand. Could you repeat?")
        return None

# Function to tell the time
def tell_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return f"The current time is {current_time}"

# Function to get a summary from Wikipedia
def get_wikipedia_summary(query):
    try:
        summary = wikipedia.summary(query, sentences=1)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"There are multiple results for {query}. Could you be more specific?"
    except wikipedia.exceptions.HTTPTimeoutError:
        return "Sorry, I couldn't fetch information from Wikipedia at the moment."

# Main function to handle commands
def run_assistant():
    speak("Hello! How can I assist you today?")
    
    while True:
        query = listen()
        
        if query:
            if "time" in query:
                response = tell_time()
                speak(response)
            elif "hello" in query or "hi" in query:
                speak("Hello! How can I help you?")
            elif "wikipedia" in query:
                speak("What do you want to know?")
                query = listen()  # Get the Wikipedia search query from the user
                response = get_wikipedia_summary(query)
                speak(response)
            elif "stop" in query or "exit" in query:
                speak("Goodbye!")
                break
            else:
                speak("I'm sorry, I didn't understand that.")
        else:
            continue

# Run the assistant
if __name__ == "__main__":
    run_assistant()
