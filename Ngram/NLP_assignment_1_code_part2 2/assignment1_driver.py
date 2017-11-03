"""
NLP Assignment 1 - driver program
data_corrected"""

import file_reader;
import preprocessor;
import tokenizer;
import probability_calculator;
import random_sent_gen;
import topic_classification;
import spell_checker;
import measure_spell_checker;
   
input_path_is_correct = 0;
sent_end_chars = [".","?","!"];

while( not input_path_is_correct ):
    entered_path = input("\n\nInput path to data corrected folder: "); #"/Users/anant/Downloads/"
    
    path = entered_path+"data corrected";
    print("\nwill start reading at:", path, "\n");    
    confirm = input("If that's right enter yes else no: "); #"yes"
    if(confirm.lower() =="yes"):input_path_is_correct = 1

#path ="/Users/Pooja/Desktop/Python/python_scripts/data_corrected";


folders_to_train = ["graphics","medicine","motorcycles","religion","space","atheism","autos"];
all_folders = ["graphics","medicine","motorcycles","religion","space","atheism","autos"];

print("\n\n Choose one of these options\n\n")
print ("1 for Random sentence generation/completion\n2 for Topic Classification (Includes Good Turing and Perplexity)")
print ("3 Spelling Correction\n")

choice = int(input("Enter your choice\t"));
n_gram = int( input("\n\nEnter n for n-gram: "));

if (choice == 1) :
    folder = input("\n\nEnter folder name to train\nenter all to train on everything: ");
    if(folder.lower() != "all"):
        if(not folder in folders_to_train): 
            print("unknown folder:/");
            exit(0);
        else:
            folders_to_train = [folder];
            
    '''
    #folder = input("\n\nEnter folder name to train\nenter all to train on everything: ");
    if(folder.lower() != "all"):
    if(not folder in folders_to_train): 
        print("unknown folder:/");
        exit(0);
    else:
        folders_to_train = [folder];
    '''    
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

    #all_preprocessed_text = "the students liked the assignment"
    
    #sent_end_chars = [".","?","!"];

    #Tokenize the corpus
    #last argument in the function call below is for lowercasing 
    token_dictionary = tokenizer.tokenize(all_preprocessed_text, n_gram, sent_end_chars, 1, 0 );

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
elif (choice == 2) :
    #confirm = input("Do you want to move ahead to to topic classification: "); #"yes"
    #if(confirm.lower() =="yes"):
    completed_topic_classification = topic_classification.topic_classifier(path, n_gram)

    #print(completed_topic_classification);
else:
    #print ("\nIt was chose to do spell check\n")
    #path = input("\n\nInput path to data corrected folder: "); #"/Users/Pooja/Downloads/"
    #path = "/Users/Pooja/pythonWD/data_corrected 2/";
    path = path+"/";
    print("spell check is being performed at:", path,"\n if that is not right please rerun\n" );
    spell_checker.do_spell_correction(path, 0) #Last arguement is to run on dev set
    '''
    #for generating the measure of spell correction on dev data:
    #for this to work dev results should have been generated using do_spell_correction(path, 1) above.
    # You will have to add a 
    measure_spell_checker.measure_spell_correction(path)
    '''

