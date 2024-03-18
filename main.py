import time
import shutil


def printSuccess(message):
    print("[\033[92m {} \033[00m] {}" .format("OK", message))


def printWorking(message):
    print("[\033[93m {} \033[00m] {}" .format("PROG", message))


def printError(message):
    print("[\033[91m {} \033[00m] {}" .format("ERR", message))


def copyFiles(fileName, fileType, num):
    for filesNum in range(2, num+1):
        printWorking(f"Coping {filesNum} file")
        shutil.copy2(f'{fileName}.{fileType}', f'./{fileName}{filesNum}.{fileType}')
        print(f"copied file ({filesNum}/{num})")
        printSuccess(f"Copied {filesNum} file")


def createFile(repeatSentence, fileName, fileType, num):
    sentenceLines = ""
    sentence = ""

    printWorking("Creating 1st file")
    for wordsStatus in range(1, num + 1):
        sentence += repeatSentence
    for linesStatus in range(1, num + 1):
        sentenceLines += sentence + "\n"
        printSuccess(f"Created line ({num}/{linesStatus})")

    with open(f"{fileName}.{fileType}", "w", encoding="utf-8") as file:
        file.write(sentenceLines)
        printSuccess("Created 1 file")

    copyFiles(fileName, fileType, num)


if __name__ == "__main__":
    start = time.time()
    createFile("kys ", "kys", "txt", 10)
    endTime = time.time() - start
    printSuccess(f"task completed in {endTime}, press enter to quit")
