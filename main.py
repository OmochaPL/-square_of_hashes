
''' Please write a function named hash_square(length), which takes an integer argument. 
The function prints out a square of hash characters, and the argument specifies the length of the side of the square. '''


def hash_square(length):
    i = 0
    while i < length :
        print("#" * length)
        i += 1 

# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)
