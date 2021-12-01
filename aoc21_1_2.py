from aocdata import datafile

inpfile = datafile(2021, 1)

dpstore = []
sumstore = []
dpcount = 0

def applic(inpstr):
  global dpcount
  global dpstore
  dpstore.append(inpstr)
  if len(dpstore) > 3:
    del dpstore[0]
  if len(dpstore) > 2:
    sumstore.append(sum(dpstore))
    if len(sumstore) > 2:
      del sumstore[0]
    if len(sumstore) > 1:
      if sumstore[1]-sumstore[0] > 0:
        dpcount += 1
      else:
        print('*', end='')
  print(f'{dpstore} {sumstore} {dpcount}')

def solve():
  with open(inpfile) as inp:
    for i in inp:
      applic(int(i.strip()))


if __name__ == '__main__':
  solve()
  print(dpcount)