secret_word = "12"
guess = ""
# guess_count = 5
# guess_limit = 10
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
        if guess != secret_word:
            # print("wrong!, guess left: ", guess_count)
            print("wrong!")
        elif guess == secret_word:
            print("true")
    else:
        out_of_guesses = True


if out_of_guesses:
    print("Out of guessess, YOU LOSE!")
else:
    print("You win!")
