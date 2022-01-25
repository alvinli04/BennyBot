from __future__ import division, print_function
import os
import random
import math
from itertools import permutations, combinations, product, chain, zip_longest
from collections import deque, defaultdict
from pprint import pprint as pp
from fractions import Fraction as F
import ast, re, sys
import discord
from discord.ext import commands

def solve24(digits):
    """\
    >>> for digits in '3246 4788 1111 123456 1127 3838'.split():
            solve(list(digits))


    Solution found: 2 + 3 * 6 + 4
    '2 + 3 * 6 + 4'
    Solution found: ( 4 + 7 - 8 ) * 8
    '( 4 + 7 - 8 ) * 8'
    No solution found for: 1 1 1 1
    '!'
    Solution found: 1 + 2 + 3 * ( 4 + 5 ) - 6
    '1 + 2 + 3 * ( 4 + 5 ) - 6'
    Solution found: ( 1 + 2 ) * ( 1 + 7 )
    '( 1 + 2 ) * ( 1 + 7 )'
    Solution found: 8 / ( 3 - 8 / 3 )
    '8 / ( 3 - 8 / 3 )'
    >>> """
    digilen = len(digits)
    # length of an exp without brackets
    exprlen = 2 * digilen - 1
    # permute all the digits
    digiperm = sorted(set(permutations(digits)))
    # All the possible operator combinations
    opcomb   = list(product('+-*/', repeat=digilen-1))
    # All the bracket insertion points:
    brackets = ( [()] + [(x,y)
                         for x in range(0, exprlen, 2)
                         for y in range(x+4, exprlen+2, 2)
                         if (x,y) != (0,exprlen+1)]
                 + [(0, 3+1, 4+2, 7+3)] ) # double brackets case
    for d in digiperm:
        for ops in opcomb:
            if '/' in ops:
                d2 = [('F(%s)' % i) for i in d] # Use Fractions for accuracy
            else:
                d2 = d
            ex = list(chain.from_iterable(zip_longest(d2, ops, fillvalue='')))
            for b in brackets:
                exp = ex[::]
                for insertpoint, bracket in zip(b, '()'*(len(b)//2)):
                    exp.insert(insertpoint, bracket)
                txt = ''.join(exp)
                try:
                    num = eval(txt)
                except ZeroDivisionError:
                    continue
                if num == 24:
                    if '/' in ops:
                        exp = [ (term if not term.startswith('F(') else term[2])
                               for term in exp ]
                    ans = ' '.join(exp).rstrip()
                    return ans
    return 'No solution found.'


# Fas Fax stuff
class FFGame:
    def __init__(self, teams):
        self.teams = teams
        self.scoreboard = defaultdict(lambda:0)
    
    def score(self, player, correct):
        for i in range(len(self.teams)):
            if player in self.teams[i]:
                if correct:
                    self.scoreboard[i] += 2
                else:
                    self.scoreboard[i] -= 1
                break

    def get_teams(self):
        return self.teams
    def get_scoreboard(self):
        return self.scoreboard


def main():
    teams = [['a', 'b'], ['c','d']]
    fg = FFGame(teams)
    fg.score('a', True)
    print(fg.get_teams())
    print(fg.get_scoreboard()[0])

if __name__ == '__main__':
    main()
