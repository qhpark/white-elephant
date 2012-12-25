#!/usr/bin/env python

import random

participants = [ 'Dongchul', 'Daniel', 'Q-Ha', 'Alex', 'SM', 'Lawrence', 'BK', 'Serim', 'Clara', 'Julia', ]

def main():
    selected = [False,] * len(participants);

    remaining = len(participants)
    while True:
        t = random.randint(0,len(participants) - 1)
        if not selected[t]:
            print participants[t]
            selected[t] = True
            remaining -= 1
            if remaining == 0:
                break;
            dummy = raw_input()
    
if __name__ == "__main__":
    main()
