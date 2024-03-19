import time
import shutil


def print_success(message):
    print("[\033[92m {} \033[00m] {}" .format("OK", message))


def print_error(message):
    print("[\033[91m {} \033[00m] {}" .format("ERR", message))


def copy_files(base_file_name, file_type, num_copies):
    for file_num in range(2, num_copies + 1):
        shutil.copy2(f'{base_file_name}.{file_type}', f'./{base_file_name}{file_num}.{file_type}')
        print(f"Copied file ({file_num}/{num_copies})")
        print_success(f"Copied {file_num} file")


def create_files(repeat_sentence, file_name, file_type, num_lines, num_files):
    sentence_lines = ""
    sentence = ""

    for word_status in range(1, num_lines + 1):
        sentence += repeat_sentence

    for line_status in range(1, num_lines + 1):
        sentence_lines += sentence + "\n"
        print_success(f"Created line ({line_status}/{num_lines})")

    with open(f"{file_name}.{file_type}", "w", encoding="utf-8") as file:
        file.write(sentence_lines)
        print_success("Created 1 file")

    copy_files(file_name, file_type, num_files)


if __name__ == "__main__":
    print("Welcome to STG!")
    repeat_sentence = input("Please enter sentence to repeat > ")
    file_name = input("Please enter base file name > ")
    file_type = input("Please enter file type (without the dot) > ")
    num_lines = int(input("Please enter number of lines in one file > "))
    num_files = int(input("Please enter number of files > "))

    start_time = time.time()
    create_files(repeat_sentence, file_name, file_type, num_lines, num_files)
    end_time = time.time() - start_time
    print_success(f"Task completed in {end_time}, press enter to quit")

