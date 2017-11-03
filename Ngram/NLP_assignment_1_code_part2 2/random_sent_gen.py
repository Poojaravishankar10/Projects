
"""
random sentence generator

"""
import random
import bisect

def find_ge( cdf_dict, x): #binary search on cumulative probability table
    cdf_keys = list(cdf_dict.keys());
    cdf_values  = list( cdf_dict.values());   
    i = bisect.bisect_left(cdf_values, x)
    if i != len(cdf_values):
        return cdf_keys[i]
    else: 
        return cdf_keys[i-1]

def sentence_gen(cdf, n_gram, sent_end_chars, seed_sent):
    sentence = [];   
    n_minus_one_words = ();    
    starting_chars_to_add = n_gram-1;
    
    #if doing sentence completion:
    if(seed_sent != ""):
       sentence = seed_sent.split();             
       len_seed_sent = len( sentence)
       if(len_seed_sent >= n_gram-1):
           n_minus_one_words = tuple( sentence[len_seed_sent-n_gram+1:])
           starting_chars_to_add = 0;
       else:
           n_minus_one_words = tuple( sentence )
           starting_chars_to_add = n_gram - 1 - len(sentence);
           
       if( not n_minus_one_words in cdf ):
           #print("Last n-1 words of seed sentence aren't present in corpus together \n");
           print("\n\nLanguage model built from the corpus is not able to complete the sentence")
           print(" as subsequence of last ",n_gram-1," words is not present in the corpus\n\n")
           return seed_sent;
           
    i =1;
    while(i<=starting_chars_to_add):
        n_minus_one_words = ("<s>",) + n_minus_one_words;
        i+=1;
    
    sen_length = len(sentence);
    while( not sen_length or not (sentence[sen_length-1] in sent_end_chars) ):         
        random_sample = random.random();
        relevant_dict = cdf[ n_minus_one_words ];
        nth_word = find_ge(relevant_dict, random_sample);
        if(n_gram!=1):
            n_minus_one_words = n_minus_one_words[1:] + (nth_word,);
        if (nth_word != '<unk>'):
            sentence.append( nth_word );
            sen_length +=1;
        #print(nth_word)
    sentence[0] = sentence[0].capitalize();   
    return(" ".join(sentence));

    