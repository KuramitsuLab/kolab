import os
import sys
sys.path.append('..')
import collect_aoj
import kotonoha

l_userId = ['akinobu', 'tefu417', ]
l_problemId = ['1600', 'ITP1_1_A']

def getCode(l_userId, l_problemId):
  for problemId in l_problemId:
    for userId in l_userId:
      print('@@get: ', userId, problemId)
      collect_aoj.download(userId, problemId)

def trans_kotonoha(py_file):
  transpiler = kotonoha.Kotonoha()
  transpiler.load('python3:builtin:random')
  with open(py_file) as f:
    code = transpiler.compile(f.read())
  return code

def trans_download(userId, problemId, py_file):
  os.makedirs(f'data/{problemId}/transKotonoha', exist_ok=True)
  with open(f'data/{problemId}/transKotonoha/{userId}_{problemId}_kotonoha.py', 'w') as f:
    f.write(trans_kotonoha(py_file))

def trans(l_userId, l_problemId):
  for problemId in l_problemId:
    for userId in l_userId:
      trans_download(userId, problemId, f'data/{problemId}/{userId}_{problemId}.py')

if __name__ == '__main__':
  getCode(l_userId, l_problemId)
  trans(l_userId, l_problemId)
