"""

Read all files 

"""
import os;

def read_file( path_to_file ):
    file_handle = open( path_to_file,"r");
    return file_handle.read();

def list_all_text_files( path ):
    all_files = os.listdir(path);
    all_text_files = [];
    for file_name in all_files:
        if( file_name.endswith(".txt") ):
            all_text_files.append(path+file_name);
    return(all_text_files);
        
        
    