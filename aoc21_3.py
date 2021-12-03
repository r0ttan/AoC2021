from aocdata import datafile

inpfile = datafile(2021, 3)
dr = []

def applic(inpstr):
  global dr
  for n, i in enumerate(inpstr):
    if len(dr) < len(inpstr):
      dr.append(int(i))
    else:
      dr[n] += int(i)

def solve():
  inplen = 0
  gamma = 0
  epsilon = 0
  with open(inpfile) as inp:
    for i in inp:
      inplen += 1
      applic(i.strip())

  res = [1 if dr[n] > inplen/2 else 0 for n, d in enumerate(dr)]
  gamma = int(''.join(str(r) for r in res), 2)
  res = [1 if dr[n] <= inplen/2 else 0 for n, d in enumerate(dr)]
  epsilon = int(''.join(str(r) for r in res), 2)
  print(gamma*epsilon)


if __name__ == '__main__':
  solve()