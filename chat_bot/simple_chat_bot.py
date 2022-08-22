import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy
import tflearn
import tensorflow
import random
import json
import pickle

stemmer = LancasterStemmer()

# Phase 1: Making list to save data and accessing data from json file
with open("intents.json") as file:
	data = json.load(file)

try:
	with open("data.pickle", "rb") as f:
		words, labels, training, output = pickle.load(f)
except:
	# Phase 2: Will give data to fit in bag of words bag
	words = []
	labels = []
	docs_x = []
	docs_y = []

	for intent in data["intents"]:
		for pattern in intent["patterns"]:
			wrds = nltk.word_tokenize(pattern)
			words.extend(wrds)
			docs_x.append(wrds)
			docs_y.append(intent["tag"])

		if intent["tag"] not in labels:
			labels.append(intent["tag"])

	words = [stemmer.stem(w.lower()) for w in words if w != "?"]
	words = sorted(list(set(words)))

	labels = sorted(labels)

	training = []
	output = []

	out_empty = [0 for _ in range(len(labels))]

	for x, doc in enumerate(docs_x):
		bag = []

		wrds = [stemmer.stem(w.lower()) for w in doc]

		for w in words:
			if w in wrds:
				bag.append(1)
			else:
				bag.append(0)

		output_row = out_empty[:]
		output_row[labels.index(docs_y[x])] = 1

		training.append(bag)
		output.append(output_row)

	training = numpy.array(training)
	output = numpy.array(output)

	with open("data.pickle", "wb") as f:
		pickle.dump((words, labels, training, output), f)

# Phase 3: Complete AI and neural network for chatbot
# tensorflow.reset_default_graph()
tensorflow.compat.v1.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

# Phase 4: Saving model for reuse
try:
	model.load("model.tflearn")
except:
	model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
	model.save("model.tflearn")


# Phase 5: Utility function
def bag_of_words(s, words):
	"""
	will generate bag of words (binary[1, 0])
	:param s:
	:param words:
	:return:
	"""

	bag = [0 for _ in range(len(words))]
	s_words = nltk.word_tokenize(s)
	s_words = [stemmer.stem(word.lower()) for word in s_words]

	for se in s_words:
		for i, w in enumerate(words):
			if w == se:  # Current words we looking is equal to word in out input sentance
				bag[i] = 1

	return numpy.array(bag)


def chat():
	"""
	for conversation
	:return:
	"""
	print("Bot ready to talk (Type 'quit' to stop): ")
	while True:
		user_inp = input("You: ")
		if user_inp.lower() == "quit":
			break

		# To bring bag of words with the nearest prediction
		results = model.predict([bag_of_words(user_inp, words)])
		# print(results) # print probabylity
		result_idx = numpy.argmax(results)
		tag = labels[result_idx]

		for tg in data["intents"]:
			if tg['tag'] == tag:
				responses = tg['responses']

		print(random.choice(responses))

		
chat()
