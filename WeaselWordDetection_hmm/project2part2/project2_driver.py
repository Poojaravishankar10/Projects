# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 21:46:01 2016

"""

import preprocessor_BIO
import baseline      #for first baseline
import baseline1
import kaggle_op
import file_reader
import hmm
import nltk
import checker
import cross_validation
import proj_config



#
# User should enter the directory path having 'train' folder.
#
input_path_is_correct = 0;
while (not input_path_is_correct) :
    path = input("\nInput path to train folder:")
    final_path = path + "train/"
    print("\nWill start reading at:", final_path, "\n");
    confirm = input("If that's right enter yes else no: ");
    if (confirm.lower() =="yes") :
        input_path_is_correct = 1
    baseline_number = proj_config.baseline_number;

'''              *********** CREATE OUTPUT FOLDERS ***********              '''
#
# Create output folders.
# One folder for storing preprocessed files
# Second folder for storing the baseline output of test-public
# Third folder for stroing the baseline output of test-private
#
file_reader.create_folder(path+"train_BIO")
file_reader.create_folder(path+"test-public-baseline1/")
file_reader.create_folder(path+"test-private-baseline1/")
file_reader.create_folder(path+"test-public-hmm/")
file_reader.create_folder(path+"test-private-hmm/")

'''             *********** PREPROCESS TRAIN FILES ***********              '''
#
# Preporces the train folder and replace CUE* with B or I and _ with O
#
preprocessor_BIO.preprocess_train_files(path+"train/", path+"train_BIO/")


'''            ****************   BASELINE   ***************                '''

'''
There are 2 Baselines: {1,2} set baseline_number accordingly to run them


if(baseline_number == 1):
    run_baseline = baseline;
elif(baseline_number == 2):
    run_baseline = baseline1;
else:
    print("baseline enum is {1,2}\n");

#
# After the preprocessing generate dictionary of possible weasel words
#
preprocess_dict = run_baseline.generate_weasel_dictionary(path+"train_BIO/")


run_baseline.generate_baseline_files(path+"test-public/",
                                 path+"test-public-baseline1/",
                                 preprocess_dict)

run_baseline.generate_baseline_files(path+"test-private/",
                                 path+"test-private-baseline1/",
                                 preprocess_dict)

kaggle_op.gen_kaggle_file(path+"test-public-baseline1/",
                          path+"test-private-baseline1/",
                          path)
'''

'''           *********** SETUP FLAGS FOR EXTENSION   ***********           '''

config_var = dict()

if (proj_config.em_prob_is_word_and_pos_given_tag) :
    config_var = {"w_and_pos":1}
elif (proj_config.em_prob_is_pos_given_tag) :
    config_var = {"pos_only":1}

if (proj_config.bio_balancing) :
    config_var["prune_train"] = proj_config.bio_balance_tuple


'''           ************* CROSS VALIDATION BLOCK ************             '''


cross_validation.generate_cross_validation_set(path)
hmm.gen_hmm_tag(path+"train_BIO/", path+"cv_test/", path+"cv_test/", 2, config_var )

kaggle_op.gen_kaggle_file(path+"cv_truth/",          #public test data path
                          path+"test-private-hmm/",  #private test data path
                          path,                      #kaggle output file's path
                          "test_truth",              #kaggle output file's prefix
                          1,                         #generate only public row in kaggle output file.
                          0)                         #ambiguous sentence marking threshold

kaggle_op.gen_kaggle_file(path+"cv_test/",
                          path+"test-private-hmm/",
                          path,
                          "test_gen",
                          1,
                          0)

print("Sentence: ")
checker.sentence_score(path+"_test_truth_kag_sent_op.csv",path+"_test_gen_kag_sent_op.csv" )

print("Word: ")
checker.word_score(path+"_test_truth_kag_word_op.csv",path+"_test_gen_kag_word_op.csv" )



'''*********** Code to tag Public-test-data and Private-test-data **********'''
'''
hmm.gen_hmm_tag(path+"train_BIO/", path+"test-public/", path+"test-public-hmm/", 2, config_var)
hmm.gen_hmm_tag(path+"train_BIO/", path+"test-private/", path+"test-private-hmm/", 2, config_var)
kaggle_op.gen_kaggle_file(path+"test-public-hmm/",
                          path+"test-private-hmm/",
                          path,
                          "pruned_8-11",
                          0,
                          0)
'''
