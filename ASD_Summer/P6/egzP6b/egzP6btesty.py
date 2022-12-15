import sys
from copy import deepcopy
import time
from random import random, randint, seed, shuffle
ALLOWED_TIME = 2

global k_seed
k_seed = 0


class Node:
  def __init__(self, val, parent):
    self.left = None
    self.right = None
    self.parent = parent
    self.key = val
    self.x = None
  
  def __add__(self, other):
    return Node(self.key + other.val, None)

  def __mul__(self, other):
    return NotImplemented

  def __rmul__(self, other):
    return Node(self.key * other, None)

  def __eq__(self, other):
    if type(self) == Node and type(other) == Node:
      return self.key == other.val
    else:
      return False


TEST_SPEC = [
#    n,        	hint
    (0,         3),
    (10,  		  7),
    (20, 		    15),
    (1000, 		  421),
    (10000, 	  4913),
    (100000, 	  42337),
    (200000, 	  78303),
    (300000, 	  116673),
    (400000, 	  146091),
    (99998,     99999)
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


CHESS_SET = ["UL", "UR", "RU", "RD", "DR", "DL", "LD", "LU"]


def gentest(k, hint):
    global k_seed
    tab = []
    if k == 0:
      tab = ["UL", "RD", "LU", "LU", "RD", "DL", "UR", "DR"]
    if k == 99998:
      tab = ["RU" for _ in range(k)]
    else:
      for _ in range(k):
        tab.append(CHESS_SET[randint(0, 7)])
        k_seed += 1
        seed(k_seed)

    return [tab], hint


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

