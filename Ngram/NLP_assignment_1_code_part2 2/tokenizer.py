import nltk;
import math;
nltk.download('punkt')


def add_start_end_sentence_tags(tokens, ngrams, sent_end_chars, remove_extras =1) :
    #Needed for training model for random sentence generation, sentence completion, perplexity, topic classification
    #

    #For perplexity calculation- don't call this function on test set 

    token_index = 0;    
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
        elif( remove_extras and
             (".co" in tokens[token_index] or 
              "@" in tokens[token_index] or
              ".ed" in tokens[token_index] or 
              tokens[token_index] in ["Subject", "Re"]) ):
            del tokens[token_index]
            token_index -= 1;                
        token_index += 1;
    return tokens;

def preprocess_for_unknown_word_handling(tokens):
    # one <unk> for all n-grams
    #return list of tokens - 1D array
    token_freq = dict()
    token_freq = nltk.FreqDist(tokens);
    token_index = 0;
    while (token_index < (len(tokens))) :
        key = tokens[token_index]
        #print(key, token_freq[key])
        if (token_freq[key] == 1) :
            tokens[token_index] = '<unk>'
        token_index += 1
    return tokens;
   
def calculate_vacabulary_size(tokens):
    #token is a 1d array
    token_freq = nltk.FreqDist(tokens);
    vacabulary_size = 0
    for key in token_freq:
        vacabulary_size += 1;    
    #print("\n vacabulary size",vacabulary_size);
    return vacabulary_size;
  
def build_tuple_list(tokens, ngrams, lower_case):
    #returns a [(n elements), (), ()]
    tuple_list = []
    token_index = 0
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
        tuple_list.append(new_tuple)
        token_index += 1
    return tuple_list;
    
def interpolate_get_freq(freq_of_freq, non_zero_arr, index):
    value = 0;
    if(non_zero_arr[index] != index ):
        value = freq_of_freq[non_zero_arr[index]]/(non_zero_arr[index]-index+1);
    else:
        value = freq_of_freq[index];
    return value;  
#
# tokens      : All the tokens after processing the text.
# token_index : Indexing into the list container all the tokens.
# touple_list : list of touples. Length of each touple will be equal to ngrams.
# temp_tuple_list : buils a temporary list which becomes one touple.
#
def tokenize( text, ngrams, sent_end_chars, lower_case = 0, test_data = 0):
    
    tokens = nltk.word_tokenize(text);
    #print(tokens);
    tuple_list = []
    

    '''                    ADDING START/END SENTENCE TAGS                   '''    
    #
    # Finding lenght of tokens in every iteration is not efficient.
    # We should find the length of tokens once before the while loop
    # and update it accordingly based on number of <s> tokens we add.
    #
    #print("\n\n Begin preprocessing....\n\n")
         
    #print(tokens);
    tokens = add_start_end_sentence_tags(tokens, ngrams, sent_end_chars);
    
    '''                       UNKNOWN WORD HANDLING                         '''
    #
    # Replacing words present only once in corpus to <unk>
    # Check if we need to insert ngram-1 unknown words.
    #
    if (not test_data) :
        tokens = preprocess_for_unknown_word_handling(tokens);
    
    
    '''                     FINDING THE VACABULARY SIZE                     '''
    
    vacabulary_size = calculate_vacabulary_size(tokens);

    
    '''           BUILDING THE TPULE LIST AS PER THE CHOSEN NGRAM           '''
    #
    # Based on the chosen ngram model, buiding the touple list.
    #
    tuple_list = build_tuple_list(tokens, ngrams, lower_case);
    #print(tuple_list)
    if (test_data):
        return ((len(tokens)), tuple_list);
    
    #compute frequency distribution for all the ngrams in the text
    fdist = nltk.FreqDist(tuple_list)
    
   
    '''              FINDING NUMBER OF NGRAMS REPEATED 0 TIMES              '''
    '''                     FINDING THE MAXIMUM FREQUENCY                   '''
   
    ngram_count_in_corpus = 0; #count unique n-gram tuples
    ngram_count_of_zero_freq = 0;
    max_freq = -1;
    for key in fdist:
        ngram_count_in_corpus += 1
        if (fdist[key] > max_freq):
            max_freq = fdist[key];
            
    
    ngram_count_of_zero_freq = (math.pow( vacabulary_size, ngrams ) - 
                                ngram_count_in_corpus);
    #print("\n Count of ngrams present: ",ngram_count_in_corpus)
    #print("\ncount of ngrams repeated 0 times:",ngram_count_of_zero_freq);    
    #print("\n maximum freqency is :",max_freq)
    
    
    '''               CALCULATING FREQUENCY OF FREQUENCY                    '''

    #
    # Frequency of frequency !
    # Move this code to probability calculation module or may be a new module.
    #
    i = 0;
    freq_of_freq = [];
    while i <= max_freq :
        freq_of_freq.append(0); #Instead try with arrays.
        i += 1;
    freq_of_freq[0] = ngram_count_of_zero_freq;
 
   
    #print("\nbefore smoothing\n")
    #print_count = 0;
    for key in fdist:
            freq_of_freq[fdist[key]] += 1
            '''
            if (print_count < 50):
                print(key,fdist[key])
            print_count += 1
            '''
    #print(dict(fdist));
            
    '''                       GOOD TRUING SMOOTHING                         '''
    #
    # C* = (c+1)*Nc+1/Nc (what if Nc is zero)
    #
    # Applicable only for frequencies whihc are less than k(=5 for now)
    # We are going to do smothing only for bigrams.
    # in case of unigram N0 and N1 will be zero!
    #       
    #print("\nfrequency table\n",freq_of_freq)
    #print("\n\nafter smoothing\n")
    #print_count = 0
    non_zero_index_arr = [];
    freq_of_freq_index = 0;
    next_non_zero_index = 0;    
    for v in freq_of_freq:
        if(v != 0):
            next_non_zero_index = freq_of_freq_index;
        elif(next_non_zero_index<freq_of_freq_index):
            next_non_zero_index = freq_of_freq_index;
            while(freq_of_freq[next_non_zero_index]==0):
                next_non_zero_index +=1;
        non_zero_index_arr.append(next_non_zero_index);   
        freq_of_freq_index +=1;
    #print(non_zero_index_arr, "\n\n", freq_of_freq);         

    good_turing_zero = interpolate_get_freq(freq_of_freq, non_zero_index_arr, 1) /ngram_count_of_zero_freq; #freq_of_freq[1]
    k = 5; ##### parameter to be tuned with dev set
    temp_list = []
    zero_list = dict();
    for key in fdist:
        c = fdist[key]
        if (c < k):
            fdist[key] = (c+1)*interpolate_get_freq(freq_of_freq, non_zero_index_arr,c+1)/ interpolate_get_freq(freq_of_freq, non_zero_index_arr, c);
        '''
        if (print_count < 50):
                #print(key,fdist[key])
        print_count += 1
        '''
        
        temp_list = key[0:ngrams-1];
        temp_list += ('<zero>',)
        temp_list = tuple(temp_list);
        zero_list[temp_list] = good_turing_zero;
    for x in zero_list:
        fdist[x] = zero_list[x];
    #print(fdist);
    return (dict(fdist));
