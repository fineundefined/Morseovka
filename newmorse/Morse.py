class Morse:

    def decodeMorse(morseCode, morse_code):

        morseCodeDict = morseCode.split(" ")

        output = []

        for morse in morseCodeDict:
            try:
                output.append(morse_code[morse])
            except KeyError:
                if morse == "":
                    output.append(" ")
                else:
                    pass

        output = "".join(output)
        return output.lower()

    def encodeMorse(toEncode, morse_code):

        morse_code_inverted = {v: k for k, v in morse_code.items()}

        toEncodeDict = list(toEncode)

        output = []

        for char in toEncodeDict:
            try:
                output.append(morse_code_inverted[char.upper()])
            except KeyError:
                if char == " ":
                    output.append(" ")
                else:
                    pass

        return " ".join(output)

    pass
