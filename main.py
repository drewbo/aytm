from itertools import permutations
import math
import sys
import pickle
import argparse
from termcolor import colored

parser = argparse.ArgumentParser()
parser.add_argument('--use-snapshot', type=str, help='snapshot file input', default=None)
parser.add_argument('--save-snapshot', type=str, help='snapshot file to save', default=None)
args = parser.parse_args()

men = ['Anthony', 'Clinton', 'Dimitri', 'Ethan', 'Joe', 'Kareem', 'Keith', 'Malcolm', 'Michael', 'Shad', 'Tyler']
women = ['Alexis', 'Alivia', 'Audrey', 'Diandra', 'Geles', 'Jada', 'Keyana', 'Nicole', 'Nurys', 'Uche', 'Zoe']

# Match Ceremonies
mcs = [
  { 'order': ['Geles', 'Uche', 'Diandra', 'Jada', 'Zoe', 'Alivia', 'Alexis', 'Nurys', 'Keyana', 'Audrey', 'Nicole'], 'beams': 3 },
  { 'order': ['Diandra', 'Uche', 'Nicole', 'Jada', 'Audrey', 'Alivia', 'Alexis', 'Nurys', 'Keyana', 'Geles', 'Zoe'], 'beams': 1 },
  { 'order': ['Jada', 'Uche', 'Nurys', 'Alexis', 'Zoe', 'Alivia', 'Diandra', 'Geles', 'Audrey', 'Keyana', 'Nicole'], 'beams': 2 },
  { 'order': ['Keyana', 'Uche', 'Alexis', 'Nicole', 'Zoe', 'Diandra', 'Nurys', 'Alivia', 'Geles', 'Audrey', 'Jada'], 'beams': 3 },
  { 'order': ['Nicole', 'Jada', 'Uche', 'Geles', 'Zoe', 'Alivia', 'Alexis', 'Diandra', 'Nurys', 'Audrey', 'Keyana'], 'beams': 1 },
  { 'order': ['Keyana', 'Geles', 'Diandra', 'Jada', 'Alexis', 'Nurys', 'Zoe', 'Alivia', 'Uche', 'Audrey', 'Nicole'], 'beams': 4 }
]

# Truth Booths
truths = [
  { 'man': 'Ethan', 'woman': 'Keyana', 'value': False },
  { 'man': 'Anthony', 'woman': 'Geles', 'value': False },
  { 'man': 'Malcolm', 'woman': 'Nurys', 'value': False },
  { 'man': 'Dimitri', 'woman': 'Nicole', 'value': False },
  { 'man': 'Clinton', 'woman': 'Uche', 'value': False },
  { 'man': 'Keith', 'woman': 'Alexis', 'value': False },
  { 'man': 'Keith', 'woman': 'Alivia', 'value': False }
]

def beams (attempt, correct):
    return sum([1 for i, j in zip(attempt, correct) if i == j])

def truth_check (attempt, correct):
    return (men.index(attempt['man']) == correct.index(attempt['woman'])) == attempt['value']

def possible (wArray):
    ceremonies = all(map(lambda mc: beams(mc['order'], wArray) == mc['beams'], mcs))
    booths = all(map(lambda truth: truth_check(truth, wArray), truths))
    return ceremonies and booths

pairs = [{ 'man': man, 'woman': woman } for man in men for woman in women]
pairs_odds = {}
for pair in pairs:
    if not pairs_odds.get(pair['woman']):
        pairs_odds[pair['woman']] = {}
    pairs_odds[pair['woman']][pair['man']] = 0

if args.use_snapshot:
    possibilities = pickle.load(open(args.use_snapshot, 'rb'))
    p_length = len(possibilities)
else:
    possibilities = permutations(women)
    p_length = math.factorial(len(women))

count = 1
remaining = []
for p in possibilities:
    sys.stdout.write('Possibility %s of %s, %s%% \r' % (count, p_length, round(count / p_length * 100, 2)))
    sys.stdout.flush()
    if possible(p):
        remaining.append(p)
        for index, man in enumerate(men):
            pairs_odds[p[index]][man] += 1
    count += 1

print('')
if args.save_snapshot:
    pickle.dump(remaining, open(args.save_snapshot, 'wb'))

print('Total Possibilities: %s' % p_length)
print('Remaining Possibilities: %s' % len(remaining))

# max output length
mol = len(max(men + women, key=len))
def output (odds):
    num = odds / len(remaining) * 100
    return colored(str(round(num, 2)).rjust(mol, ' '), get_color(num))

def get_color(num):
    if num < 10:
        return 'red'
    if num < 30:
        return 'yellow'
    return 'green'

print('  '.join([''.rjust(mol, ' ')] + [man.rjust(mol, ' ') for man in men]))
for woman in women:
    print('  '.join([woman.rjust(mol, ' ')] + [output(pairs_odds[woman][man]) for man in men]))
