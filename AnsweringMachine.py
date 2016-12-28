# Filename: AnsweringMachine
# Description: this class accepts a string (question from the user), and will have an appropriate
#               answer (events for a specific date) according to the input string
#
# Author: Bumsu Jung
# Creation Date: 12/28/16
# Latest Update: 12/28/16


class AnsweringMachine:
    def __init__(self, message):
        self._message = message
        # Interpretation will happen here - User the interpreter pattern here
        # runs a loop to interpret
        self._answer = ''



    def answer(self):
        return self._answer