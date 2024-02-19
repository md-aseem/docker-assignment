import os
import socket
from collections import Counter

def list_text_files(directory):
    try:
        return [f for f in os.listdir(directory) if f.endswith('.txt')]
    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")
        return []
    except OSError as e:
        print(f"Error accessing directory '{directory}': {e}")
        return []

def count_words_in_file(filepath):
    try:
        with open(filepath, 'r') as file:
            text = file.read()
        return len(text.split())
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return 0
    except OSError as e:
        print(f"Error reading file '{filepath}': {e}")
        return 0

def find_top_words(filepath, top_n=3):
    try:
        with open(filepath, 'r') as file:
            words = file.read().lower().split()
        word_counts = Counter(words)
        return word_counts.most_common(top_n)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return []
    except OSError as e:
        print(f"Error reading file '{filepath}': {e}")
        return []

def get_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except OSError as e:
        print("Error getting IP address:", e)
        return "Unknown IP"

def main():
    data_dir = '/home/data'
    output_dir = '/home/output'
    output_file = 'result.txt'

    try:
        file_list = list_text_files(data_dir)
        word_counts = {}

        for file in file_list:
            filepath = os.path.join(data_dir, file)
            word_counts[file] = count_words_in_file(filepath)

        grand_total = sum(word_counts.values())
        top_words = find_top_words(os.path.join(data_dir, 'IF.txt'))
        ip_address = get_ip_address()

        with open(os.path.join(output_dir, output_file), 'w') as output:
            output.write("List of text files: " + ", ".join(file_list) + "\n")
            for file, count in word_counts.items():
                output.write(f"Total words in {file}: {count}\n")
            output.write(f"Grand total of words: {grand_total}\n")
            output.write("Top 3 words in IF.txt:\n")
            for word, count in top_words:
                output.write(f"'{word}': {count}\n")
            output.write(f"IP Address: {ip_address}\n")

        with open(os.path.join(output_dir, output_file), 'r') as result:
            print(result.read())

    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    main()
