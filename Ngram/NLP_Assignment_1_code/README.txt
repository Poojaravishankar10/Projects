


How to run the code :
=====================

— Run assignment1_driver.py [We have used ‘Anaconda’ with ’Spyder’ IDE for the development]
- User should enter the folder path which contains the folder ’data_corrected’
- After cross checking with the user, program will request for the folder name (eg: atheism, autos)
- After generating the probability table, user can either create a random sentence or complete a given sentence.

Console Output :
================

[nltk_data] Downloading package punkt to /Users/Pooja/nltk_data...
[nltk_data]   Package punkt is already up-to-date!


Input path to data_corrected folder: /Users/Pooja/Desktop/Python/python_scripts/

will start reading at: /Users/Pooja/Desktop/Python/python_scripts/data_corrected 

If that's right enter yes else no: yes


Enter folder name to train
enter all to train on everything: atheism


Enter n for n-gram: 2


Enter the random sentence that needs to be completed or Press enter to generate a random sentence



You could watch for military target and participate in the separation of days and i still contradictory statements that they come from healta tammy pass the statement a cage which were injured the day , the argument .
>>> 

Code Organization :
===================

We have created following modules to do required tasks in this project.

1) assignment1_driver.py
	Driver for the entire project. Imports other modules to do required tasks.
	Interacts with User and requests for input.

2) file_reader.py
	Based on the user input, reads all the files in the directory mentioned by the user and generates one single sentence.
 	
3) preprocessor.py
	Preprocess the the generated sentence by removing special characters. More on this is mentioned in design section.
 
4) tokenizer.py
	Builds the tokens for each of the unique words and generates a dictionary with couple having n elements (n is the ngram here) and number of times each tuple has repeated. For example, in case of unigram, this will build a dictionary with couple having one element as the key and number of times that one word repeated as the value.

5) probability_calculator.py
	Builds a probability table using the dictionary generated in the previous module.

6) random_sent_gen.py
	Generates random sentences. Users will be choosing to either create a new sentence or to complete a random sentence they input.

