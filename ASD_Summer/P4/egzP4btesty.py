import sys
from copy import deepcopy
import time
from random import random, randint, seed, shuffle
ALLOWED_TIME = 0.02

global k_seed
k_seed = 0


class Node:
  def __init__(self, key, parent):
    self.left = None
    self.right = None
    self.parent = parent
    self.key = key
    self.x = None
  
  def __add__(self, other):
    return Node(self.key + other.key, None)

  def __mul__(self, other):
    return NotImplemented

  def __rmul__(self, other):
    return Node(self.key * other, None)

  def __eq__(self, other):
    if type(self) == Node and type(other) == Node:
      return self.key == other.key
    else:
      return False


TEST_SPEC = [
    #n (wierzcholki), q (len(T)), hint (wynik)
    (0,               5,          16),
    (15,              9,          0),
    (25,              14,        -45),
    (100,             69,         5),
    (400,             54,        -1664),
    (700,             77,         1458),
    (1000,            191,       -13284),
    (300000,          69,         2378996),
    (300000,          21,         318031),
    (300000,          37,        -825364),
]


def randint_seed(a, b):
  global k_seed
  output = randint(a, b)
  k_seed += 1
  seed(k_seed)
  return output


def randnode_seed(root, a, b):
  global k_seed
  k_seed += 1
  seed(k_seed)
  if not root:
    root = Node(randint(a, b))
  else:
    if randint(0, 1):
      root.left = randnode_seed(root.left, a, b)
    else:
      root.right = randnode_seed(root.right, a, b)
  return root


def node_add(root, node):
  if root.key > node.key:
    if not root.left:
      root.left = node
      node.parent = root
    else:
      node_add(root.left, node)
  else:
    if not root.right:
      root.right = node
      node.parent = root
    else:
      node_add(root.right, node)


def gentest(n, q, hint):
    root = None
    T = None
    if n == 0:
      e11 = Node(11, None)

      e5 = Node(5, e11)
      e11.left = e5
      
      e15 = Node(15, e11)
      e11.right = e15
      
      e3 = Node(3, e5)
      e5.left = e3
      
      e8 = Node(8, e5)
      e5.right = e8
      
      e12 = Node(12, e15)
      e15.left = e12
      
      e7 = Node(7, e8)
      e8.left = e7
      
      e10 = Node(10, e8)
      e8.right = e10
      
      root = e11
      T = [e5, e7, e8, e11, e12]

    else:
      X = [randint_seed(-3 * n, 3 * n) for _ in range(n)]
      X = list(dict.fromkeys(X))

      Y = []
      for el in X:
        Y.append(Node(el, None))

      root = Y[len(Y) // 2]
      for i in range(len(Y)):
        if i != len(Y) // 2:
          node_add(root, Y[i])

      Y = sorted(Y, key=lambda x: x.key)
      Y = Y[1:-1]
      shuffle(Y)
      T = [Y[i] for i in range(q)]


    return [root, T], hint


RERAISE = True

def print_err(*a):
    print(*a, file = sys.stderr)
 
# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

def limit(L, lim = 120):
    x = str(L)
    if len(x) < lim:
        return x
    else:
        return x[:lim]+"[za dlugie]..."

class TimeOut(Exception):
  def __init__(self):
    pass

def internal_runtests( copyarg, printhint, printsol, check, generate_tests, all_tests, f, ACC_TIME ):
  seed(0)
  passed, timeout, answer, exception = 0, 0, 0, 0

  print("Generowanie testów. Proszę czekać...")
  print("(!) To może zająć kilka sekund...")

  if all_tests == False:
    TESTS = generate_tests(3)
  else:
    TESTS = generate_tests(100)

  # A - Accepted
  # T - Timeout
  # W - Wrong Answer
  # E - Exception when solving
  # O - Terminated by operator
  status_line = ''

  total  = len(TESTS)
  total_time = 0
  for i,d in enumerate(TESTS):
    print("-----------------")
    print("Test", i )
    arg  = copyarg(d["arg"])
    hint = deepcopy(d["hint"])
    printhint( hint )
    try:
      time_s = time.time()
      sol    = f(*arg)
      printsol(sol)
      time_e = time.time()
      res = check(hint, sol)
      if ACC_TIME > 0 and float(time_e-time_s) > ACC_TIME:
        timeout += 1
        status_line += ' T'
        print("!!!!!!!! PRZEKROCZONY DOPUSZCZALNY CZAS")
      elif res:
        passed += 1
        status_line += ' A'
        print("Test zaliczony!")
      else:
        answer += 1
        status_line += ' W'
        print("TEST NIEZALICZONY!!!")
      print("Orientacyjny czas: %.2f sek." % float(time_e-time_s))
        
      total_time += float(time_e-time_s)

    except TimeOut:
      timeout += 1
      status_line += ' T'
      print("!!!!!!!! PRZEKROCZONY DOPUSZCZALNY CZAS")
    except KeyboardInterrupt:
      exception += 1
      status_line += ' O'
      print("Obliczenia przerwane przez operatora")
    except Exception as e:
      exception += 1
      status_line += ' E'
      print("WYJATEK:", e)
      if RERAISE: raise e

  print("-----------------")
  print("Liczba zaliczonych testów: %d/%d" % (passed,total))
  print("Liczba testów z przekroczonym czasem: %d/%d" % (timeout,total))
  print("Liczba testów z błędnym wynikiem: %d/%d" % (answer,total))
  print("Liczba testów zakończonych wyjątkiem: %d/%d" % (exception,total))
  print("Orientacyjny łączny czas : %.2f sek." % total_time)
  print("Status testów:%s" % status_line)

def copyarg(arg):
    return deepcopy(arg)

def printhint(hint):
    print("Oczekiwany wynik: ", hint)

def printsol(sol):
    print("Otrzymany wynik:  ", sol)

def check(hint, sol):
    return hint == sol
    
def generate_tests(num_tests = None):
    global TEST_SPEC
    TESTS = []

    if num_tests is not None:
        TEST_SPEC = TEST_SPEC[:num_tests]

    for spec in TEST_SPEC:
        newtest = {}
        arg, hint = gentest(*spec)
        newtest["arg"] = arg
        newtest["hint"] = hint
        TESTS.append(newtest)
              
    return TESTS
 
def runtests(f, all_tests = 3):
    internal_runtests( copyarg, printhint, printsol, check, generate_tests, all_tests, f, ALLOWED_TIME )

