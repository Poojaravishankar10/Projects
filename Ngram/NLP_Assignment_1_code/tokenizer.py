import nltk;
nltk.download('punkt')


#
# tokens      : All the tokens after processing the text.
# token_index : Indexing into the list container all the tokens.
# touple_list : list of touples. Length of each touple will be equal to ngrams.
# temp_tuple_list : buils a temporary list which becomes one touple.
#
def tokenize( text, ngrams, sent_end_chars, lower_case = 0):
    
    tokens = nltk.word_tokenize(text);
    touple_list = []
    token_index = 0
        
    #
    # Finding lenght of tokens in every iteration is not efficient.
    # We should find the length of tokens once before the while loop
    # and update it accordingly based on number of <s> tokens we add.
    #
    #print("\n\n Begin preprocessing....\n\n")
    
    while (token_index < (len(tokens))) :
        if (tokens[token_index] in sent_end_chars and
            token_index < (len(tokens) - 1) and
            not tokens[token_index + 1] in sent_end_chars): 
            #
            # Insert n-1 '<s>' in case of ngrams
            #
            i = 1
            while (i < ngrams):
                tokens.insert(token_index + i, '<s>')
                i += 1
            if( i != 1):
                token_index += i - 1;
        elif( ".co" in tokens[token_index] or 
              "@" in tokens[token_index] or
              ".ed" in tokens[token_index] or 
              tokens[token_index] in ["Subject", "Re"]):
            del tokens[token_index]
            token_index -= 1;                
        token_index += 1;
        
    token_index = 0 
    #print(tokens);
    while (token_index < (len(tokens)- ngrams + 1)):
        i = 0
        temp_tuple_list = []
        while i < ngrams:
            if(lower_case):
                word = tokens[token_index+i].lower()   
            else:
                word = tokens[token_index+i];
            temp_tuple_list.append(word)
            i += 1
        new_tuple = tuple(temp_tuple_list)
        del(temp_tuple_list)
        touple_list.append(new_tuple)
        token_index += 1
    #print("\n\n End preprocessing.\n\n")
    
    #compute frequency distribution for all the ngrams in the text
    fdist = nltk.FreqDist(touple_list)
    #print(fdist);
    return(dict(fdist));    
