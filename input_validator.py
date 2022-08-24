# Copyright (C) Eva Malpaya
# #################################################################################################################### 
# Eva Malpaya
# CS 372, Oregon State University
# Programming Project 4
# August 7, 2022
# #################################################################################################################### 

class Input_validator():
    min = -1
    max = -1
    promptMsg = ""
    prompt = ""

    def __init__(self, setMin, setMax, setPromptMsg):
        self.min = setMin
        self.max = setMax
        self.promptMsg = setPromptMsg
        self.prompt = '>'

    def getInput(self):
        while True:
            print("Type 'quit' to quit (without quotes)")  
            print(self.promptMsg, end="")
            print(str(self.min) + '-' + str(self.max) + ":")            
            userInput = input (self.prompt)

            if (userInput.upper() == 'QUIT'):
                return userInput  
            elif not userInput.isnumeric():
                print('!!!\r\nOops! Invalid choice selected.')
                print('Please try again.')                
            elif int(userInput) not in range(self.min, self.max + 1):
                print('!!!\r\nOops! Invalid choice selected.')
                print('Please try again.')
            else:
                return userInput