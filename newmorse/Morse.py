"""
Morse file.

This file is used to encode and decode messages
"""


class Morse:
    """
    This class stores 3 functions.

    set_morse to initialize the array and return its values.
    decodeMorse to decode the message.
    encodeMorse for encode the message.
    """

    def set_morse(self, dot=".", dash="-"):
        """
        Set morse fun.

        Create a function to initialize the morse code array
        this function has two arguments for the dot and for the dash,
        which are specified in the main
        """
        """
         Create morse code dictionary list
        """
        self.morse_code = {dot + dash + dot * 3: "&",
                           dash * 2 + dot * 2 + dash * 2: ",",
                           dot * 4 + dash: "4", dot * 5: "5",
                           dot * 5: "5",
                           dot * 3 + dash * 3 + dot * 3: "SOS",
                           dash + dot * 3: "B",
                           dash + dot * 2 + dash: "X",
                           dot + dash + dot: "R",
                           dot + dash * 2: "W",
                           dot * 2 + dash * 3: "2",
                           dot + dash: "A",
                           dot * 2: "I",
                           dot * 2 + dash + dot: "F",
                           dot: "E", dot + dash + dot * 2: "L",
                           dot * 3: "S", dot * 2 + dash: "U",
                           dot * 2 + dash * 2 + dot * 2: "?",
                           dot + dash * 4: "1", dash + dot + dash: "K",
                           dash + dot + dot: "D",
                           dash + dot * 4: "6", dash + dot * 3 + dash: "=",
                           dash * 3: "O", dot + dash * 2 + dot: "P",
                           dot + dash + dot + dash + dot + dash: ".",
                           dash * 2: "M", dash + dot: "N", dot * 4: "H",
                           dot + dash * 4 + dot: "'", dot * 3 + dash: "V",
                           dash * 2 + dot * 3: "7",
                           dash + dot + dash + dot + dash + dot: ";",
                           dash + dot * 4 + dash: "-",
                           dot * 2 + dash * 2 + dot + dash: "_",
                           dash + dot + dash * 2 + dot + dash: ")",
                           dash + dot + dash + dot + dash * 2: "!",
                           dash * 2 + dot: "G", dash * 2 + dot + dash: "Q",
                           dash * 2 + dot * 2: "Z",
                           dash + dot * 2 + dash + dot: "/",
                           dot + dash + dot + dash + dot: "+",
                           dash + dot + dash + dot: "C",
                           dash * 3 + dot * 3: ":",
                           dash + dot + dash * 2: "Y",
                           dash: "T",
                           dot + dash * 2 + dot + dash + dot: "@",
                           dot * 3 + dash + dot * 2 + dash: "$",
                           dot + dash * 3: "J",
                           dash * 5: "0", dash * 4 + dot: "9",
                           dot + dash + dot * 2 + dash + dot: '"',
                           dash + dot + dash * 2 + dot: "(",
                           dash * 3 + dot * 2: "8",
                           dot * 3 + dash * 2: "3"}
        return self.morse_code

    def decodeMorse(morseCode, morse_code):
        """Decode from morse code."""
        """
        split message.
        create an empty array to
        put the decoded text there
        """
        morseCodeDict = morseCode.split(" ")
        output = []
        """
         compare each object in the array
         with the keys of objects in the morse dictionary array,
         and if there is a match,
         add an object from the morse
         dictionary by the matched key
         """
        for morse in morseCodeDict:
            try:
                output.append(morse_code[morse])
            except KeyError:
                if morse == "":
                    output.append(" ")
                else:
                    pass
        """create a string from the array.
         return its text in lowercase"""
        output = "".join(output)
        return output.lower()

    """Create a function to encode the message.
    which takes two arguments:
    the text to encode and the morse code dictionary"""

    def encodeMorse(toEncode, morse_code):
        """Encode from text to morse code."""
        """
        we invert the morse code dictionary
        to make it possible to enumerate the array.
        Create an array from the input text.
        create an empty array to write the translation into"""

        morse_code_inverted = {v: k for k, v in morse_code.items()}

        toEncodeDict = list(toEncode)

        output = []

        """
        for each character in the input
        text array we try to find a match with the characters in
        the morse code dictionary array
        (convert the input text characters to uppercase).
        If there is a match,
        then add the object key to the output array.
        If not, add a space.
        """
        for char in toEncodeDict:
            try:
                output.append(morse_code_inverted[char.upper()])
            except KeyError:
                if char == " ":
                    output.append(" ")
                else:
                    pass

        """return the output array"""
        return " ".join(output)

    pass
