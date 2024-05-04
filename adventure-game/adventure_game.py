import time
import random


def print_and_sleep(text):
    print(text)
    time.sleep(2)


# Function that creates the introduction text before the game
def game_intro_text():
    print_and_sleep("Welcome to this Harry Potter inspired adventure game!")
    print_and_sleep("You are playing as Harry Potter on a quest to defeat "
                    "Voldemort.")
    print_and_sleep("Remember, before you face Voldemort, you need to find "
                    "and destroy all six horcruxes.")


def black_forest_intro_text():
    print_and_sleep("You apparate to the dark forest. It's pitch black.")
    print_and_sleep("You light your wand and proceed, heading in the "
                    "direction of distant sounds.")
    print_and_sleep("You eventually enter a clearing and come face to face"
                    " with Voldemort himself.")


def display_current_horcrux_count(curr_count):
    print_and_sleep(f"You have now found and destroyed {curr_count}/6 "
                    "horcruxes.\n")


def get_found_horcrux(index):
    # Contains all existing horcruxes for Harry to find
    horcruxes_list = [
        "Tom Riddle's Diary",
        "Marvalo Gaunt's Ring",
        "Salazar Slytherin's Locket",
        "Helga Hufflepuff's Cup",
        "Rowena Ravenclaw's Lost Diadem",
        "Nagini"]
    return horcruxes_list[index]


def get_first_game_choice():
    return input("\nIts a brand new day! What would you like to do?\n"
                 "Enter 1 to follow a lead to search for horcruxes.\n"
                 "Enter 2 to go to the dark forest to face Voldemort.\n"
                 "(Please enter 1 or 2)\n")


def get_second_game_choice():
    return input("\nWhat would you like to do next?\n"
                 "Enter 1 to start battle with Voldemport\n"
                 "Enter 2 to apparate back to safety!\n")


def get_play_again_choice():
    return input("\nWoud you like to play again? (y/n)?\n")


def find_horcruxes(found_horcruxes_count):
    new_found_horcruxes_count = found_horcruxes_count
    success_strings = [
        "Great work! You've found ",
        "Amazing! After a lot of planning (that didn't completely pan out) "
        "you've got your hands on ",
        "Well done! With a bit of luck and help from your friends, you've "
        "found "
    ]
    fail_strings = [
        "Well, that lead was a bust. You didn't fix any horcruxes today. "
        "Try again.",
        "That was close, but you didn't manage to get it. Try again!"
    ]

    # Makes it so that there is a ~70% chance of finding a horcrux on a try.
    x = random.randint(1, 10)

    if found_horcruxes_count == 6:
        print_and_sleep("You have already found all horcruxes!")
    elif x > 3:
        new_found_horcruxes_count = found_horcruxes_count+1
        print_and_sleep(random.choice(success_strings)
                        + get_found_horcrux(new_found_horcruxes_count-1))
        display_current_horcrux_count(new_found_horcruxes_count)
    else:
        print_and_sleep(random.choice(fail_strings))
    return new_found_horcruxes_count


def fight_voldemort(found_horcruxes_count):
    if found_horcruxes_count < 6:
        print_and_sleep("You put up a fair fight, but its not enough.")
        print_and_sleep("Unfortunately Voldemort is undefeatable as there"
                        " are still horcruxes out there giving him life.")
        print_and_sleep("You are defeated. You lose the game.")
    elif found_horcruxes_count == 6:
        print_and_sleep("You begin to battle with Voldemort, casting "
                        "Expelliramus! as Voldemort screams 'Avada Kadavra!'")
        print_and_sleep("Moments later.. Voldemort's wands flies into your "
                        "hand.")
        print_and_sleep("Voldemort is defeated! You win!")


def play_again():
    play_again_choice = get_play_again_choice()
    if play_again_choice == 'y':
        print_and_sleep("Excellent! Restarting the game "
                        "...")
    elif play_again_choice == 'n':
        exit(0)
    else:
        print_and_sleep("(Please enter y or n)")


def play_game():
    # Counter for found horcruxes
    found_horcruxes_count = 0
    game_intro_text()
    while True:
        player_choice = get_first_game_choice()
        if player_choice == '1':
            found_horcruxes_count = find_horcruxes(found_horcruxes_count)
        elif player_choice == '2':
            black_forest_intro_text()
            while True:
                player_choice = get_second_game_choice()
                if player_choice == '1':
                    fight_voldemort(found_horcruxes_count)
                    return
                elif player_choice == '2':
                    print_and_sleep("You have apparated back to safety.")
                    break
                else:
                    print_and_sleep("(Please enter 1 or 2)")
        else:
            print_and_sleep("(Please enter 1 or 2)")


def game():
    while True:
        play_game()
        play_again()


game()
