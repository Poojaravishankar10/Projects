"""
Pre processor
"""
import re;

def preprocess(text):
    r_unwanted = re.compile('\n')
    r_unwanted.sub("", text)
    #new_data = re.sub(r'[-|>|,|\'|\(|\)|\\|#|:|"]',r' ',text);
    new_data = re.sub(r'[-|+|>|<|}|{|_|~|*|/|=|\(|\)|\\|#|:|;|$|\`|\"|\[|\]|\^|#|\%|\&|]', r' ', text );
    #print(new_data);
    return new_data;
