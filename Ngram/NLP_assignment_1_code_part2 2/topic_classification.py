# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 20:59:39 2016

"""

import file_reader;
import preprocessor;
import tokenizer;
import probability_calculator;
import perplexity;

input_path_is_correct = 0;
#n_gram = int( input("\n\nEnter n for n-gram: "));
n_gram = 2;

all_folders_to_train = ["atheism","autos","graphics","medicine","motorcycles","religion","space"];


#probability_table = (dict, dict, dict, dict, dict, dict, dict)
probability_table = [dict() for x in range(7)]
#path ="/Users/Pooja/Desktop/Python/python_scripts/data_corrected/";



def topic_classifier(path, ngrams):
    folder_index = 0;
    bad_prediction = 0;
    total_processed = 0;
    
    '''                   BUILD LANGUAGE MODELS FOR ALL THE FOLDERS             '''
    
    print ("\n\nBuidling chosen language model ...\n\n");

    while (folder_index < 7) :
        print("Processing folder ",all_folders_to_train[folder_index])
        #read all text files
        all_text_files = [];
        folder_path = path+"/classification task/"+all_folders_to_train[folder_index]+"/train_docs/";
        all_text_files += file_reader.list_all_text_files(folder_path);
    

        #preprocess each file
        all_preprocessed_text = "";
        for file in all_text_files:
            file_text = file_reader.read_file(file);
            all_preprocessed_text += " "+preprocessor.preprocess(file_text);    
            sent_end_chars = []#".","?","!"];

        token_dictionary = tokenizer.tokenize(all_preprocessed_text, ngrams, sent_end_chars, 1, 0 );

        probability_table[folder_index] = probability_calculator.generate_probability_table(token_dictionary, ngrams);
        folder_index += 1;

    '''                     topic classification                 '''

    all_perplexities = dict();
    count = 0;
    input_path_is_correct = 0;
    while (count < 1) :
        output = "Id,Prediction";
        #classification_path = path+"/classification task"+"/test_for_classification/";
        #classification_path = path+"/classification task/"+all_folders_to_train[count]+"/dev_test/"
        #"/Users/Deekshith/Desktop/Python/python_scripts/data_corrected/classification task/";
        while( not input_path_is_correct ):    
            print("\n Enter the folder path on which you want the topic classifier to run\n");
            classification_path = input("Enter the abosulute path (eg /Users/Deekshith/data corrected/classification task/test_for_classification/)\n\n");
            print("\nTopic classification will run on :", classification_path, "\n");             
            confirm = input("If that's right enter yes else no: ");
            if(confirm.lower() =="yes"):input_path_is_correct = 1
            
        print("\nOutput of topic classification will be written to \n",classification_path+"result.csv")
        #print(classification_path);
    
        #random_folder_index = random.randrange(0,6);
        #classification_path = classification_path+all_folders_to_train[random_folder_index]+"/train_docs/";
        all_text_files = file_reader.list_all_text_files(classification_path); 
        for file in all_text_files:
            file_text = file_reader.read_file(file);
            all_preprocessed_text = preprocessor.preprocess(file_text);
            total_processed += 1;
            #print("\n\n\nfile picked for verification is \n",file)
    

            perplexity_list = [float for x in range(7)]

            folder_index = 0;
            while folder_index < 7 :
                perplexity_list[folder_index] = perplexity.calculate_perplexity(all_preprocessed_text, 
                                                           probability_table[folder_index], ngrams);
                folder_index += 1;
    

            folder_index = 1;
            min_perplexity = perplexity_list[0];
            output_folder_index = 0;

            #print("\n Perplexity for all the folders",perplexity_list);

            while (folder_index < 7):
                if (min_perplexity > perplexity_list[folder_index]) :
                        min_perplexity = perplexity_list[folder_index]
                        output_folder_index = folder_index;
                folder_index += 1;
            if (output_folder_index != count) :
                    bad_prediction += 1;
                    
            just_file_name = file.split('/')[-1];    
            all_perplexities[just_file_name] = perplexity_list;
            output += "\n"+just_file_name+","+str(output_folder_index);
        
#            output += "\n"+file.split('/')[-1]+","+str(output_folder_index);
            #count = count + 1;
    
        new_file_path = classification_path+"result.csv";
        new_file = open(new_file_path,"w");
        new_file.write(output);
        new_file.close();     
        #print("\n total files processed\n",total_processed);
        count = count+1;
    print("\n total files processed\n",total_processed);
    
    print ("\nPerplexity of all the files in the chosen folder\n")
    print(", ".join(all_folders_to_train));
    for key in all_perplexities:
        row_op = [];    
        for v in all_perplexities[key]:
            row_op.append( str(int(v)));
        print(key+": ", ", ".join(row_op));
    
    #print("\n\n total processed ",total_processed,"bad prediction",bad_prediction)
    return 1;

    
    
