import os

with open('input.txt', 'r') as f1:
    with open('output.txt', 'a') as f2:
        for line in f1.read():
            f2.write(line)
