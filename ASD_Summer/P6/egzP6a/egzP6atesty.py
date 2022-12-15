import sys
from copy import deepcopy
import time
from random import random, randint, seed, shuffle
ALLOWED_TIME = 0.05


global k_seed
k_seed = 0

TEST_SPEC = [
    #n (ilość), s (oczekiwany), m (max. długość), h (hint)
    (0, 3, 5, "a1a1"),
    (15, 5, 5, "9khf"),
    (25, 8, 10, "o68ce6"),
    (150, 75, 10, "05933v"),
    (500,  150, 50, "i349j3j1xqb1a2av09dz8wv0x4p0rxyf3gfd"),
    (2500, 500, 75, "e921v12bc7sf26zfl77y9j703kqohmwp3k0bj55yqi4p3sfc14fhwa28tsce"),
    (7500, 5000, 75, "1j429jjzpvk09f04h9y2ju5he7"),
    (10000, 5000, 100, "bhpfhs44i0r45ebxrk4bg05vf7k4yylxm8zmkk8msdcc95ck9"),
    (15000, 5000, 100, "urar84zngca6wn9no65qgh42rk4p107o1kclnzvz5bhjrmicwedvgaqnf757qv62pqp"),
    (25000, 20000, 100, "s1bd0oyzh2vw9ppobpkr"),
]

def randint_seed(a, b):
  global k_seed
  output = randint(a, b)
  k_seed += 1
  seed(k_seed)
  return output

def gentest(n, s, m, hint):
    if n == 0:
        T = ['aba', 'abc', 'ab1', 'abab', 'a1a1', 'aa12a']
        return T, s, hint

    T = []

    for i in range(n):
        dl = randint(1, m)
        ss = ""
        for j in range(dl):
            letter = randint(0, 5)
            if letter < 2:
                ss += chr(randint(48, 57))
            else:
                ss += chr(randint(97, 122))
        T.append(ss)

    
    return T, s, hint

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
    arg2 = deepcopy(d["arg2"])
    hint = deepcopy(d["hint"])
    printhint( hint )
    try:
      time_s = time.time()
      sol    = f(arg, arg2)
      time_e = time.time()
      
      printsol( sol )
      res = check(arg, hint, sol)
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
    print("Przykładowy oczekiwany wynik: ", hint)
    print("Może być wiele prawidłowych wyników...")

def printsol(sol):
    print("Otrzymany wynik : ", sol)

def check(T, hint, sol):
    #97, 122
    passed = True 
    if len(hint) != len(sol):
        return False
    if not sol in T:
        return False
    letters = 0
    for i in range(len(hint)):
        if ord(hint[i]) >= 97 and ord(hint[i]) <= 122:
            letters += 1 
        if ord(sol[i]) >= 97 and ord(sol[i]) <= 122:
            letters -= 1 
    if letters != 0:
        return False 
    return True 
    
def generate_tests(num_tests = None):
    global TEST_SPEC
    TESTS = []

    if num_tests is not None:
        TEST_SPEC = TEST_SPEC[:num_tests]

    for spec in TEST_SPEC:
        newtest = {}
        arg, arg2, hint = gentest(*spec)
        newtest["arg"] = arg
        newtest["arg2"] = arg2
        newtest["hint"] = hint
        TESTS.append(newtest)
              
    return TESTS
 
def runtests(f, all_tests = 3):
    internal_runtests( copyarg, printhint, printsol, check, generate_tests, all_tests, f, ALLOWED_TIME )

