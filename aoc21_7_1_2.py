from aocdata import datafile

inpfile = datafile(2021, 7)

def applic(inpstr):
  pass

def solve():
  with open(inpfile) as inp:
    for i in inp:
      crpos = [int(c) for c in i.strip().split(',')]
      fuelcons = [0 for _ in range(max(crpos)+1)]
  for n, p in enumerate(fuelcons):
    for c in crpos:
      tdist = [n, c]
      fuelcons[n] += max(tdist) - min(tdist)  # part1
      #fuelcons[n] += sum([s for s in range(0, (max(tdist) - min(tdist))+1)])   #part2
  print(min(fuelcons))



if __name__ == '__main__':
  solve()