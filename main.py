import time
import shutil


def printSuccess(message):
    print("[\033[92m {} \033[00m] {}" .format("OK", message))


def printError(message):
    print("[\033[91m {} \033[00m] {}" .format("ERR", message))


def copyFiles(fileName, fileType, num):
    for filesNum in range(2, num+1):
        shutil.copy2(f'{fileName}.{fileType}', f'./{fileName}{filesNum}.{fileType}')
        print(f"copied file ({filesNum}/{num})")
        printSuccess(f"Copied {filesNum} file")


def createFiles(repeatSentence, fileName, fileType, lineNumber, fileNumber):
    sentenceLines = ""
    sentence = ""

    for wordsStatus in range(1, lineNumber + 1):
        sentence += repeatSentence
    for linesStatus in range(1, lineNumber + 1):
        sentenceLines += sentence + "\n"
        printSuccess(f"Created line ({linesStatus}/{lineNumber})")

    with open(f"{fileName}.{fileType}", "w", encoding="utf-8") as file:
        file.write(sentenceLines)
        printSuccess("Created 1 file")

    copyFiles(fileName, fileType, fileNumber)


if __name__ == "__main__":
    print("Walcome to STG!")
    repeatSentence = input("Please enter sentence to repeat > ")
    fileName = input("Please enter file name > ")
    fileType = input("Please enter file type (witout the dot) > ")
    lineNumber = int(input("Please enter number of lines in one file > "))
    fileNumber = int(input("Please enter number of files > "))

    start = time.time()
    createFiles(repeatSentence, fileName, fileType, lineNumber, fileNumber)
    endTime = time.time() - start
    printSuccess(f"task completed in {endTime}, press enter to quit")
