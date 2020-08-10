#!/usr/bin/env python
# coding=utf-8
"""
    Copyright (C) 2019 * Ltd. All rights reserved.
 
    Editor      : PyCharm
    File name   : reed.py
    Author      : Charles
    Created date: 2020/8/10 10:17 下午
    Description :
       川原秋色静，芦苇晚风鸣
"""
import turtle
import random

stack = []

def createWord(max_it, word, proc_rules, x, y, turn):
    turtle.up()
    turtle.home()
    turtle.goto(x, y)
    turtle.right(turn)
    turtle.down()
    t = 0
    while t < max_it:
        word = rewrite(word, proc_rules)
        drawit(word, 5, 20)
        t = t+1

def rewrite(word, proc_rules):
    wordList = list(word)
    for i in range(len(wordList)):
        curChar = wordList[i]
        if curChar in proc_rules:
            wordList[i] = proc_rules[curChar]
    return "".join(wordList)

def drawit(newWord, d, angle):
    newWordLs = list(newWord)
    for i in range(len(newWordLs)):
        cur_Char = newWordLs[i]
        if cur_Char == 'F':
            turtle.forward(d)
        elif cur_Char == '+':
            turtle.right(angle)
        elif cur_Char == '-':
            turtle.left(angle)
        elif cur_Char == '[':
            state_push()
        elif cur_Char == ']':
            state_pop()

def state_push():
    global stack
    stack.append((turtle.position(), turtle.heading()))

def state_pop():
    global stack
    position, heading = stack.pop()
    turtle.up()
    turtle.goto(position)
    turtle.setheading(heading)
    turtle.down()

def randomStart():
    x = random.randint(-300, 300)
    y = random.randint(-320, -280)
    heading = random.randint(-100, -80)
    return ((x, y), heading)

def main():
    rule_sets = []
    rule_sets.append(((3, 5), 'F', {'F':'F[+F][-F]F'}))
    rule_sets.append(((4, 6), 'B', {'B':'F[-B][+ B]', 'F':'FF'}))
    rule_sets.append(((2, 4), 'F', {'F':'FF+[+F-F-F]-[-F+F+F]'}))
    tree_count = 50
    turtle.tracer(10, 0)
    for x in range(tree_count):
        rand_i = random.randint(0, len(rule_sets) - 1)
        selected_ruleset = rule_sets[rand_i]
        i_range, word, rule = selected_ruleset
        low, high = i_range
        i = random.randint(low, high)
        start_position, start_heading = randomStart()
        start_x, start_y = start_position
        createWord(i, word, rule, start_x, start_y, start_heading)

if __name__ == '__main__': main()