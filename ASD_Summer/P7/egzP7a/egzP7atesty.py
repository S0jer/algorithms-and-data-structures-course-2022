import sys
from copy import deepcopy
import time
from random import random, randint, seed, shuffle
ALLOWED_TIME = 0.3


global k_seed
k_seed = 0

TEST_SPEC = [
    #n (połączenia),  hint (wynik)
    (0,               0),
    (10,              2),
    (15,              2),
    (25,              4),
    (50,              14),
    (80,              19),
    (110,             17),
    (140,             17),
    (170,             30),
    (210,             36),
]

def randint_seed(a, b):
  global k_seed
  output = randint(a, b)
  k_seed += 1
  seed(k_seed)
  return output

def gentest(n, hint):
    if n == 0:
        T = [(2, 3, None), (0, 1, 3), (0, 2, None), (1, 3, 4), (2, 3, None)]
        return T, hint

    T = []
    
    for i in range(n):
        n1 = randint_seed(0, 7)
        n2 = 0
        if n1 == 7:
            n2 = 0 
        elif n1 >= 6:
            n2 = 1 
        elif n1 >= 2:
            n2 = 2 
        else:
            n2 = 3 

        el = [None, None, None]
        if n2 > 0:
            el[0] = randint_seed(0, n//3)
        if n2 > 1:
            el[1] = randint_seed(el[0]+1, n//1.5)
        if n2 > 2:
            el[2] = randint_seed(el[1]+1, n-1)

        T.append((el[0], el[1], el[2])) 
    
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
  seed(0)
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
    print("Oczekiwany wynik: ", hint)

def printsol(sol):
    print("Otrzymany wynik : ", sol)

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

