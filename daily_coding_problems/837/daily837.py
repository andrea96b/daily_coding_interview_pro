# This problem was asked by Nest.

# Create a basic sentence checker that takes in a stream of characters and determines whether they form valid sentences.
# If a sentence is valid, the program should print it out.

# We can consider a sentence valid if it conforms to the following rules:

# The sentence must start with a capital letter, followed by a lowercase letter or a space.
# All other characters must be lowercase letters, separators (,,;,:) or terminal marks (.,?,!,‽).
# There must be a single space between each word.
# The sentence must end with a terminal mark immediately following a word.
# Ex1: This, is a correct sentence. (True)
# Ex2: this  is wrong (False)


class SentenceChecker:
    
    def __init__(self):
        self.state = self.__s1
        self.valid = False
        self.separators = [',',';',':']
        self.terminals = ['.','?','!']

    def __s1(self,char):
        if char.isupper():
            return self.__s2
        else:
            return None
    
    def __s2(self,char):
        if char.islower():
            return self.__s4
        elif char == ' ':
            return self.__s3
        else:
            return None
    
    def __s3(self,char):
        if char.islower():
            return self.__s4
        elif char == ' ':
            return None

    def __s4(self,char):
        if char.islower():
            return self.__s4
        elif char == ' ':
            return self.__s3
        elif char in self.separators:
            return self.__s5
        elif char in self.terminals:
            self.valid = True
            return None

    def __s5(self,char):
        if char == ' ':
            return self.__s4
        else:
            return None

    def check(self,sentence : str) -> bool:
        self.valid = False
        self.__state = self.__s1
        for char in sentence:
            if self.__state:
                self.__state = self.__state(char)
        return self.valid



if __name__=="__main__":
    pass