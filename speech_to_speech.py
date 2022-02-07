
import speech_recognition as sr
from google_trans_new import google_translator
from gtts import gTTS
from playsound import playsound
import os

record = sr.Recognizer()
translator = google_translator()

audio_file = "translated_voice.mp3"

while True:
	with  sr.Microphone() as source:
		print("\nSay something..")
		print("Say 'STOP PROGRAM' to stop the program..\n\n")
		audio = record.listen(source)
		try:
			speech_text = record.recognize_google(audio)
			print(speech_text)
			
			if (speech_text == "stop program"):
				break
		except sr.UnknownValueError:
			print("I don't get what you said!")
			
		except sr.RequestError:
			print("Unable to fecth your request from google!")
		
		translated_text = translator.translate(speech_text, lang_tgt='ig')
		print(translated_text)

		voice = gTTS(translated_text)
		voice.save(audio_file)
		playsound(audio_file)
		os.remove(audio_file)















# 		import tkinter as tk

# import speech_recognition as sr
# from google_trans_new import google_translator
# from gtts import gTTS
# from playsound import playsound
# import os
# import  sys


# window = tk.Tk()
# window.title("Speech to Speech")
# window.geometry("400x400")



# record = sr.Recognizer()
# translator = google_translator()

# audio_file = "translated_voice.mp3"


# def start():
# 	global is_start
# 	print(is_start)
# 	if is_start == False:
# 		record_btn.config(image=stop_btn)
# 		is_start = True

# 		with  sr.Microphone() as source:
# 			print("\nSay something..")
# 			print("Say 'STOP PROGRAM' to stop the program..\n\n")
# 			audio = record.listen(source)

# 			try:
# 				speech_text = record.recognize_google(audio)
# 				print(speech_text)
# 			except sr.UnknownValueError:
# 				print("I don't get what you said!")
				
# 			except sr.RequestError:
# 				print("Unable to fecth your request from google!")

# 			translated_text = translator.translate(speech_text, lang_tgt='ig')
# 			print(translated_text)

# 			voice = gTTS(translated_text)
# 			voice.save(audio_file)
# 			playsound(audio_file)
# 			os.remove(audio_file)
				

# 	else:
# 		record_btn.config(image=start_btn)
# 		is_start = False
# 		sys.exit()


# 	# if is_start == False:
# 	# 	record_btn.config(image=stop_btn)
# 	# 	is_start = True

# start_btn = tk.PhotoImage(file="start.png")
# stop_btn = tk.PhotoImage(file="stop.png")
# star_label = tk.Label(image=start_btn)


# is_start = False
# record_btn = tk.Button(window, text="Start", image=start_btn, command=start)
# record_btn.pack()


# # en_labl = tk.














# # 	while True:
		
			
# # 				if (speech_text == "stop program"):
# # 					break
			
			
			


# window.mainloop()

