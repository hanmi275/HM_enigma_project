#print("Hello World from the algorithm file!")
import string
import sys
from .enigma import enigma

"""
Documentation of algorithm.py
"""
def encode(inpt):
    """
    Returns the user-entered message in enigma-code.
    Dissects the entered string into letters who are individually translated into enigma code by functions of the enigma class.
    
    Parameters
    ----------
    inpt : string
    
    Returns
    ----------
    code_out : string
    """
    # Initialze class
    my_enigma = enigma()
    # and an empty array to collect the returned coded letters.
    code = []
    # Iterate over input string:
    for letter in inpt:
        # lower case letters are encoded using the enigma class
        if letter in string.ascii_lowercase:
            code.append(my_enigma.code(letter))
        # spaces are appended directly. The original enigma code did not feature spaces, however for testing of this algorithm they enhance the visibilty greatly
        elif(letter == " "):
            code.append(letter)
        # For any other signs/numbers/uppercase, draw and error and exit the program
        else:
            print(">> Sir, I don't know %s.... \n --- Enigma terminated ---" % letter)
            sys.exit()
    # join the obtained collection of chars back to a string
    code_out = ''.join(code)
    # display the code and return it
    print(">> The enigma machine encoded your message: \n%s" % code_out)
    return(code_out)
    
def decode(code):
    """
    Returns the message corresponding to the user-entered enigma code.
    Dissects the entered string into letters who are individually translated from enigma code by functions of the enigma class.
    As the enigma machine was based on a "umkehrwalze" (reflector), the coding and decoding process follows exactly the same path as (for each step) two letters correspond to each other. Therefore the same function my_enigma.code can be used for decoding as well. The rest of the function is also constructed following the "encode" function.
    
    Parameters
    ----------
    inpt : string
    
    Returns
    ----------
    code_out : string
    """
    my_enigma = enigma()
    otpt = []
    for letter in code.lower():
        #print(letter)
        if(letter.isalpha()):
            otpt.append(my_enigma.code(letter))
        else:
            otpt.append(letter)
    otpt_out = ''.join(otpt)
    print(">> The enigma machine decoded your message: \n%s" % otpt_out)
    return(otpt_out)
    
def test(inpt):
    """
    Tests the written enigma machine by forth-and-back translation of the given user input and then calling the abovementioned functions. Depending on the result of the test, messages are displayed.
    
    Parameters
    ----------
    inpt : string
    
    Returns
    ----------
    ~none~
    """
    code = encode(inpt)
    otpt = decode(code)
    if(otpt == inpt):
        print(">> Enigma sucessfully transfered your message!")
    else:
        print(">> Oooooops, something went wrong....")
    
    
    
