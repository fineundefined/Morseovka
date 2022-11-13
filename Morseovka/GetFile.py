class GetFile:
    def GetTextFromTXT(fileName):

        try:
            textFromFile = open(fileName, "r")
            textFromFile = textFromFile.read()

            return textFromFile

        except FileNotFoundError:

            return FileNotFoundError

    pass
