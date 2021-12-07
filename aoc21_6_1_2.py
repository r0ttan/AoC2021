from aocdata import datafile

inpfile = datafile(2021, 6)


def solve():
  with open(inpfile) as inp:
    for i in inp:
      school = [int(u) for u in i.strip().split(',')]
  zum = [0,0,0,0,0,0,0,0,0]
  for s in school:
    zum[s] += 1
  tmpf = 0
  for _ in range(256):
    for n, z in enumerate(zum):
      if n == 0:
        tmpf = z #tmpf = zum[n]
        zum[n] = zum[n+1]
      elif n < 8:
        zum[n] = zum[n+1]
      else:
        zum[n] = tmpf
        zum[6] += tmpf
  print(sum(zum))


if __name__ == '__main__':
  solve()