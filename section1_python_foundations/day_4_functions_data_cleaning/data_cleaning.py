"""
This is an introductions into functions and data cleaning
syntax

def function_name:
    return task
functions_name()

"""
import re
def cleaning_data(text):
        if not text:
                return ""
        text = text.lower()
        return text
raw_text =input("Input text in upper case: ")

print(cleaning_data(raw_text))