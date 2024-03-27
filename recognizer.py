import speech_recognition as sr
import webbrowser

# Initialize recognizer
recognizer = sr.Recognizer()

# Function to open YouTube
def open_youtube():
    webbrowser.open('https://www.youtube.com')

# Function to open Google
def open_google():
    webbrowser.open('https://www.google.com')

# Function to open Amazon
def open_amazon():
    webbrowser.open('https://www.amazon.com')

# Function to open Facebook
def open_facebook():
    webbrowser.open('https://www.facebook.com')

# Function to open any website
def open_website(website):
    webbrowser.open('https://www.' + website + '.com')

# Function to handle user commands
def handle_command(command):
    if 'open YouTube' in command:
        open_youtube()
        return True
    elif 'open Google' in command:
        open_google()
        return True
    elif 'open Amazon' in command:
        open_amazon()
        return True
    elif 'open Facebook' in command:
        open_facebook()
        return True
    elif 'open' in command:
        website = command.split("open ")[1]
        open_website(website)
        return True
    return False

# Function to listen to user's voice
def listen_to_voice():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        return ""
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return ""

# Main function
def main():
    while True:
        command = listen_to_voice()
        if command.lower() == 'exit':
            break
        handle_command(command)

if __name__ == "__main__":
    main()
