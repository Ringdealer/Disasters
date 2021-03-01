from io import StringIO
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import sys
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import math
import data_munging as cleaner
import reverse_geocoder as rg


df = pd.read_csv('blazes/test.csv')

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
"""
df.columns = ['Cause', 'Coordinates', 'Date', 'Fuels Involved', 'Incident', 'Incident Type', 'Location', 'Perimeter Contained (%)', 'Personnel Involved', 'Area Contained (Acres)']
df.dropna(how='all', inplace=True)
df.reset_index(inplace=True)
"""
#df.loc[:,:] = df.applymap(lambda x: x.strip() if type(x)==str else x)

"""
st = us_abbrev_dic={
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona':'AZ',
    'Arkansas':'AR',
    'California': 'CA',
    'Colorado':'CO',
    'Connecticut':'CT',
    'Delaware':'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

def foo(df, col):
    i = 0
    flag = 0
    for sentence in df[col]:
        if isinstance(sentence, str):
            word_list = re.findall(r'\w+', sentence)
            word_list_len = len(word_list) - 1
            for word in word_list:
                wordup = word.upper()
                for st_name, st_abbrev in st.items():
                    upper_st = st_name.upper()
                    if (wordup == upper_st or wordup == st_abbrev):
                        df.at[i, 'State Names Test'] = st_name
                        i += 1
                        flag = 1
                        break
                if (word_list.index(word) == word_list_len and flag == 0):
                    df.at[i, 'State Names Test'] = ""
                    i += 1
                elif (flag == 1):
                    flag = 0
                    break
        else:
            df.at[i, 'State Names Test'] = ""
            i += 1
    return None

result = ""
def is_match(pattern, x, word):
    global result
    if isinstance(x, str):
        match = re.search(pattern, x)
        if match:
            result = x.replace(match.string, word)
        else:
            return False
    else:
        return False
    return True

df.loc[:, 'Cause'] = df.loc[:, 'Cause'].apply(lambda x:\
x.replace(x, result)\
    if is_match(r'[Hh]uman[-]?', x, 'Human Caused') else x)

for item in df.loc[:, 'Cause']:
    print(item)
    
"""


# Get the location given by latitude and longitude coordinates
def get_location(coordinates):
    return rg.search(coordinates)

def create_region_col(df):
    i = 0
    for latitude in df['Latitude']:
        for longitude in df['Longitude']:
            if (not math.isnan(latitude) and not math.isnan(longitude)):
                coordinates = (latitude, longitude)
                location = get_location(coordinates)
                df.at[i, 'Region'] = list(location[0].values())[3]
                i += 1
            else:
                i += 1
            break


if __name__ == '__main__':
    create_region_col(df)

print(df.loc[:, ['Longitude', 'Region']].head(100))
