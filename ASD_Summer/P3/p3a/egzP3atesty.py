import sys
from copy import deepcopy
import time
from random import random, randint, seed, shuffle
from math import sqrt
ALLOWED_TIME = 1

class Node:
  def __init__(self, wyborcy, koszt, fundusze):
    self.next = None
    self.wyborcy = wyborcy 
    self.koszt = koszt 
    self.fundusze = fundusze 
    self.x = None

global k_seed
k_seed = 0

TEST_SPEC = [
    #m (wybory), n (okręgi), q (koszt kampanii),w (wynik)
    (0,          5,          50,                18),     
    (10,         20,         20,                2944),     
    (10,         50,         50,                8696),     
    (20,         50,         100,               19008), 
    (30,         50,         100,               27318), 
    (35,         100,        150,               79592),
    (40,         120,        160,               120690),
    (45,         140,        170,               167864),
    (50,         160,        125,               201772),
    (55,         180,        100,               256812) 
]

def f(x):
    global k_seed
    k_seed += 1
    seed(k_seed)
    return round(sqrt(x ** 2 * random()))

def gentest(m, n, q, hint):
    if m == 0:
      wyb1okr1 = Node(3, 8, 15)
      wyb1okr2 = Node(2, 7, 15)
      wyb1okr3 = Node(4, 5, 15)
      wyb1okr1.next = wyb1okr2
      wyb1okr2.next = wyb1okr3
      wyb2okr1 = Node(4, 7, 8)	
      wyb2okr2 = Node(5, 2, 8)
      wyb2okr1.next = wyb2okr2
      wyb3okr1 = Node(3, 5, 10)
      wyb3okr2 = Node(3, 5, 10)
      wyb3okr1.next = wyb3okr2
      T = [wyb1okr1, wyb2okr1, wyb3okr1]
      return T, 18


    global k_seed
    T = [None for _ in range(m)]

    for i in range(m):
      k_seed += 1 
      seed(k_seed)
      x = randint(1, n*2)
      k_seed += 1 
      seed(k_seed)
      y = randint(q//25+1, q//5)
      startNode = Node(x, y, q)
      p = startNode
      for j in range(n-1):
        k_seed += 1 
        seed(k_seed)
        x = randint(1, n*2)
        k_seed += 1 
        seed(k_seed)
        y = randint(q//25+1, q//5)
        newNode = Node(x, y, q)
        p.next = newNode 
        p = p.next 
      T[i] = startNode

    return T, hint

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
       
def timeout_handler(signum, frame):
   raise TimeOut()

def internal_runtests( copyarg, printhint, printsol, check, generate_tests, all_tests, f, ACC_TIME ):
  passed, timeout, answer, exception = 0, 0, 0, 0

  print("Generowanie testów. Proszę czekać...")
  print("(!) To może zająć kilka sekund...")

  if all_tests == False:
    TESTS = generate_tests(3)
  else:
    TESTS = generate_tests(10)

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
      sol    = f(arg)
      time_e = time.time()
      
      printsol( sol )
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
    print("Oczekiwany wynik: ", round(hint, 4))

def printsol(sol):
    print("Otrzymany wynik : ", round(sol, 4))

def check(hint, sol):
    return abs(hint - sol) < 0.01
    
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

