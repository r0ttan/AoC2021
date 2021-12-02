from aocdata import datafile
from collections import defaultdict
inpfile = datafile(2021, 2)

pos = defaultdict(int)
#pos = {}
aim = 0

def applic(inpstr):
  global pos, aim
  k, v = inpstr.split()
  if k == 'up':
    aim -= int(v)
  elif k == 'down':
    aim += int(v)
  else:
    pos[k] = int(v) + pos[k]
    pos['depth'] = int(v)*aim + pos['depth']

def solve():
  with open(inpfile) as inp:
    for i in inp:
      applic(i)
  sumpos = pos['forward'] * pos['depth']
  print(sumpos)



if __name__ == '__main__':
  solve()