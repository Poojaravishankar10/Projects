# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 22:27:25 2016

"""
import tokenizer;
import math;
import nltk;
nltk.download('punkt')

def perplexity(probabilitylist, Numtokens):
    sum=0
    for probvalues in probabilitylist:
        sum+= math.log10(probvalues)
    pp=((sum*-1) *(1.0/Numtokens)) 
    perplexity=math.pow(10,pp)

    return  perplexity

def lookup_probability(onetuple, probability_table):
    n_gram = len(onetuple);
    if(n_gram == 1 ):
        row_index = ();
        #prob_row = probability_table[];
    else:
        row_index = onetuple[0:-1];
    col_index = onetuple[-1];
    
    if(not ( row_index in probability_table ) ):
        i = 0;    
        row_index = ();        
        while i < n_gram-1:
            row_index += ("<unk>",);
            i=i+1;        
        #row_index = ("<unk>","<unk>" );
    if( not(col_index in probability_table[row_index])):
        col_index = "<unk>";
    if (not(col_index in probability_table[row_index])) :
        col_index = "<zero>";
    #print(row_index, col_index);
    return probability_table[row_index][col_index];

'''
def calculate_perplexity(text, probability_table, ngram):
    #tuple_list = [];
    probability_values = [];
    sent_end_chars = [".","?","!"];

    text_list = nltk.word_tokenize(text);
    sent_begin_tuple = ();
    i = 0;    
    while i < ngram-1:
        sent_begin_tuple += ("<s>",);
        i=i+1;
    n_minus_one_words = sent_begin_tuple;
    number_of_lookups = 0;
    for v in text_list:
        if( n_minus_one_words[-1] in sent_end_chars):
            n_minus_one_words = sent_begin_tuple;
        current_tuple = n_minus_one_words + (v,);
        probability_value = lookup_probability(current_tuple, probability_table);
        probability_values.append(probability_value);
        number_of_lookups +=1;
    return perplexity(probability_values, number_of_lookups);
'''
def calculate_perplexity(text, probability_table, ngram):
    tuple_list = [];
    probability_values = [];
    sent_end_chars = []#".","?","!"];
    tuple_output = tokenizer.tokenize(text, ngram, sent_end_chars, 1, 1);

    
    tuple_list = tuple_output[1];
    number_of_tokens = tuple_output[0];
    
    i = 0;
    probability_value = 0;
    length = len(tuple_list);
    
    while i < length :
        probability_value = lookup_probability(tuple_list[i], probability_table);
        probability_values.append(probability_value);
        i += 1;
    return perplexity(probability_values, number_of_tokens); 
    #print(tuple_list);
        
    
