


How to run the code :
=====================

— Run project2_driver.py [We have used ‘Anaconda’ with ’Spyder’ IDE for the development (python 3.5)]
- User should enter the folder path which contains the folder ’train’. 

- Output will be stored in the folder path passed above by the user.
- Outputs for cross validation sets are displayed by default.

How to tune config parameters :
===============================

- proj_config.py has the default settings for which our model works the best.
- following parameter can be tuned.
	— baseline_number  : can be 1 or 2 - We have two baselines and based on this parameter, corresponding baseline will be run.
	- enable_smoothing : enables good turing smoothing for unseen words.
	- handle_unseen_with_pos : This is to enable unseen word handling using POS. More details on this technique are described in the report.
	- enable_unknown_word_handling : Flag to switch on unknown word handling.
	- em_prob_is_word_and_pos_given_tag : Flag to change the emission probabilities from P(WORD|tag) to P((WORD,POS)|tag)
	- em_prob_is_pos_given_tag : Flag to change the emission probabilities from P(WORD|tag) to P(POS|tag)
	- bio_balancing    : Flag to switch on resampling training data.
	- bio_balance_tuple: Tuple to control resampling  parameters describe in the report.
 	
Console Output :
================

Input path to train folder:/Users/Deekshith/Desktop/Cornell/2_NLP/assignment_2/part1/original/

Will start reading at: /Users/Deekshith/Desktop/Cornell/2_NLP/assignment_2/part1/original/train/ 

If that's right enter yes else no: yes
Total number of words in /Users/Deekshith/Desktop/Cornell/2_NLP/assignment_2/part1/original/cv_truth/  :  24987 

Total number of sentences in /Users/Deekshith/Desktop/Cornell/2_NLP/assignment_2/part1/original/cv_truth/ :  919 

Total number of words in /Users/Deekshith/Desktop/Cornell/2_NLP/assignment_2/part1/original/cv_test/  :  24987 

Total number of sentences in /Users/Deekshith/Desktop/Cornell/2_NLP/assignment_2/part1/original/cv_test/ :  919 


Sentence: 
Precision:  0.5219123505976095
Recall:  0.5646551724137931
Fscore:  0.5424430641821947

Word: 
Precision:  0.25597269624573377
Recall:  0.2516778523489933
Fscore:  0.2538071065989847

>>> 

Code Organization :
===================

We have created following modules to do required tasks in this project.

1) project2_driver.py
	Driver for the entire project. Imports other modules to do required tasks.
	Interacts with User and requests for input. Also creates directories to save the output of preprocess, cross validation, baseline, etc.

2) file_reader.py
	Folder path is passed and reads all the file names and stores them in a list.

3) preprocessor_BIO.py
	Replaces instance of CUE* in train folder to sequence of B, I and O.
	
4) baseline1.py and baseline.py
	Generates a weasel dictionary and output baseline files. We have two baseline files and at a time one of the baseline can be chosen to perform the sequence tagging task.

5) kaggle_op.py
	Generates the kaggle output based on the tagged files generated.

6) checker.py
	Calculates precision, recall and fscore for the kaggle output files generated from cross validation set.

7) cross_validation.py
	Generates cross validation set.

8) hmm.py
	Includes basic hmm and three other extensions.

9) smoothing.py
	Contains code for good turing smoothing.

10) proj_config.py
	Contains 8 config variables to enable different configurations (including the extensions) which can be tuned to perform various experiments.

