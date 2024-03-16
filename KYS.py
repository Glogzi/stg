import time
import shutil

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
        print(f"created file (1/1)")

    for filesStatus in range(2, round(num/divide) + 1):
        shutil.copy2(f'{title}.{fileType}', f'./{title}{filesStatus}.{fileType}')
        print(f"copied file ({filesStatus}/{round(num/divide)})")

if __name__ == "__main__":
    start = time.time()
    createMultiple("kys ", "kys", "txt", 1000, 2)
    endTime = time.time() - start
    print(f"task completed in {endTime}, press enter to quit")
    input()