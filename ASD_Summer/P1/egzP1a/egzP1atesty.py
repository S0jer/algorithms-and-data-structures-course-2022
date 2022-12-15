import time 

TEST_SPEC = [
# N (długość tablicy), X (statystyczny wsskaznik ilosci liter, niedokładny!) hint (poprawna odpowiedź)
  (0, 0, 5),
  (10, 5, 13),
  (20, 10, 28),
  (50, 15, 48),
  (100, 25, 97),
  (150, 50, 130),
  (500, 15, 560),
  (2500, 25, 2274),
  (5000, 25, 4493),
  (10000, 50, 8475),
  (20000, 50, 17255),
  (100000, 150, 83089),
]

MY_seed    = 42
MY_a       = 134775813
MY_c       = 1
MY_modulus = 2**32

M = [('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'), ('E', '.'), ('F', '..-.'),
('G', '--.'), ('H', '....'), ('Res', '..'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
('M', '--'), ('N', '-.'), ('O', '---'), ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'), 
('S', '...'), ('T', '-'), ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'),
('Y', '-.--'), ('Z', '--..')]

def MY_random():
   global MY_seed, MY_a, MY_c, MY_modulus
   MY_seed = (MY_a * MY_seed + MY_c) % MY_modulus
   return MY_seed

def runtests( f, recursion ):
    global TEST_SPEC
    NEWTESTS = []
    if recursion == True: 
        for j in range(6):
            NEWTESTS.append(TEST_SPEC[j])
        TEST_SPEC = NEWTESTS
    total = 0 
    zaliczone = 0 
    testy = 0
    i = 0
    for el in TEST_SPEC:
        W = ""
        for j in range(el[0]):
            W = W + chr((MY_random()%26)+65)

        D = [4, 19]

        for j in range(el[1]):
            rng = MY_random()%26
            if rng not in D:
                D.append(rng)

        if i == 0:
            W = "SOS"
            D = [0, 4, 13, 19, 25]
        D.sort()
        
        start = time.time()
        sol = f(W, M, D)
        end = time.time()
        total += (end-start)
        testy += 1 
        if sol == el[2]:
            print("TEST #", i, " zaliczony")
            print("Twoja odpowiedz: ", sol, "\nPoprawna odpowiedz: ", el[2])
            print("Czas trwania: %.2f sek.\n" %float(end-start))
            zaliczone += 1
        else:
            print("TEST #", i, " NIEZALICZONY!")
            print("Twoja odpowiedz: ", sol, "\nPoprawna odpowiedz: ", el[2])
            print("Czas trwania: %.2f sek.\n" %float(end-start))

        i += 1
    print("Zaliczone testy: ", zaliczone, "/", testy)
    print("Orientacyjny łączny czas: %.2f sek." %float(total))

