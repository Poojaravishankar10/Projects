"""
NLP Assignment 1 - driver program
"""

import file_reader;
import preprocessor;
import tokenizer;
import probability_calculator;
import random_sent_gen;

input_path_is_correct = 0;

while( not input_path_is_correct ):
    path = input("\n\nInput path to data_corrected folder: "); #"/Users/anant/Downloads/"
    path += "data_corrected";
    print("\nwill start reading at:", path, "\n");    
    confirm = input("If that's right enter yes else no: "); #"yes"
    if(confirm.lower() =="yes"):input_path_is_correct = 1
    

folders_to_train = ["graphics","medicine","motorcycles","religion","space","atheism","autos"];
folder = input("\n\nEnter folder name to train\nenter all to train on everything: ");
if(folder.lower() != "all"):
    if(not folder in folders_to_train): 
        print("unknown folder:/");
        exit(0);
    else:
        folders_to_train = [folder];
    
n_gram = int( input("\n\nEnter n for n-gram: "));


#read all text files
all_text_files = [];
for folder in folders_to_train:
    folder_path = path+"/classification task/"+folder+"/train_docs/";
    all_text_files += file_reader.list_all_text_files(folder_path);
    

#preprocess each file
all_preprocessed_text = "";
for file in all_text_files:
    file_text = file_reader.read_file(file);
    all_preprocessed_text += " "+preprocessor.preprocess(file_text);
    
sent_end_chars = [".","?","!"];

#Tokenize the corpus
#last argument in the function call below is for lowercasing 
token_dictionary = tokenizer.tokenize( all_preprocessed_text, n_gram, sent_end_chars, 1 );

#get cdf
cum_probability = probability_calculator.generate_cdf(token_dictionary, n_gram);

#
# Printing Cumulative probability table.
# Uncomment this block to print the Cumulative probability table.
#

'''
print("\n\n Cumulative probability table \n\n")

for key in cum_probability:
    print(key,":\n",cum_probability[key], "\n");

print("\n\n NOTE : These values are not probability values but the cumulative probability values\n\n")
'''

#print ("Enter the random sentence that needs to be completed")
seed_sent = input("\n\nEnter the random sentence that needs to be completed or Press enter to generate a random sentence\n\n")

sentence = random_sent_gen.sentence_gen(cum_probability,n_gram,sent_end_chars,seed_sent);

#If you want to generate seeded sentence then use the below fn call, last arg is the seed sentence.
#sentence = random_sent_gen.sentence_gen(cum_probability,n_gram,sent_end_chars, "abcd the");

print("\n",sentence); 
