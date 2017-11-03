# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 20:04:21 2016

@author: anant

spell checker module

If you want to generate dev results - please add a folder called dev results.
"""
import file_reader;
import nltk;
import preprocessor;
import tokenizer;
import probability_calculator;

nltk.download('punkt');

def get_confusion_set( path ):
  
    confusion_set = dict();
    fname = path+"confusion_set.txt";
    confusion_set = dict();
    confusion_list = file_reader.read_lines_as_list(fname);
#    with open(fname) as f:
#        confusion_list = f.readlines();     
    
    list_size = len(confusion_list);
    i = 0;    
    confusion_list[0] = confusion_list[0].replace('\ufeff', '');
    while i < list_size:       
        one_line = nltk.word_tokenize(confusion_list[i]);
        #if (len(one_line) == 3 ):
        #    one_line[1]+=" "+one_line[2]; #handle maybe may be
        #elif (len(one_line) > 2 ):
        #    print("Confusion Dictionary construction problem with: ", one_line);
        
        confusion_set[ one_line[0] ] = one_line[1];
        confusion_set[ one_line[1] ] = one_line[0];
        i=i+1;
    return( confusion_set );   


def generate_fixed_files( all_folders_to_train, confusion_set, probability_table, path, dev_set = 1 ):
    folder_index = 0;
    while( folder_index < len(all_folders_to_train) ):
        folder = all_folders_to_train[folder_index];
        probability_model = probability_table[folder_index];
        print("\n Processing folder ",folder);
        if(dev_set):
            bad_files_path = path+folder+"/train_modified_docs/";                
            fixed_files_path = path+folder+"/dev_results/";
        else:
            bad_files_path = path+folder+"/test_modified_docs/";
            fixed_files_path = path+folder+"/test_docs/";

        #folder_path = path+all_folders_to_train[folder_index]+"/train_docs/";
        
        all_text_files = [];    
        all_text_files += file_reader.list_all_text_files(bad_files_path);#folder_path);
        #count = 0;
        for file in all_text_files:
            file_text = file_reader.read_file(file);
            file_text_list = nltk.word_tokenize(file_text);
            i = 0;
            prev_word = ("<s>",);
            file_list_len = len(file_text_list);
            while i < file_list_len:
                current_word = file_text_list[i];
                if(prev_word in ['.','!',"?"]):
                    prev_word = ("<s>",);
            
                if( current_word in confusion_set ):            
                    #print("testing for ", current_word, "\n");
                    current_word1 = confusion_set[current_word];
                    if(not(prev_word in probability_model)):
                    #    print("didn't find prev_word ", prev_word, " replacing it with <unk>\n");
                        prev_word = ("<unk>",);  
                     #   prev_word = file_text_list[i]; 
                     #   i=i+1;
                     #   continue;
                    probability_row = probability_model[prev_word]; 
                    prob = 0;
                    prob1 = 0;
                    if( not(current_word in probability_row) ):
                        if(current_word1 in probability_row ):
                            prob1 = probability_row[current_word1]
                        else:
                            prob1 = 0;
                            prob = 1;
    #                    print("didn't find current_word ", current_word, " replacing it with <unk>\n");
                    else:
                        prob = probability_row[current_word];
                        if(current_word1 in probability_row ):
                            prob1 = probability_row[current_word1]
                        else:
                            prob1 = 0;
                        
    #                    current_word = "<unk>";
    #                if( not(current_word1 in probability_row) ):
     #                   print("didn't find conf_word ", current_word1, " replacing it with <unk>\n");
     #                   current_word1 = "<unk>";
                        
    #                prob1 = probability_row[ current_word];
    #                prob2 = probability_row[current_word1];
                    if(prob<prob1):
                        new_word = confusion_set[file_text_list[i]];
                        if(file_text_list[i].isupper()):
                            new_word = new_word.capitalize();                        
                       # print("Replaced ", file_text_list[i], " with ", new_word, "\n");
                        file_text_list[i] = new_word;
                prev_word = (file_text_list[i],);
                i=i+1;                            
            corrected_file_text = " ".join(file_text_list);
            ##create a a file and write
            corrected_file_name = file.split('/')[-1].replace("_modified", "");
            print(fixed_files_path+corrected_file_name);
            wfile = open(fixed_files_path+corrected_file_name, "w+");
            wfile.write(corrected_file_text);
            wfile.close();
            #count +=1;
            #if(count>10): break;
        folder_index +=1;
        
#def spell_train( path ):
def do_spell_correction( path, dev_set = 1 ):
        
    n_gram =2;
    
    path += "spell_checking_task_v2/";
    
    print("***Running spell correction at: ", path, " \n ***");
    confusion_set = get_confusion_set( path );
    all_folders_to_train = ["graphics","medicine","motorcycles","religion","space","atheism","autos"];
    
    
    '''                   BUILD LANGUAGE MODELS FOR ALL THE FOLDERS             '''
    
    folder_index = 0;
    
    probability_table = [dict() for x in range(7)]
    
    while (folder_index < len(all_folders_to_train)) :
        print("\n Processing folder ",all_folders_to_train[folder_index])
        #read all text files
        all_text_files = [];
        folder_path = path+all_folders_to_train[folder_index]+"/train_docs/";
        all_text_files += file_reader.list_all_text_files(folder_path);
        
    
        #preprocess each file
        all_preprocessed_text = "";
        for file in all_text_files:
            file_text = file_reader.read_file(file);
            all_preprocessed_text += " "+preprocessor.preprocess(file_text);    
            sent_end_chars = [".", "!", "?"];
    
        token_dictionary = tokenizer.tokenize(all_preprocessed_text, n_gram, sent_end_chars, 1 );
    
    
        probability_table[folder_index] = probability_calculator.generate_probability_table(token_dictionary, n_gram);
        folder_index += 1;
    print("\n Done processing all the folders\n")
    print("\n Done processing all the folders\n")
    generate_fixed_files(all_folders_to_train, confusion_set, probability_table,path, dev_set );    