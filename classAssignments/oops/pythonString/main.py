import logging
logging.basicConfig(filename="main.log",level=logging.INFO,format="%(levelname)s %(asctime)s %(message)s")
logging.info("Logged into main file.")
print("Welcome to String Functions....!")
import stringFunctions
""" 
    string_extract - extracts string from 1-300 with the skip of 3.
    string_reverse - reverse the given string data.
    string_upper   - converts the whole string into upper case.
    string_lower   - converts the whole string into lower case.
    string_caps    - capitalizes the given string.
    string_strip   - remove white spaces from both adjacent sides of the given string.
    string_lstrip  - remove white-spaces from left side of the given string.
    string_rstrip  - remove white-spaces from right side of the given string.
"""
fun=stringFunctions.String()
