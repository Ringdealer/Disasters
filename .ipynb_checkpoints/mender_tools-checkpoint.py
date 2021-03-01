import pandas as pd
import re


def emend_values(orig_df, mod_df, source_col, target_col, pattern):
    """
    Method for assigning the correct values to its corresponding column. Note that
	we are going to use the original dataframe (orig_df) in order to keep its data inmutable
	"""
    i = 0
    for word in orig_df[source_col]:
        if isinstance(word, str):
            word.rstrip() # Removes white space at the end of the string
            match = re.search(pattern, word)
            if match:
                 mod_df.at[i, target_col] = match.string
                 i += 1
            else:
                i += 1               
        else:
            i += 1    

    return mod_df

def strip_symbol(df, col, pattern):
    """Method for striping the symbol that comes with each number"""
    i = 0
    for word in df[col]:
        if isinstance(word, str):
            word = word.replace(pattern, '')
            df.at[i, col] = word
            i += 1
        else:
            i += 1
			
    return df

def convert_to_int(df, column, pattern):
    """Method for converting strings to int"""
    i = 0
    for word in df[column]:
        if isinstance(word, str):

            if re.search(pattern, word):
                if re.search(pattern, word).group().isdigit():
                    df.at[i, column] = int(re.search(pattern, word).group())
                    i += 1
        else:
            i += 1

    return df


def convert_to_nan(df, column):
    """
	Method for converting values to NaN
	"""
    i = 0
    for word in df[column]:
        if isinstance(word, str):
            df.at[i, column] = None
        i += 1

    return df


def fill_na(df, column):
    """
	Method for filling empty cells with NaN
	"""
    i = 0
    for word in df[column]:
        if word is None:
            df.at[i, column] = 0
        i += 1

    return df




