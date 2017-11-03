# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 17:37:09 2016


"""

baseline_number = 1

enable_smoothing = 0
handle_unseen_with_pos = 0
enable_unknown_word_handling = 1

em_prob_is_word_and_pos_given_tag = 1
em_prob_is_pos_given_tag = 0
bio_balancing = 1
bio_balance_tuple = (8,-1,1)

'''                 CONSTRAINTS                '''
assert (em_prob_is_word_and_pos_given_tag != 1 or
        em_prob_is_pos_given_tag != 1)

if enable_smoothing == 1:
    handle_unseen_with_pos = 0
