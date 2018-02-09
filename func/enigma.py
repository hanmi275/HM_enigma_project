"""
Documentation of algorithm.py
"""
class enigma:
    def __init__(self):
        """
        Sets up inigma class. Constitution of rotors and reflector. None that: The rotor strings are meant to correspond to a sorted alphabet 'on their backside' which can be drawn from the self.keyboard. The reflector connects pairs of letters, respectively, which are located next to each other in this approach.
        
        Parameters
        ----------
        ~none~
        
        Returns
        ----------
        ~none~
        """
        self.keyboard = "abcdefghijklmnopqrstuvwxyz"
        self.first_rotor = "ekmflgdqvzntowyhxuspaibrcj"
        self.second_rotor = "ajdksiruxblhwtmcqgznpyfvoe"
        self.third_rotor = "bdfhjlcprtxvznyeiwgakmusqo"
        self.reflector = "iuasdvglftoxezchmrknbqpwjy"
    
    def code(self, inpt):
        """
        Function that gets called from the algorithm module. Takes user inpt (one letter) and sends it through the enigma machine in three steps (illustrated in the following functions, respectively).
        Note: several print-statements are available to view the process of the coding.
        
        Parameters
        ----------
        inpt : char
        
        Returns
        ----------
        code : char
        """
        #print("Letter input: %s" % inpt)
        #print(">> First rotor: %s" % self.first_rotor)
        #print(">> Second rotor: %s" % self.second_rotor)
        #print(">> Third_rotor: %s" % self.third_rotor)
        code = self.reform(self.reflect(self.transform(inpt)))
        #print("Letter output: %s" % code)
        return(code)
    
    def transform(self,letter):
        """
        Takes the sent letter and translates it according to the positions of the three rotors. 
        MOTION: As for the original enigma machine, any pressed key will trigger a movement step of the first rotor before(!) the translation. Furthermore, when the first rotor reaches position 'r', an immediate motion step on rotor is triggered, and if the second rotor gets to 'f', rotor c moves.
        TRANSLATION: Let's assume, 'a' was supplied to the algorithm. According to rotor I, this translates to an e. The second rotor recieves the 'e' and (as it is the 5th letter on it's alphabetically ordered side) translates this to an 's', which is then passed to the third rotor. The letter resulting from the third rotor is returned.
        If 'a' was sent'
        Note: several print-statements are available to view the process of the coding.
        
        Parameters
        ----------
        letter : char
        
        Returns
        ----------
        code : char
        """
        self.first_rotor = self.first_rotor[25]+self.first_rotor[0:25]
        #print(">> First rotor moved to: %s" % self.first_rotor)
        if self.first_rotor[0] == "r":
            self.second_rotor = self.second_rotor[25]+self.second_rotor[0:25]
            #print(">> Triggered second rotor! Second rotor moved to: %s" % self.second_rotor)
            if self.second_rotor[0] == "f":
                self.third_rotor = self.third_rotor[25]+self.third_rotor[0:25]
                #print(">> Triggered third rotor! Third rotor moved to: %s" % self.third_rotor)
        return self.third_rotor[self.keyboard.index(self.second_rotor[self.keyboard.index(self.first_rotor[self.keyboard.index(letter)])])]
    
    def reflect(self, letter):
        """
        Implements the reflector ("Umkehrwalze). Pairs of letters are connected and located next to each other in the self.reflector string. Using modulo 2, the function determines to which side the current letter is associated and returns the counterpart.
        
        Parameters
        ----------
        letter : char
        
        Returns
        ----------
        code : char
        """
        idx = self.reflector.index(letter)
        if idx % 2 == 0:
            return self.reflector[idx+1]
        else: 
            return self.reflector[idx-1] 
        
    def reform(self, letter):
        """
        According to the transform function. The letters are passed backwards through the rotors, no motion is triggered.
        
        Parameters
        ----------
        letter : char
        
        Returns
        ----------
        code : char
        """
        return self.keyboard[self.first_rotor.index(self.keyboard[self.second_rotor.index(self.keyboard[self.third_rotor.index(letter)])])]
        
    def __str__(self):
        """
        Displays current rotor positions.
        
        Parameters
        ----------
        ~none~
        
        Returns
        ----------
        ~none~
        """
        print(">> Enigma rotor at position %s %s %s!" % (self.first_rotor[0], self.first_rotor[0], self.first_rotor[0]))
