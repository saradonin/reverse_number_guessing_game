def guess():
    min = 0
    max = 1000
    print("""Let's play a game. 
      """)
    count = 0
    while True:
        guess = int((max - min) / 2 + min)
        count += 1  # to jest tymczasowy pomocnik
        print(f"My guess is: {guess} ({count}.try)")

        print("Did I guess? [y/n]")
        answer_1 = input().lower()

        if answer_1 == 'y':
            return "I won!"
        elif answer_1 == 'n':
            print("Too big? [y/n]")
            answer_2 = input().lower()

            if answer_2 == 'y':
                max = guess
            elif answer_2 == 'n':
                print("Too small? [y/n]")
                answer_3 = input().lower()

                if answer_3 == 'y':
                    min = guess
                elif answer_3 == 'n':
                    print("Don't cheat!")
                else:
                    print("Please answer with: 'y' for Yes or 'n' for No")
            else:
                print("Please answer with: 'y' for Yes or 'n' for No")
        else:
            print("Please answer with: 'y' for Yes or 'n' for No")

print(guess())
