import speech_recognition as sr
import pyttsx3
import wikipedia
import datetime
import requests
import json

# initialize speech recognition engine
r = sr.Recognizer()

# initialize text to speech engine
engine = pyttsx3.init()

# set voice properties
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# function to get current time
def get_time():
    now = datetime.datetime.now()
    time = now.strftime("%H:%M:%S")
    speak("The time is " + time)

# function to get weather information
# def get_weather():
#     # API endpoint for weather updates
#     url = "http://api.openweathermap.org/data/2.5/weather?q=city_name&appid=your_api_key"
#
#     # replace city_name with your desired location and your_api_key with your OpenWeatherMap API key
#     response = requests.get(url)
#     data = json.loads(response.text)
#
#     # parse weather data
#     temperature = int(data['main']['temp'] - 273.15)
#     description = data['weather'][0]['description']
#     humidity = data['main']['humidity']
#
#     # speak weather updates
#     speak("The temperature in city_name is " + str(temperature) + " degrees Celsius.")
#     speak("The weather is " + description + " with " + str(humidity) + " percent humidity.")

# function to search the web using Wikipedia
def search_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia, " + result)
    except:
        speak("I'm sorry, I could not find any information on that.")

# main function
def main():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said: " + command)

        if "time" in command:
            get_time()
        # elif "weather" in command:
        #     get_weather()
        elif "search" in command:
            query = command.split("for")[-1]
            search_wikipedia(query)
        else:
            speak("I'm sorry, I don't understand that command.")

    except:
        speak("I'm sorry, I could not recognize your voice. Please try again.")

if __name__ == "__main__":
    while True:
        main()
