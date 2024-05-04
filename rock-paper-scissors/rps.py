#!/usr/bin/env python3

import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self, name):
        self.name = name

    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass


class Rock(Player):
    def move(self):
        return 'rock'


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.next_move = random.choice(moves)  # Initial move is random

    def learn(self, my_move, their_move):
        self.next_move = their_move

    def move(self):
        return self.next_move


class CyclePlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.next_move = random.choice(moves)  # Initial move is random

    def learn(self, my_move, their_move):
        if my_move == 'paper':
            self.next_move = 'scissors'
        elif my_move == 'rock':
            self.next_move = 'paper'
        elif my_move == 'scissors':
            self.next_move = 'rock'

    def move(self):
        return self.next_move


class HumanPlayer(Player):
    def move(self):
        while True:
            choice = input("\tWhat's your move? Enter rock/paper/scissors:")
            if choice in moves:
                return choice
            else:
                print("\tThat's not a valid move. Try again.")


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, rounds_choice, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.num_rounds = int(rounds_choice)
        self.score = {self.p1.name: 0, self.p2.name: 0}

    def display_score(self):
        print(f"\tScore -> {self.p1.name}: {self.score[self.p1.name]}",
              f"{self.p2.name}: {self.score[self.p2.name]}")

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"\t{self.p1.name}: {move1}  {self.p2.name}: {move2}")
        if move1 == move2:
            print(f"\t** It's a tie! **")
            self.score[self.p1.name] += 1
            self.score[self.p2.name] += 1
            self.display_score()
        elif beats(move1, move2):
            print(f"\t** {self.p1.name} wins! **")
            self.score[self.p1.name] += 1
            self.display_score()
        else:
            print(f"\t** {self.p2.name} wins! **")
            self.score[self.p2.name] += 1
            self.display_score()

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(self.num_rounds):
            print(f"Round {round+1}:")
            self.play_round()
        if self.score[self.p1.name] == self.score[self.p2.name]:
            print(f"Game over! It's a tie.")
        elif self.score[self.p1.name] > self.score[self.p2.name]:
            print(f"Game over! Winner is {self.p1.name}")
        else:
            print(f"Game over! Winner is {self.p2.name}")
        self.display_score()


if __name__ == '__main__':
    rounds_choice = input("How many rounds would you like to play? ")
    game = Game(
        rounds_choice,
        random.choice([
            ReflectPlayer('Computer'),
            CyclePlayer('Computer'),
            RandomPlayer('Computer'),
            Rock('Computer')
        ]),
        HumanPlayer('Player')
    )
    game.play_game()
