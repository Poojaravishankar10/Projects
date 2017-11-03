


How to run the code :
=====================

— Run assignment1_driver.py [We have used ‘Anaconda’ with ’Spyder’ IDE for the development]
- User should enter the folder path which contains the folder ’data_corrected’
- After entering the path 3 options will be given to the user. Based on the selection, corresponding task will be executed. (more on this in console output)

Console Output :
================

First instance:
---------------

Input path to data corrected folder: /Users/Deekshith/Desktop/Python/python_scripts/

will start reading at: /Users/Deekshith/Desktop/Python/python_scripts/data corrected 


If that's right enter yes else no: yes


 Choose one of these options


1 for Random sentence generation/completion
2 for Topic Classification (Includes Good Turing and Perplexity)
3 Spelling Correction


Enter your choice	3


Enter n for n-gram: 2



spell check is being performed at: /Users/Deekshith/Desktop/Python/python_scripts/data corrected/ 
 if that is not right please rerun

***Running spell correction at:  /Users/Deekshith/Desktop/Python/python_scripts/data corrected/spell_checking_task_v2/  
 ***

Second instance:
—--------------
Input path to data corrected folder: /Users/Deekshith/Desktop/Python/python_scripts/

will start reading at: /Users/Deekshith/Desktop/Python/python_scripts/data corrected 


If that's right enter yes else no: yes


 Choose one of these options


1 for Random sentence generation/completion
2 for Topic Classification (Includes Good Turing and Perplexity)
3 Spelling Correction


Enter your choice	2



Enter n for n-gram: 2


Buidling chosen language model ...


Processing folder  atheism
Processing folder  autos
Processing folder  graphics
Processing folder  medicine
Processing folder  motorcycles
Processing folder  religion
Processing folder  space

 Enter the folder path on which you want the topic classifier to run


Enter the abosulute path (eg /Users/Deekshith/data corrected/classification task/test_for_classification/)

/Users/Deekshith/Desktop/Python/python_scripts/data corrected/classification task/test_for_classification/

Topic classification will run on : /Users/Deekshith/Desktop/Python/python_scripts/data corrected/classification task/test_for_classification/ 


If that's right enter yes else no: yes

Output of topic classification will be written to 
 /Users/Deekshith/Desktop/Python/python_scripts/data corrected/classification task/test_for_classification/result.csv

 total files processed
 250

Perplexity of all the files in the chosen folder

atheism, autos, graphics, medicine, motorcycles, religion, space
file_37.txt:  58, 38, 37, 45, 41, 78, 33
file_76.txt:  39, 27, 27, 28, 25, 44, 32
file_26.txt:  64, 55, 55, 55, 49, 66, 53
...
...


third instance:
----------------

Input path to data corrected folder: /Users/Deekshith/Desktop/Python/python_scripts/

will start reading at: /Users/Deekshith/Desktop/Python/python_scripts/data corrected 


If that's right enter yes else no: yes


 Choose one of these options


1 for Random sentence generation/completion
2 for Topic Classification (Includes Good Turing and Perplexity)
3 Spelling Correction


Enter your choice	1



Enter n for n-gram: 3



Enter folder name to train
enter all to train on everything: autos



Enter the random sentence that needs to be completed or Press enter to generate a random sentence

the

 The fuel vehicles again .


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

7) topic_classification.py
	Builds the chosen language model for all the folders. Request user for the folder path on which topic classification should be performed. Write the output to path chosen.

8) perplexity.py
	File which has the code to calculate perplexity.

9) measure_spell_checker.py
	Measures the performance of spell checker on the dev set

10) spell_checker.py
	Performs spell checking and generates corrected files.


