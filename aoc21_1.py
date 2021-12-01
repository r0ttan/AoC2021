from aocdata import datafile

inpfile = datafile(2021, 1)

dpstore = []
dpcount = 0

def applic(inpstr):
  global dpcount
  global dpstore
  dpstore.append(inpstr)
  if len(dpstore) > 1:
    if int(dpstore[1])-int(dpstore[0]) > 0:
      dpcount += 1
    #else:
    #  print('*', end='')
  if len(dpstore) > 2:
    del dpstore[0]
  #print(f'{dpstore} {dpcount}')

def solve():
  with open(inpfile) as inp:
    for i in inp:
      applic(i.strip())


if __name__ == '__main__':
  solve()
  print(dpcount)
