from word_frequency import compute_word_frequency, read_input_file

def main():
    input_file_path = 'data/input.txt'
    input_text = read_input_file(input_file_path)
    word_frequency = compute_word_frequency(input_text)

    print("Word Frequency Analysis:")
    for word, count in word_frequency.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
