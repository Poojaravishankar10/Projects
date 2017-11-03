#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 20:36:40 2016

"""
#
# Answer ranking function is a linear combination of match count (number of
# words matching between question and sentence that might be having the asnwer)
# and doc score. Set this to 0 to disable.
#
doc_score_weight = 0.5

# how many documents should be processed for every question.
max_rank_check = 100

# Should token match happen after lower casing both question text and answer text.
lowercase_mode_on = 1

# How many sentences at once we want to consider while finding answer.
context_span = 1

# How many answers should be picked from heap maintaining weighted score.
weighted_answer_count = 2

############################## Debugging/Testing ##############################

debug_mode = 0

# While testing, how many questions we want to process. Setting this to 0 will
# process all the questions even in debug mode
question_boundary = 1