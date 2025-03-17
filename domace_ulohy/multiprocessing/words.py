import time
import multiprocessing


def remove_white_characters(slovo: str):
    time.sleep(1)
    return slovo.strip()


def rotate(slovo: str):
    time.sleep(1)
    return slovo[::-1]


def change_size(slovo: str):
    time.sleep(1)
    return slovo.swapcase()


def process_word(word):
    return change_size(rotate(remove_white_characters(word)))


if __name__ == "__main__":
    # serial solution
    start_time = time.time_ns()

    with open("words.txt", "r", encoding="utf8") as in_data, open(
        "modified.txt", "w", encoding="utf8"
    ) as out_data:
        for word in in_data:
            word = change_size(rotate(remove_white_characters(word)))
            out_data.write(f"{word}\n")

    end_time = time.time_ns()
    print(f"time in seconds: {(end_time - start_time) / 10 ** 9}")

    # parallel solution
    start_time = time.time_ns()

    with open("words.txt", "r", encoding="utf8") as in_data, open(
        "modified.txt", "w", encoding="utf8"
    ) as out_data:

        pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
        vysledok = pool.map(process_word, in_data)
        for word in vysledok:
            out_data.write(f"{word}\n")

    end_time = time.time_ns()
    print(f"time in seconds: {(end_time - start_time) / 10 ** 9}")
