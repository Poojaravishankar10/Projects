"""
Probabilty module
"""

def generate_cdf(token_dictionary, n_gram):
   
    count_tables = generate_count_tables(token_dictionary, n_gram)    
    n_minus_one_count = count_tables[0];
    ngram_count_table = count_tables[1];

    for key in ngram_count_table:
        row = ngram_count_table[key];
        oldkey = "";
        for nth_word in row:
            ngram_count_table[key][nth_word] /= n_minus_one_count[key];
            if( oldkey != ""):   
                ngram_count_table[key][nth_word]+= ngram_count_table[key][oldkey];
            oldkey = nth_word;
    return(ngram_count_table);        
    
def generate_count_tables(token_dictionary, n_gram):
    n_minus_one_count = dict();
    ngram_count_table = dict();
            
    for key in token_dictionary:
        n_minus_one_words = key[0:n_gram-1];
        nth_word = key[n_gram-1];
    
        if( n_minus_one_words in n_minus_one_count ):
            n_minus_one_count[n_minus_one_words] += token_dictionary[key]          
        else:
            n_minus_one_count[n_minus_one_words] = token_dictionary[key]
        
        if( n_minus_one_words in ngram_count_table ):    
            ngram_count_table[n_minus_one_words][nth_word] = token_dictionary[key];
        else:
            ngram_count_table[n_minus_one_words] = dict();
            ngram_count_table[n_minus_one_words][nth_word] = token_dictionary[key];
    return (n_minus_one_count, ngram_count_table);
       


