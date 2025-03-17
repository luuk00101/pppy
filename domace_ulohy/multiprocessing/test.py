import multiprocessing
from multiprocessing import Pool, Queue
import time


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


def read_file(q):
    with open("words.txt", "r", encoding="utf8") as f:
        for line in f:
            q.put(line)
    q.put(None)  # Signal that the file has been fully read


def write_file(q):
    with open("modified.txt", "w", encoding="utf8") as f:
        while True:
            line = q.get()
            if line is None:  # Check if the file has been fully written
                return
            f.write(line)


def process_data(input_q, output_q):
    while True:
        line = input_q.get()
        if line is None:
            output_q.put(None)
            return
        output_q.put(process_word(line))


def main():
    start_time = time.time_ns()

    input_q = Queue()
    output_q = Queue()

    pocet_jadier = 4

    read_process = multiprocessing.Process(target=read_file, args=(input_q,))
    read_process.start()

    procesy = []
    for i in range(pocet_jadier):
        proces = multiprocessing.Process(target=process_data, args=(input_q, output_q))
        proces.start()
        procesy.append(proces)

    write_process = multiprocessing.Process(target=write_file, args=(output_q,))
    write_process.start()

    read_process.join()
    read_process.close()

    for proces in procesy:
        proces.join()
    for proces in procesy:
        proces.close()

    write_process.join()
    write_process.close()

    end_time = time.time_ns()
    print(f"time in seconds: {(end_time - start_time) / 10 ** 9}")


if __name__ == "__main__":
    main()
