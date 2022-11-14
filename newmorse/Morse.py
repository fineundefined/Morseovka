class Morse:


    def decodeMorse(morseCode, dot='.', dash='-'):
        morse_code = {dot + dash + dot * 3: "&", dash * 2 + dot * 2 + dash * 2: ",", dot * 4 + dash: "4", dot * 5: "5",
                      dot * 5: "5", dot * 3 + dash * 3 + dot * 3: "SOS", dash + dot * 3: "B",
                      dash + dot * 2 + dash: "X",
                      dot + dash + dot: "R", dot + dash * 2: "W", dot * 2 + dash * 3: "2", dot + dash: "A",
                      dot * 2: "I",
                      dot * 2 + dash + dot: "F", dot: "E", dot + dash + dot * 2: "L", dot * 3: "S", dot * 2 + dash: "U",
                      dot * 2 + dash * 2 + dot * 2: "?", dot + dash * 4: "1", dash + dot + dash: "K",
                      dash + dot + dot: "D",
                      dash + dot * 4: "6", dash + dot * 3 + dash: "=", dash * 3: "O", dot + dash * 2 + dot: "P",
                      dot + dash + dot + dash + dot + dash: ".", dash * 2: "M", dash + dot: "N", dot * 4: "H",
                      dot + dash * 4 + dot: "'", dot * 3 + dash: "V", dash * 2 + dot * 3: "7",
                      dash + dot + dash + dot + dash + dot: ";", dash + dot * 4 + dash: "-",
                      dot * 2 + dash * 2 + dot + dash: "_", dash + dot + dash * 2 + dot + dash: ")",
                      dash + dot + dash + dot + dash * 2: "!", dash * 2 + dot: "G", dash * 2 + dot + dash: "Q",
                      dash * 2 + dot * 2: "Z", dash + dot * 2 + dash + dot: "/", dot + dash + dot + dash + dot: "+",
                      dash + dot + dash + dot: "C", dash * 3 + dot * 3: ":", dash + dot + dash * 2: "Y", dash: "T",
                      dot + dash * 2 + dot + dash + dot: "@", dot * 3 + dash + dot * 2 + dash: "$", dot + dash * 3: "J",
                      dash * 5: "0", dash * 4 + dot: "9", dot + dash + dot * 2 + dash + dot: '"',
                      dash + dot + dash * 2 + dot: "(", dash * 3 + dot * 2: "8", dot * 3 + dash * 2: "3", }

        morseCodeDict = morseCode.split(" ")

        output = []

        for morse in morseCodeDict:
            try:
                output.append(morse_code[morse])
            except:
                if morse == "":
                    output.append(" ")
                else:
                    pass

        output = "".join(output)
        return output.lower()

    def encodeMorse(toEncode, dot='.', dash='-'):
        morse_code = {dot + dash + dot * 3: "&", dash * 2 + dot * 2 + dash * 2: ",", dot * 4 + dash: "4", dot * 5: "5",
                      dot * 5: "5", dot * 3 + dash * 3 + dot * 3: "SOS", dash + dot * 3: "B",
                      dash + dot * 2 + dash: "X",
                      dot + dash + dot: "R", dot + dash * 2: "W", dot * 2 + dash * 3: "2", dot + dash: "A",
                      dot * 2: "I",
                      dot * 2 + dash + dot: "F", dot: "E", dot + dash + dot * 2: "L", dot * 3: "S", dot * 2 + dash: "U",
                      dot * 2 + dash * 2 + dot * 2: "?", dot + dash * 4: "1", dash + dot + dash: "K",
                      dash + dot + dot: "D",
                      dash + dot * 4: "6", dash + dot * 3 + dash: "=", dash * 3: "O", dot + dash * 2 + dot: "P",
                      dot + dash + dot + dash + dot + dash: ".", dash * 2: "M", dash + dot: "N", dot * 4: "H",
                      dot + dash * 4 + dot: "'", dot * 3 + dash: "V", dash * 2 + dot * 3: "7",
                      dash + dot + dash + dot + dash + dot: ";", dash + dot * 4 + dash: "-",
                      dot * 2 + dash * 2 + dot + dash: "_", dash + dot + dash * 2 + dot + dash: ")",
                      dash + dot + dash + dot + dash * 2: "!", dash * 2 + dot: "G", dash * 2 + dot + dash: "Q",
                      dash * 2 + dot * 2: "Z", dash + dot * 2 + dash + dot: "/", dot + dash + dot + dash + dot: "+",
                      dash + dot + dash + dot: "C", dash * 3 + dot * 3: ":", dash + dot + dash * 2: "Y", dash: "T",
                      dot + dash * 2 + dot + dash + dot: "@", dot * 3 + dash + dot * 2 + dash: "$", dot + dash * 3: "J",
                      dash * 5: "0", dash * 4 + dot: "9", dot + dash + dot * 2 + dash + dot: '"',
                      dash + dot + dash * 2 + dot: "(", dash * 3 + dot * 2: "8", dot * 3 + dash * 2: "3", }

        morse_code_inverted = {v: k for k, v in morse_code.items()}

        toEncodeDict = list(toEncode)

        output = []

        for char in toEncodeDict:
            try:
                output.append(morse_code_inverted[char.upper()])
            except:
                if char == " ":
                    output.append(" ")
                else:
                    pass

        return " ".join(output)

    pass
