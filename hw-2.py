from collections import Counter

lines = 0
words = 0
letters = 0
split_it = []
with open('book.txt', 'r+', encoding='utf8') as f:
    new_book = f.read().replace('Anna Pavlovna')

    f.seek(0)
    f.write(new_book)
    f.truncate()

    f.seek(0)
    for line in f:
        lines += 1
        letters += len(line)
        split_it += line.split()
        pos = True
        for letter in line:
            if letter != ' ' and pos == True:
                words += 1
                pos = False
            elif letter == ' ':
                pos = True

top_longest_words = sorted(set(split_it), key=len)[::-1][:10]
top_most_common_letters = Counter(''.join(split_it)).most_common(10)

print("Lines:", lines)
print("Words:", words)
print("Letters:", letters)
print("AVG_Letter: ", int(letters / words))
print('Top 10 words: ', top_longest_words)
print('Top 10 letters: ', top_most_common_letters)
