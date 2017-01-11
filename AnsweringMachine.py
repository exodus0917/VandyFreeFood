# Filename: AnsweringMachine
# Description: this class accepts a string (question from the user), and will have an appropriate
#               answer (events for a specific date) according to the input string.
#               The instance variables are
#                   self._message -> the user's message
#                   self._words -> the words inside the user's message
#                   self._answer -> the appropriate answer according to the user's message
#
# Author: Bumsu Jung
# Creation Date: 12/28/16
# Latest Update: 12/30/16


class AnsweringMachine:
    def __init__(self, message):
        message = message.lower()
        self._words = set()

        # Erasing empty spaces in the beginning for the message
        i = 0
        while message[i] == ' ':
            i += 1
        message = message[i:]

        # Putting all the words inside the message into a set called self._words
        j = 0
        for i in range(len(message)):
            if message[i] == ' ':
                self._words.add(message[j:i])
                j = i + 1
        self._message = message


        # Interpretation will happen here - User the interpreter pattern here
        # runs a loop to interpret
        if 'today' in self._words:
            self._answer = 'Today there are 2 events!'
        else:
            self._answer = 'Sorry I can only tell you about the events for today'

    def answer(self):
        return self._answer