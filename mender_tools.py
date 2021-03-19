import dateparser
import numpy as np
import re



def emend_values(orig_df, mod_df, source_col, target_col, pattern):
    """
    Function for assigning the correct values to its corresponding column. Note that
	we are going to use the original dataframe (orig_df) in order to keep its data inmutable
	"""
    i = 0
    for word in orig_df[source_col]:
        if isinstance(word, str):
            word = word.rstrip() # Removes white space at the end of the string
            match = re.search(pattern, word)
            if match:
                 mod_df.at[i, target_col] = match.string
                 i += 1
            else:
                i += 1               
        else:
            i += 1    

    return mod_df

def strip_string(mod_df, col, pattern):
    """Function for deleting a string specified by the user"""
    i = 0
    for word in mod_df[col]:
        if isinstance(word, str):
            word = word.rstrip()
            match = re.search(pattern, word)
            if match:
                word = word.replace(match.string, '')
                mod_df.at[i, col] = word
                i += 1
            else:
                i += 1
        else:
            i += 1            
    return mod_df

def strip_symbol(mod_df, col, pattern):
    """Function for striping the unit symbol that accompanies each number"""
    i = 0
    for word in mod_df[col]:
        if isinstance(word, str):
            word = word.replace(pattern, '')
            mod_df.at[i, col] = word
            i += 1
        else:
            i += 1			
    return mod_df

def remove_pattern(df, col, pattern):
    """ Function for removing the corresponding match."""
    i = 0
    for word in df[col]:        
        if isinstance(word, str):
            df.at[i, col] = re.sub(pattern, '', word)
            i += 1
        else:
            i += 1  

def convert_to_int(mod_df, col):
    """ Function for converting strings to integer values """
    i = 0
    for word in mod_df[col]:
        if isinstance(word, str):
            word = word.rstrip()
            word = word.replace(',', '')
            if word.isdigit():
                mod_df.at[i, col] = int(word)
                i += 1
            else:
                i += 1
        else:
            i += 1
    return mod_df


def str_to_nan(mod_df, column):
    """Function for converting string values to NaN"""
    for word in mod_df[column]:
        if isinstance(word, str):
            mod_df[column].replace(word, np.nan, inplace=True)
    return mod_df

def convert_to_string(mod_df, col):
    """Fills NaN values with string '-1' then converts all values to strings 
       and replaces all -1s with NaNs"""
    mod_df[col] = mod_df[col].fillna('-1')
    mod_df[col] = mod_df[col].astype(str)
    mod_df[col] = mod_df[col].replace('-1', np.nan)    
    return mod_df


def create_new_col(df, pattern, src_col, new_col):
    """Function for creating a new column"""
    i = 0
    for word in df[src_col]:        
        if isinstance(word, str):
            if(re.search(pattern,word)):
                match = re.search(pattern, word)
                df.at[i,new_col] = match.group()
                i += 1
            else:
                df.at[i,new_col] = ''
                i += 1
        else:
                df.at[i,new_col] = ''
                i += 1               
    return df

def convert_to_isodate(df, col):
    """Function for converting string date to ISO date format
    and assign it to a new column"""
    i = 0
    for word in df[col]:        
        if isinstance(word, str):
            word = word.rstrip()
            try:
                df.at[i, 'ISO Date'] = dateparser.parse(word).isoformat()
                i += 1
            except(AttributeError):
                pass
                i += 1
        else:
            i += 1 
    return df