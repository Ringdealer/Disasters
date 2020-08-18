import re
import pandas as pd

def convert_and_assign(orig_df, mod_df, col1, col2, pattern):
    # Method for converting strings to int using regex
    i = 0
    for word in orig_df[col1]:
        if isinstance(word, str):
            if re.search(pattern, word):
                mod_df.at[i, col2] = re.search(pattern, word).group()
                i += 1
        else:
            i += 1

    return mod_df


