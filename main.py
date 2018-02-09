#!/usr/bin/env python
""" 
Welcome to the documentation of my virtual enigma machine!
Using this algorithm module you can encode and decode messages.

This main function parses user input and forwards it to the en-/decoding algorithm. Output is generated within the algorithm functions.

Several print-statements are prepared in the subroutines to enable the user to possibly track the encoding process.
"""

import sys
import func.algorithm as alg

# Ask which function user wants to run
program_select = input(">> Welcome to the virtual enigma machine! \n 1: Encode a message \n 2: Decode a message \n 3: Test the program (encode+decode) \n")
# Check if integer was entered
if not program_select.isdigit():
    print(">> Use numbers 1-3 to select the task for enigma! \n --- Enigma terminated ---")
    sys.exit()  
# and assign this number to the program_select
program_select = int(program_select)

# Did the user select one of the suggested options? If not, terminate
if(program_select < 1 | program_select > 3):
    print(">> Pleas choose among the abovementioned options! \n --- Enigma terminated ---")
    sys.exit()
    
# If so did, ask for input and explain available options
inpt = input(">> Sir, the enigma code supports: \n>> --> lower case letters from a 26-letter alphabet \n>> --> luckily nowadays spaces! \nYour message please: \n")

#and launch respective function.
if(program_select == 1):
    #print("entered if")
    alg.encode(inpt)
elif(program_select == 2):
    alg.decode(inpt)
elif(program_select == 3):
    alg.test(inpt)
        
