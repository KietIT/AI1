import os
import playsound
import speech_recognition 
import time
import sys
import ctypes
import wikipedia
from datetime import datetime, date
import json
import re
import webbrowser
import smtplib
import requests
import urllib
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS
from youtube_search import YoutubeSearch
import pyttsx3
from pyowm import OWM
import pyaudio
import random


AI_ear = speech_recognition.Recognizer()
AI_mouth = pyttsx3.init()
language = 'vi'

while True:
	with speech_recognition.Microphone() as mic:
		AI_ear.adjust_for_ambient_noise(mic) 
		print("AI: I'm listening")
		audio = AI_ear.listen(mic, phrase_time_limit=8)
	try:
		you = AI_ear.recognize_google(audio)  
	except:
		you = ""

	print("You:" + you)
	rate = AI_mouth.getProperty('rate')
	AI_mouth.setProperty('rate', 175)
	voices = AI_mouth.getProperty('voices')
	AI_mouth.setProperty('voice', voices[1].id)

	if you == "":
		AI = "I can't hear you!"
		print(AI)
	elif "hello" in you:
		date_time = int(strftime('%H'))
		while True:
			if date_time < 12:
				AI = "Good morning! Have a good day. How can I help you?"
				print("AI:" + AI)	
				AI_mouth = pyttsx3.init()
				AI_mouth.say(AI)
				AI_mouth.runAndWait()
				break
			elif 12 <= date_time < 18:
				AI = "Good afternoon! What have you planned for this afternoon?"
				print("AI:" + AI)
				AI_mouth = pyttsx3.init()
				AI_mouth.say(AI)
				AI_mouth.runAndWait()	
				break
			elif 18 <= date_time <= 24:
				AI = "Good evening! Have you had dinner yet?"
				print("AI:" + AI)
				AI_mouth = pyttsx3.init()
				AI_mouth.say(AI)
				AI_mouth.runAndWait()	
				break	
	elif "introduce yourself" in you:
		AI = """I can do the following task such as:
		1. Greeting
		2. Show date and time
		3. Open excel, word, powerpoint
		4. Open website like Google, Youtube, Gmail,...
		5. See the weather of any city
		6. Remind you of the things to do
		7. Search for any information from wikipedia
		8. Say a funny sentence
		9. Turn off the screen when not in use """
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
		time.sleep(10)
	elif "word" in you:
		AI = "Ok! I'm opening "
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
		time.sleep(1)
		os.startfile('C:\Program Files (x86)\Microsoft Office\Office16\WINWORD.EXE')
	elif "Microsoft" in you:
		AI = "Ok! I'm opening "
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
		os.startfile("C:\Program Files (x86)\Microsoft Office\Office16\EXCEL.EXE") 
	elif "open" in you:
		AI = "Ok! I'm opening "
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
		os.startfile('C:\Program Files (x86)\Microsoft Office\Office16\POWERPNT.EXE')
	elif "team" in you:
		AI = "Ok! I'm opening "
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
		os.startfile('C:\\Users\\Admin\\OneDrive\\Desktop\\Microsoft Teams.lnk')
	elif "today" in you:
		today = date.today()
		AI = today.strftime("%B %d, %Y")
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
	elif "time" in you:
		now = datetime.now()
		AI = now.strftime("%H hours %M minutes %S seconds")
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
	elif "bye" in you:
		AI = "Bye Kiệt"
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
	elif "America" in you:
		AI = "Joe Biden"
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
	elif "Russia" in you:
		AI = "Vladimir Putin"
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
	elif 'how are you' in you:
		AI="I'm fine, thank you!"
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
	elif 'how old are you' in you:
		AI="I'm zero year old"
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
	elif "thank you" in you:
		AI='You are welcome'
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
	elif "name" in you:
		AI="My name is AI"
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
	elif "do you know me" in you:
		AI = "Yes, I know. You are Kiệt"
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
	elif 'sleep 5 second' in you:
		AI='Finish'
		time.sleep(5)
	elif 'shut down' in you:
		os.system('shutdown -s')
	elif 'restart' in you:
		os.system('shutdown -r')
	elif "YouTube" in you:
		webbrowser.open('https://www.youtube.com',new=2)
		AI="Ok!Bye"	
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
	elif "Google" in you:
		webbrowser.open('https://www.google.com.vn/',new=2)
		AI="Ok!Bye"	
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
	elif "Apple" in you:
		webbrowser.open('https://www.apple.com/',new=2)
		AI="Ok!Bye"	
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
	elif "Facebook" in you:
		webbrowser.open('https://www.facebook.com/',new=2)
		AI="Ok!Bye"
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
	elif "Gmail" in you:
		webbrowser.open('https://mail.google.com/mail/u/0/#inbox',new=2)
		AI="Ok!Bye"
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
	elif "temperature" in you:
		while True:
			AI = "Where do you want to see the weather?"
			print("AI:" + AI)
			AI_mouth = pyttsx3.init()
			AI_mouth.say(AI)
			AI_mouth.runAndWait()
			ow_url = "http://api.openweathermap.org/data/2.5/weather?"
			city = input()
			if not city:
				pass
			api_key = "fe8d8c65cf345889139d8e545f57819a"
			call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
			response = requests.get(call_url)
			data = response.json()
			if data["cod"] != "404":
				city_res = data["main"]
				current_temperature = city_res["temp"]
				current_pressure = city_res["pressure"]
				current_humidity = city_res["humidity"]
				wthr = data["weather"]
				weather_description = wthr[0]["description"]
				now = date.today()
				content = """
				Hôm nay là ngày {day} tháng {month} năm {year}
				Nhiệt độ trung bình là {temp} độ C
				Áp suất không khí là {pressure}Pa
				Độ ẩm là {humidity}%
				""".format(day = now.day,month = now.month, year= now.year, 	                                                                           	   
	                       temp = current_temperature, pressure = current_pressure, humidity = current_humidity)
				print(content)
			else:
				AI = "Your address could not be found!"
				print(AI)
				AI_mouth = pyttsx3.init()
				AI_mouth.say(AI)
				AI_mouth.runAndWait()
			break
	elif "alarm" in you:
		hour = int(input("Hour:"))
		minutes = int(input("Minutes:"))
		print("Nhắc nhở đã được cài")
		while True:
			if hour == int(datetime.today().strftime("%H")) and minutes == int(datetime.today().strftime("%M")):
				AI = "It's time!"
				print(AI)					
				AI_mouth = pyttsx3.init()
				AI_mouth.say(AI)
				AI_mouth.runAndWait()
				os.system("start iphone.mp3")
				break
	elif "Wikipedia" in you:
		with speech_recognition.Microphone() as mic:
			print("Wikipedia: ...")
			audio = AI_ear.listen(mic)
		try:
			wiki = AI_ear.recognize_google(audio)
		except:
			AI = "I don't understand, can you say it again?"
			print("AI:" + AI)
			AI_mouth = pyttsx3.init()
			AI_mouth.say(AI)
			AI_mouth.runAndWait()
		wikipedia.set_lang("vi")
		wiki = wikipedia.summary(wiki)
		print(wiki)
		AI = wiki
		time.sleep(3)	
		break	
	elif "tell me" in you:
		with open('joke.txt', 'r') as file:
			jokelist = file.read().split("\n*")
		joke = str(random.choice(jokelist))
		AI = joke
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()	
		break
	elif "what should i do":
		AI = """
		6 am: Do exercise
		6:30 am: Have breakfast
		7:00 am: Learn math
		8 am: Learn physics 
		9 am: Clean the room
		10:00 am: Have lunch"""
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
	break

	
	