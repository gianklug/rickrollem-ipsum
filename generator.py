#!/usr/bin/python3

import sys 

def main():
    # Read the lorem ipsum text
    with open('lorem.txt', 'r') as f:
        lorem_ipsum = f.read()
    # Split the text into words
    words = lorem_ipsum.split()
    # Get the amount of requested words
    amount = sys.argv[1]
    # Add additional words to the list
    if int(amount) > len(words):
        words.append(words*int(amount/len(words)))
    # Print the requested amount of words
    output = ""
    for i in range(int(amount)):
        output += words[i] + " "
    # Format the output
    if output[-1] != ".":
        output = list(output)
        output[-1] = "."
        output = "".join(output)
    # Print the output
    print(output)
        
    

if __name__ == "__main__":
    main()