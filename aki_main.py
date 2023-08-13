from akinator import (
    CantGoBackAnyFurther,
    InvalidAnswer,
    Akinator,
    Answer,
    Theme,
)
print("#  Welcome to the Guess who, \n#  Warning: This game can read and blow yor mind. \n#  Play at your own risk!!!\n\n")

def star():
    start = input("Are you ready to go forward(yes/no): ")
    if start == 'yes':
        print("OK, it's your choice,")
        theme = int(input("\nSelect the theme between Characters, Animals or Objects (1,2,3): "))
        if theme == 1:
            thm = 'Characters'
            print("You have choosen characters, Guess any one character and answer wisely, ")
            chs = input("Selected your character? (y/n): ")
        elif theme == 2:
            thm = 'Animals'
            print("You have choosen animals, Guess any one animal and answer wisely, ")
            chs = input("Selected your animals? (y/n): ")
        elif theme == 3:
            thm = 'Objects'
            print("You have choosen objects, Guess any one object and answer wisely, ")
            chs = input("Selected your objects? (y/n): ")
        else:
            print("Please select from correct options.")
            star()
        aki = Akinator(
            child_mode = True,
            theme = Theme.from_str(thm),
        )
        first_question = aki.start_game()
        print(first_question)
        answer = str(input("=> "))

        while aki.progression <= 80:
            if answer == 'back':
                # It will try to go back, if it false then the output will be expect one
                try:
                    aki.back()
                    print('went back 1 question')
                except CantGoBackAnyFurther:
                    print('cannot go back any further!')
            else:
                try:
                    answer = Answer.from_str(answer)
                except InvalidAnswer:
                    print('Invalid answer')
                else:
                    aki.answer(answer)
            answer = input(f'{aki.question}: ')
        first_guess = aki.win()
        if first_guess:
            # print out its first guess's details
            print('name:', first_guess.name)
            print('desc:', first_guess.description)
            print('image:', first_guess.absolute_picture_path)
        
    elif start == 'no':
        print("You are scared, LMAO")
    else:
        print("Please select from correct options.")
        star()
star()