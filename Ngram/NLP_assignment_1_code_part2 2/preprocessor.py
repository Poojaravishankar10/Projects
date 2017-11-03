"""
Pre processor
"""
import re;

#Add comments here saying some of our preprocesing work like ading <s> has been
#moved to tokenizer for efficiency.
 
def preprocess(text):
    r_unwanted = re.compile('\n')
    r_unwanted.sub("", text)
    #new_data = re.sub(r'[-|>|,|\'|\(|\)|\\|#|:|"]',r' ',text);
    new_data = re.sub(r'[-|+|>|<|}|{|_|~|*|/|=|\(|\)|\\|#|:|;|$|\`|\"|\[|\]|\^|#|\%|\&|]', r' ', text );
    #print(new_data);
    return new_data;
    #return text;