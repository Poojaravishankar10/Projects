# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 01:16:53 2016

@author: anant
"""
import file_reader;
import nltk;
import spell_checker;
nltk.download('punkt');
def measure_spell_correction(path):
    path = "/Users/anant/pythonWD/data_corrected 2/";
    path += "spell_checking_task_v2/";
    
    all_folders_to_train = ["graphics","medicine","motorcycles","religion","space","atheism","autos"];
    count=0;
    error = 0;
    confusion_set = spell_checker.get_confusion_set(path);
    for folder in all_folders_to_train:
        dev_results_path = path+folder+"/dev_results/";     
        all_dev_op_files = file_reader.list_all_text_files(dev_results_path);
        for file in all_dev_op_files:
            devop = file_reader.read_file(file);
            train_file = file.replace("dev_results", "train_docs");
            devop_file_text = file_reader.read_file(file);
            train_file_text = file_reader.read_file(train_file);
            devop_list = nltk.word_tokenize(devop_file_text);
            train_list = nltk.word_tokenize(train_file_text);
            devop_confusion_list = [];
            train_confusion_list = [];
            for w in devop_list:
                if(w in confusion_set):
                    devop_confusion_list.append(w);
            for w in train_list:
                if(w in confusion_set):
                    train_confusion_list.append(w);
            if(len(train_confusion_list)!= len(devop_confusion_list)):
                print("Number of confused words is not same in train and corrected data, this shouldn't have happen\n");
            error_in_file = 0;
            j = 0;
            while j < len(train_confusion_list):
                if(train_confusion_list[j] != devop_confusion_list[j]):
                    error_in_file += 1;
                j=j+1;
            if(len(train_confusion_list) == 0 ):
                if(len(devop_confusion_list) == 0):
                    print("No confusion words found in:", file, "\n");
            else:
                 count+=1;
                 error += error_in_file/len(train_confusion_list);        
            
        print("Mean error for the folder:", error/count, "\n"); 
