import sys
from copy import deepcopy
import time
from random import random, randint, seed, shuffle
from math import sqrt
ALLOWED_TIME = 4

# n - liczba szyfrów
# m - maksymalna długość szyfrów
# q - liczba wysłanych wiadomości
# hint - odpowiedź

global k_seed
k_seed = 0

TEST_SPEC = [
    #n, m, q, hint
    (0,         0,      0,          1.47712125),        # 0
    (8,         5,      10,         7.56660246),        # 0
    (10,        5,      10,         6.84990369),        # 0
    (2000,      15,     30000,      63275.80058149),    # 1
    (2000,      15,     35000,      73590.18985709),    # 1
    (5000,      18,     70000,      161072.89395236),   # 2
    (5000,      18,     75000,      172687.29946137),   # 2
    (20000,     20,     200000,     536343.47761579),   # 3
    (20000,     20,     200000,     536355.99083429)    # 3
]

def f(x):
    global k_seed
    k_seed += 1
    seed(k_seed)
    return round(sqrt(x ** 2 * random()))

def gen_string(m):
    global k_seed
    k_seed += 1
    seed(k_seed)
    length = max(f(m), 1)
    output = ""
    for _ in range(length):
        k_seed += 1
        seed(k_seed)
        output += "1" if randint(0, 1) else "0"
    return output

def gen_substring(D):
    global k_seed
    k_seed += 1
    seed(k_seed)
    x = randint(0, len(D) - 1)
    return D[x][f(len(D[x])):]

def gentest(n, m, q, hint):
    global k_seed
    D = Q = None
    if n == 0:
        D = ['0', '100', '1100', '1101', '1111']
        Q = ["", "1", "11", "0", "1101"]
    else:
        D = list(dict.fromkeys([gen_string(m) for _ in range(n)]))
        Q = [gen_substring(D) for _ in range(q)]
    D.sort()
    
    return [D, Q], hint

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

def internal_runtests( copyarg, printarg, printhint, printsol, check, generate_tests, all_tests, f, ACC_TIME ):
  passed, timeout, answer, exception = 0, 0, 0, 0

  print("Generowanie testów. Proszę czekać...")
  print("(!) To może zająć kilka sekund...")

  if all_tests == 0:
    TESTS = generate_tests(3)
  elif all_tests == 1:
    TESTS = generate_tests(5)
  elif all_tests == 2:
    TESTS = generate_tests(7)
  else:
    TESTS = generate_tests(9)

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
    printarg( *arg )
    printhint( hint )
    try:
      time_s = time.time()
      sol    = f(*arg)
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

def printarg(D, Q):
    print("D: ", limit(D))
    print("Q: ", limit(Q))

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
    internal_runtests( copyarg, printarg, printhint, printsol, check, generate_tests, all_tests, f, ALLOWED_TIME )

