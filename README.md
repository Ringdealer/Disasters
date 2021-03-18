# Learn to Scrape and Analyze Data

## Analyzing Forest Fires

---

![](https://img.shields.io/badge/made_by-Ringdealer-blue)

[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/Ringdealer/forest-fires.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Ringdealer/forest-fires/context:python)

[![GitHub issues](https://img.shields.io/github/issues/Ringdealer/forest-fires?style=plastic)](https://github.com/Ringdealer/forest-fires/issues)



---
<img src="./High.jpg">

> Badass Hot Bold Guy
---

## Table of Contents
- [Description](#description)
- [Technologies](#technologies)
- [Installation](#installation)
- [API Reference](#api-reference)
- [Using Jupyter Notebook](#jupyter)
- [Roadmap](#roadmap)
- [Comments and Suggestions](#comments)


---

### Description
This project uses a csv file scraped from InciWeb (http://inciweb.nwcg.gov), an interagency all-risk incident web information management system, with information about forest fires in the United States. The aim of this project is to show all the stages of the data analysis workflow. The steps to follow are:

- Scrape the data set
- Prepare and clean the data set
- Deal with missing values and data transformation
- Apply machine learning algorithms and data visualization tools

I considered after scraping the web site to start documenting the project with the second stage. Here I discuss how to prepare and manage the data set for wrongly inserted info and type conversion. The project illustrates different tools provided by Python to perform these tasks.

---

### Technologies
- Python
- Jupyter

---

### Installation
- pip install pandas
- pip install numpy
- pip install dateparser
- pip install reverse_geocoder

---

### API Reference
```python
def convert_to_int(mod_df, col):
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
```
---
### Using Jupyter Notebook

The csv file is in folder `blazes`, to read it into a data frame run the command:

`df = pd.read_csv('blazes/fires.csv')`

 The functions written to deal with the data are in module `mender_tools.py`. To import the module in a Jupyter notebook:

 `import mender_tools as mt`

---
### Roadmap
The project is 4 chapters long not including the  introduction and appendix: 

- Chapter 1: Scraping the Web Site
- Chapter 2: Preparing the Data
- Chapter 3: Dealing with Missing Values 
- Chapter 4: Analysis of the Data



Currently chapter 2 is finished. I pretend to follow with chapter 3 and chapter 4, leaving chapter 1 last. The whole project will be documented in a single pdf file.

---
### Comments and Suggestions

---


## References

[Back to the Top](#Learn-to-Scrape-and-Analyze-Data)


