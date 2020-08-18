import re
import pandas as pd


def convert_to_int(df, column, pattern):
    # Method for converting strings to int using regex
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
    i = 0
    for word in df[column]:
        if isinstance(word, str):
            df.at[i, column] = None
        i += 1

    return df


def fill_na(df, column):
    i = 0
    for word in df[column]:
        if word is None:
            df.at[i, column] = 0
        i += 1

    return df


def convert_and_assign(orig_df, mod_df, col1, col2, pattern):
    # Method for converting strings to int using regex
    i = 0
    for word in orig_df[col1]:
        if isinstance(word, str):
            if re.search(pattern, word):
                if re.search(pattern, word).group().isdigit():
                    mod_df.at[i, col2] = re.search(pattern, word).group()
                    i += 1
        else:
            i += 1

    return mod_df
