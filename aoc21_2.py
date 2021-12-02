from aocdata import datafile
from collections import defaultdict
inpfile = datafile(2021, 2)

pos = defaultdict(int)
#pos = {}

def applic(inpstr):
  global pos
  k, v = inpstr.split()
  pos[k] = int(v) + int(pos[k])


def solve():
  with open(inpfile) as inp:
    for i in inp:
      applic(i)
  sumpos = int(pos['forward']) * (int(pos['down'])-int(pos['up']))
  print(sumpos)



if __name__ == '__main__':
  solve()