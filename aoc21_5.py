from aocdata import datafile

inpfile = datafile(2021, 99)

def applic(inpstr):
  pass

def irange(start, stop):
  if stop >= start:
    return range(start, stop+1)
  else:
    return range(start, stop-1, -1)

def solve():
  crossings = 0
  with open(inpfile) as inp:
    lines = []
    # (x1, y1),(x2, y2)
    coords = [i.strip().split('->') for i in inp]
    linemap = [[0]*999 for _ in range(1000)]
    #linemap = [[0]*10 for _ in range(10)]
    for n, c in enumerate(coords):
      x1, y1 = [int(a) for a in c[0].strip().split(',')]
      x2, y2 = [int(a) for a in c[1].strip().split(',')]
      if x1 == x2 or y1 == y2:
        for a in irange(y1, y2):
          for b in irange(x1, x2):
            linemap[a][b] += 1

    for y in linemap:
      for x in y:
        if x >= 2:
          crossings += 1
    for l in linemap:
      print(l)
    print(crossings)



if __name__ == '__main__':
  solve()