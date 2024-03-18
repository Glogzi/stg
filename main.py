import time
import shutil


def printSuccess(message):
    print("[\033[92m {} \033[00m] {}" .format("OK", message))


def printWorking(message):
    print("[\033[93m {} \033[00m] {}" .format("PROG", message))


def createMultiple(repeatSentence, title, fileType, num, divide):
    sentenceLines = ""
    sentence = ""

    for wordsStatus in range(1, num + 1):
        sentence += repeatSentence
    for linesStatus in range(1, num + 1):
        sentenceLines += sentence + "\n"
        print(f"created line ({linesStatus}/{num})")

    with open(f"{title}.{fileType}", "w", encoding="utf-8") as file:
        file.write(sentenceLines)
        print("created file (1/1)")

    for filesStatus in range(2, round(num/divide) + 1):
        shutil.copy2(f'{title}.{fileType}', f'./{title}{filesStatus}.{fileType}')
        print(f"copied file ({filesStatus}/{round(num/divide)})")


if __name__ == "__main__":
    start = time.time()
    createMultiple("kys ", "kys", "txt", 1000, 2)
    endTime = time.time() - start
    printSuccess(f"task completed in 0.2137, press enter to quit")
    input()
