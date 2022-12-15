from math import inf, sqrt
import sys
from copy import deepcopy
import time
from random import random, randint, seed, shuffle
ALLOWED_TIME = 60

global k_seed
k_seed = 0

class Array():
  __ERROR = -1

  def __init__(self, n):
    self.n = n
    self.__tab = [0 for _ in range(n)]
    self.__cost = 0

  def set(self, index, val):
    if index >= self.n:
      return Array.__ERROR
    self.__cost += 0.001
    self.__tab[index] = val

  def get(self, index):
    if index >= self.n:
      return Array.__ERROR
    self.__cost += 0.001
    return self.__tab[index]

  def __str__(self):  
    return str(limit(self.__tab))

  def get_cost(self):
    return self.__cost

  def get_sum(self):
    return sum(self.__tab)


TEST_SPEC = [
#    n,         m,        op_lim,    hint,    check
    (8,         4,        10,       36,        0),
    (2 ** 4,    100,      10,       66869,     0.1),
    (2 ** 4,    200,      10,       309194,    0.1),
    (2 ** 13,   1000,     200,      5047683,   1),
    (2 ** 13,   1000,     200,      4904185,   1),
    (2 ** 13,   1000,     200,      5189174,   1),
    (2 ** 16,   1000,     50,       5110353,   5),
    (2 ** 16,   1000,     50,       5076657,   5),
    (2 ** 16,   1000,     50,       4727424,   5),
    (2 ** 14,   1000,     50,       5449424,   5),
]


def randint_seed(a, b):
  global k_seed
  output = randint(a, b)
  k_seed += 1
  seed(k_seed)
  return output


def gentest(n, m, op_lim, hint, check):
    global k_seed
    T = None
    Q = None
    r = 0
    if n == 8:
      r = n
      T = Array(n)
      Q = [
        (0, 0, 14),
        (1, 0, 3),
        (0, 3, 22),
        (1, 2, 3)]
    else:
      T = Array(n)
      Q = []
      r = n // 2 - 1
      if n == 2 ** 14:
        r = round(2 * r - 4 * sqrt(r))
        n = r
      for _ in range(m):
        if randint_seed(0, 1):
          a, b = randint_seed(0, r), randint_seed(0, r)
          Q.append((1, min(a, b), max(a, b)))
        else:
          index, val = randint_seed(0, r), randint_seed(0, 255)
          Q.append((0, index, val))
    
    return [T, T.n, Q, n], hint, op_lim, check


RERAISE = True

def print_err(*a):
    print(*a, file = sys.stderr)
 
# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

def limit(L, lim = 80):
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
  expensive, asd_avoid = 0, 0

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
  points = 0
  sqrt = False
  logn = False
  total  = len(TESTS)
  total_time = 0
  for i,d in enumerate(TESTS):
    print("-----------------")
    print("Test", i )
    arg  = copyarg(d["arg"])
    hint = deepcopy(d["hint"])
    op_lim = deepcopy(d["op_lim"])
    chk = deepcopy(d["check"])
    try:
      time_s = time.time()
      sol = f(*arg)
      time_e = time.time()
      res = check(arg[0], op_lim, hint, sol, chk)
      printhint(arg[0], op_lim, hint, sol)
      if ACC_TIME > 0 and float(time_e-time_s) > ACC_TIME:
        timeout += 1
        status_line += ' T'
        print("!!!!!!!! PRZEKROCZONY DOPUSZCZALNY CZAS")
      elif res == 0:
        passed += 1
        status_line += ' A'
        print("Test zaliczony!")
        points += 0.2
        if i >= 3:
          sqrt = True
        if i >= 6:
          logn = True
      elif res == 3:
        asd_avoid += 1
        print("UŻYJ ASD-0x1000101!!!")
        status_line += ' X'
      else:
        if res == 1:
          answer += 1
          print("TEST NIEZALICZONY!!!")
          status_line += ' W'
        else:
          expensive += 1
          print("ZBYT DROGIE ROZWIĄZANIE!!!")
          if hint == sol:
            points += 0.2
          status_line += ' C'
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
  print("Liczba testów z za drogim algorytmem: %d/%d" % (expensive,total))
  print("Liczba testów bez użycia ASD-0x1000101: %d/%d" % (asd_avoid,total))
  print("Orientacyjny łączny czas : %.2f sek." % total_time)
  print("Status testów:%s" % status_line)
  if sqrt:
    points += 1.5
  if logn:
    points += 2.5
  if not answer:
    points += 1

  if asd_avoid:
    points = 0.0
  print(f"Liczba uzyskanych punktów: {round(points, 2)}")

def copyarg(arg):
    return deepcopy(arg)

def printhint(T, op_lim, hint, sol):
    print(f"Koszt wygenerowany przez użytkownika:       {round(T.get_cost(), 4)} BIT COINS")
    print(f"Maksymalny kosz wywołań funkcji:            {op_lim} BIT COINS")
    print(f"Otrzymany wynik:                            {sol}")
    print(f"Oczekiwany wynik:                           {hint} ")

def printsol(sol):
  pass

def check(T, op_lim, hint, sol, chk):
  if chk > T.get_cost():
    return 3
  elif T.get_cost() > op_lim:
    return 2
  elif hint != sol:
    return 1
  else:
    return 0
    
def generate_tests(num_tests = None):
    global TEST_SPEC
    TESTS = []

    if num_tests is not None:
        TEST_SPEC = TEST_SPEC[:num_tests]

    for spec in TEST_SPEC:
        newtest = {}
        arg, hint, op_lim, check = gentest(*spec)
        newtest["arg"] = arg
        newtest["hint"] = hint
        newtest["op_lim"] = op_lim
        newtest["check"] = check
        TESTS.append(newtest)
              
    return TESTS
 
def runtests(f, all_tests = 3):
    internal_runtests( copyarg, printhint, printsol, check, generate_tests, all_tests, f, ALLOWED_TIME )

