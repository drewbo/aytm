from itertools import permutations
import math
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--people', type=int, help='people', default=3)
args = parser.parse_args()

people = range(args.people)

def beams (attempt, correct):
    return sum([1 for i, j in zip(attempt, correct) if i == j])

def possible (wArray):
    return beams(people, wArray) < 1

possibilities = permutations(people)
p_length = math.factorial(len(people))

count = 1
good = 0
for p in possibilities:
    sys.stdout.write('Possibility %s of %s, %s%% \r' % (count, p_length, round(count / p_length * 100, 2)))
    sys.stdout.flush()
    if possible(p):
        good += 1
    count += 1

print('')

print('Total Possibilities: %s' % p_length)
print('Remaining Possibilities: %s' % good)
print('Likelihood of no self-matching: %s' % round(good / p_length * 100, 2))
