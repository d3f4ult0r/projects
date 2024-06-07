import random
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Guessing game")
    
    # Create subparsers for the modes
    subparsers = parser.add_subparsers(dest='mode', help='Choose mode: computer or user')
    
    # Subparser for computer-mode
    parser_computer = subparsers.add_parser('computer', help='Computer guesses your random number')
    # No additional arguments needed for computer mode

    # Subparser for user-mode
    parser_user = subparsers.add_parser('user', help='User guesses computer\'s random number')
    # No additional arguments needed for user mode

    args = parser.parse_args()

    if args.mode == 'computer':
        computer_guess()
    elif args.mode == 'user':
        user_guess()
    else:
        parser.print_help()

def user_guess():
    print("-------------------------------------------------------------------")
    print("          TRY GUESSING MY PROGRAM'S RANDOM NUMBER")
    print("-------------------------------------------------------------------")
    print("                          Created by d3f4ult0r")
    print("-------------------------------------------------------------------")
    random_number = random.randint(1, 100)
    guess = 0
    tries = 0
    while guess != random_number:
        tries += 1
        guess = int(input("Guess the number: "))
        if guess < random_number:
            print("---guess higher---")
        elif guess > random_number:
            print("---guess lower---")
        else:
            break

    print(f"YOU WON IN {tries} TRIES")

def computer_guess():
    print("-------------------------------------------------------------------")
    print("  THINK OF A RANDOM NUMBER, WATCH MY PROGRAM GUESS IT")
    print("    h for high, l for low, c for correct")
    print("-------------------------------------------------------------------")
    print("                          Created by d3f4ult0r")
    print("-------------------------------------------------------------------")

    low = 1
    high = int(input("What's your upper limit? "))
    tries = 0
    feedback = ''

    try:
        while feedback != 'c':
            tries += 1
            if low != high:
                guess = random.randint(low, high)
            else:
                guess = low

            feedback = input(f"Is {guess} too high or too low? (h/l/c): ")

            if feedback == 'h':
                high = guess - 1
            elif feedback == 'l':
                low = guess + 1
    except ValueError:
        sys.exit("YOU FORGOT YOUR INITIAL RANDOM NUMBER!!!")

    print(f"THE COMPUTER GUESSED YOUR NUMBER IN {tries} TRIES")

if __name__ == "__main__":
    main()