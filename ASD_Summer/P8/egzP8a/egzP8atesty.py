import sys
from copy import deepcopy
import time
from random import random, randint, seed, shuffle
ALLOWED_TIME = 2


global k_seed
k_seed = 0

TEST_SPEC = [
    #n (połączenia),  m (max),        hint (wynik)
    (0,               0,              15000),
    (10,              10,             92),
    (20,              20,             190),
    (500,             100,            4972),
    (15000,           2500,           3348088),
    (50000,           5000,           13720053),
    (75000,           10000,          22062179),
    (100000,          20000,          29421726),
    (125000,          30000,          37340053),
    (150000,          40000,          44931807),
]

def randint_seed(a, b):
  global k_seed
  output = randint(a, b)
  k_seed += 1
  seed(k_seed)
  return output

def gentest(n, m, hint):
  if n == 0:
    T = [ (0, 3), (4, 5), (1, 4) ]
    S = [ 5000, 3000, 15000 ]
    return T, S, m, hint
  T = []
  S = []
  for i in range(n):
    a = randint_seed(0, m-3)
    b = randint_seed(a+1, m) 
    T.append((a, b))
    x = randint_seed(1, 1000)
    if x == 1000:
      S.append(randint_seed(1, 150*n))
    elif x >= 997:
      S.append(randint_seed(1, 20*n))
    else:
      S.append(randint_seed(1, 5*n))
  return T, S, m, hint

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
  seed(0)
  passed, timeout, answer, exception = 0, 0, 0, 0

  print("(!) Generowanie testów. Proszę czekać...")
  print("(!) To może zająć nawet KILKANAŚCIE sekund...")
  print("(!) Do testowania wstępnego użyj all_tests = False")

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
    arg2  = copyarg(d["arg2"])
    arg3  = copyarg(d["arg3"])
    hint = deepcopy(d["hint"])
    printhint( hint )
    try:
      time_s = time.time()
      sol    = f(arg, arg2, arg3)
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
        arg, arg2, arg3, hint = gentest(*spec)
        newtest["arg"] = arg
        newtest["arg2"] = arg2
        newtest["arg3"] = arg3
        newtest["hint"] = hint
        TESTS.append(newtest)
              
    return TESTS
 
def runtests(f, all_tests = 3):
    internal_runtests( copyarg, printhint, printsol, check, generate_tests, all_tests, f, ALLOWED_TIME )

