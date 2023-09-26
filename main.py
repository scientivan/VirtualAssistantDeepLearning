import detect
import torch

print(torch.cuda.is_available())
# detect.run(source=0,imgsz=(128,128),device=1)
# from unittest import result
# import nltk

# stemmer = nltk.stem.lancaster.LancasterStemmer()

# import numpy as np
# import tflearn
# import random
# import json
# import pyttsx3

# with open("intents.json") as file:
#     data = json.load(file)

# words = []
# labels = []
# docs_x = []
# docs_y = []

# for intent in data["intents"]:
#     for pattern in intent["patterns"]:
#         wrds = nltk.word_tokenize(pattern)
#         words.extend(wrds)
#         docs_x.append(wrds)
#         docs_y.append(intent["tag"])

#     if intent["tag"] not in labels:
#         labels.append(intent["tag"])
# words = [stemmer.stem(w.lower()) for w in words if w != "?"]
# words = sorted(list(set(words)))
# labels = sorted(labels)

# training = []
# output = []

# out_empty = [0 for _ in range(len(labels))]
# #docs_x [['Hi'], ['How', 'are', 'you'], ['Is', 'anyone', 'there', '?'],
# #doc    ['Hi']
# #       ['How', 'are', 'you']
# #       ['Is', 'anyone', 'there', '?']
# #       ['Hello']
# #wrds   ['hi']   doc yang sudah di ambil inti kata per kata
# #       ['how', 'ar', 'you']
# #       ['is', 'anyon', 'ther', '?']
# #words  ['buy', 'cal', 'could']
# for x, doc in enumerate(docs_x):
#     temporary_bag = []

#     wrds = [stemmer.stem(w.lower()) for w in doc]
#     print(wrds)
#     for w in words:
#         if w in wrds:
#             temporary_bag.append(1)
#         else:
#             temporary_bag.append(0)
#     output_row = out_empty[:]
#     output_row[labels.index(docs_y[x])] = 1

#     training.append(temporary_bag)
#     output.append(output_row)

# training = np.array(training)
# output = np.array(output)
# print(len(training[0])) # 46
# print(len(output[0])) # 6

# net = tflearn.input_data(shape=[None,len(training[0])])
# net = tflearn.fully_connected(net,8)
# net = tflearn.fully_connected(net,8)
# net = tflearn.fully_connected(net,len(output[0]),activation='softmax')

# net = tflearn.regression(net)
# model = tflearn.DNN(net)
# # model.fit(training,output,n_epoch=500,batch_size=8,show_metric=True)
# # model.save('model.tflearn')

# try:
#     model.load('model.tflearn')
# except:
#     pass

# def bag_of_words(s, words):
#     bag = [0 for _ in range(len(words))]

#     s_words = nltk.word_tokenize(s)
#     s_words = [stemmer.stem(word.lower()) for word in s_words]

#     for se in s_words:
#         for i, w in enumerate(words):
#             if w == se:
#                 bag[i] = 1
            
#     return np.array(bag)

# intents = data['intents']
# data_ = [intents[i] for i in range(len(intents))]

# import speech_recognition as sr
# r = sr.Recognizer()

# def takeCommand():

# 	r = sr.Recognizer()

# 	with sr.Microphone() as source:
# 		print('Listening')
		
# 		r.pause_threshold = 0.7
# 		audio = r.listen(source)
		
# 		try:
# 			print("Recognizing")
			
# 			Query = r.recognize_google(audio, language='en-in')
# 			print("the command is printed=", Query)
			
# 		except Exception as e:
# 			print(e)
# 			return "None"
		
# 		return Query

# def BotSpeak(audio):
	
    	
# 	engine = pyttsx3.init()
# 	# getter method(gets the current value
# 	# of engine property)
# 	voices = engine.getProperty('voices')
	
# 	# setter method .[0]=male voice and
# 	# [1]=female voice in set Property.
# 	engine.setProperty('voice', voices[0].id)
# 	engine.setProperty('rate',170)
# 	# # Method for the speaking of the the assistant
# 	engine.say(audio)
	
# 	# Blocks while processing all the currently
# 	# queued commands
# 	engine.runAndWait()

# import pywhatkit
# import datetime

# def PlayMusic(song):
#     pywhatkit.playonyt(song)
#     BotSpeak('Playing' + song)

# def TellTime():
#     time = str(datetime.datetime.now())
#     print(time) #2021-08-06 15:45:35.522024
#     hour = time[11:13]
#     min = time[14:16]
#     sec = time[17:19]
#     BotSpeak("It's " + hour + "Hours" + min + "Minutes and" + sec + 'Seconds')	
    
# def SearchOnGoogle(searchInput_):
#     if 'search' in searchInput_:
#         searchInput_ = searchInput_.replace('search','')
#     if 'for' in searchInput_:
#         searchInput_ = searchInput_.replace('for','')
#     if 'browse' in searchInput_:
#         search = searchInput_.replace('browse','')
#     search = search.lower()
#     BotSpeak('Searching for ' +search)
#     pywhatkit.search(search)

# def TellDay():
# 	day = datetime.datetime.today().weekday() + 1
	
# 	Day_dict = {1: 'Monday', 2: 'Tuesday',
# 				3: 'Wednesday', 4: 'Thursday',
# 				5: 'Friday', 6: 'Saturday',
# 				7: 'Sunday'}
	
# 	if day in Day_dict.keys():
# 		day_of_the_week = Day_dict[day]
# 		return day_of_the_week
    
# def SchoolSchedule():
#     day = TellDay()
#     if day.lower() != 'sunday' and day.lower() != 'saturday':
#         time = str(datetime.datetime.now())
#         #print(time) #2021-08-06 15:45:35.522024
#         hour = int(time[11:13])
#         min = int(time[14:16])
#         time = (hour * 60) + min
#         if day.lower() == 'monday':
#             if time > 435 and time < 480:
#                 return 'Compulsory English Lesson'
#             elif time > 525 and time < 630:
#                 return 'Religion Lesson'
#             elif time > 630 and time < 720:
#                 return 'Specialization English Lesson'
#             elif time > 750 and time < 840:
#                 return 'Specialization Mathematic Lesson'
#         elif day.lower() == 'tuesday':
#             if time > 435 and time < 480:
#                 return 'Civil lesson'
#             elif time > 525 and time < 630:
#                 return 'Chemistry lesson'
#             elif time > 630 and time < 720:
#                 return 'Indonesia lesson'
#         elif day.lower() == 'wednesday':
#             if time > 435 and time < 480:
#                 return 'Compulsory Mathematic lesson'
#             elif time > 525 and time < 630:
#                 return 'Art and culture lesson'
#             elif time > 630 and time < 720:
#                 return 'Crafts lesson'
#         elif day.lower() == 'thursday':
#             if time > 435 and time < 480:
#                 return 'Javanese lesson'
#             elif time > 525 and time < 630:
#                 return 'Sport lesson'
#             elif time > 630 and time < 720:
#                 return 'Physics lesson'
#         elif day.lower() == 'friday':
#             if time > 435 and time < 480:
#                 return 'Japanese lesson'
#             elif time > 525 and time < 630:
#                 return 'Biology lesson'
#             elif time > 630 and time < 720:
#                 return 'Indonesian Historic lesson'

# import pyjokes

# def TakeInput():
#     inp = takeCommand().lower()
#     return inp 

# def GiveOutput(input_):
#     results = model.predict([bag_of_words(input_, words)]) # prediksi model tentang perkataan user
#     print(results)
#     result_index_ = np.argmax(results)  # ngambil value di array yang memiliki nilai rate paling tinggi
#     print('CATEGORY: ', labels[result_index_]) # permintaan user itu masuk kategori apa di intents.json
#     return result_index_

# def GiveResponses(result_index__,input_):
#     for i in range(len(data_)):
#         if labels[result_index__] == data_[i]['tag']:
#             choice = ''
#             if data_[5] == data_[i]: # Time condition
#                 TellTime()
#             elif data_[6] == data_[i]:
#                 command = str.replace(input_.lower(),'play','')
#                 PlayMusic(command)
#             elif data_[7] == data_[i]: 
#                 BotSpeak(pyjokes.get_joke())
#             elif data_[8] == data_[i]: 
#                 SearchOnGoogle(input_.lower())
#             elif data_[11] == data_[i]:
#                 BotSpeak('It is time for' + SchoolSchedule())
#             else:
#                 choice = random.choice(data_[i]['responses'])
#                 print(data_[i]['responses'])
#                 #choice = data_[i]['responses'][random.randint(0,len(data_[i]['responses'] ) - 1)]
#                 BotSpeak(choice)

# def UserSpeak(): # function utamanya
#     condition = False
#     while True:
#         inp = TakeInput() # akan nunggu user input dulu baru lanjut eksekusi code kebawah
#         if 'turn on' in inp.lower(): # masih error
#             condition = True
#         if condition == True:
#             if 'turn off' in inp.lower():
#                 condition = False          
#             result_index = GiveOutput(inp) # me return hasil index dari rate paling tinggi
#             print( result_index)
            
#             if labels[result_index] == data_[1]['tag']: # goodbye condition programnya off 
#                 BotSpeak(data_[1]['responses'][random.randint(0,len(data_[1]['responses'] ) - 1)])
#                 print(data_[1]['responses'][random.randint(0,len(data_[1]['responses'] ) - 1)])
#                 break
            
#             GiveResponses(result_index,inp)
# UserSpeak()