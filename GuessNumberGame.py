#!/usr/local/bin/python2.7


import random


def play_game(num):
    while True:
        a = int(raw_input("please input a number:"))
        if a > num:
            print "The number is bigger"
        elif a < num:
            print "The number is zsmaller"
        else:
            print "You are right!"
            break


def if_continue():
    num = random.randint(0, 99)
    while True:
        c = raw_input("Do you want to play the game once more,please input Y/N:")
        if c == "Y":
            play_game(num)
        elif c == "N":
            print "Thank you for playing this game, GoodBye!"
            break
        else:
            print "The input is not correct, Please input Y/N only!"


def main():
    print "----------begin game-----------"
    num = random.randint(0, 99)
    play_game(num)
    if_continue()


if __name__ == '__main__':
    main()

