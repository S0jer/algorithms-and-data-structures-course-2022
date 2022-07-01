# W problemie tankowania paliwa nasz pojazd musi przemieścić się z punktu 0 do punktu F, a po drodze ma stacje
# do tankowania paliwa si, przy czym 0 < s1 < s2 < ... < sn < F. Każda stacja jest identyfikowana przez jej odległość
# od punktu 0, tzn. si to odległość pomiędzy i-tą stacją a punktem 0. Pojazd potrafi przejechać odległość d bez potrzeby
# tankowania. Podaj algorytm, który obliczy, na ilu minimalnie stacjach musi zatrzymać się pojazd na drodze od punktu 0 do punktu F.
# Uwaga: jeżeli zdarzy się, że odległość d jest zbyt mała, żeby dojechać do kolejnej stacji, to należy zwrócić wartość None.

# Rozwiązanie:
# Semestr II/ASD/Zad_ob/Czołgi.py


# Zadanie 18: http://web.csulb.edu/~tebert/teaching/lectures/528/greedy/greedy.pdf
#
# Consider the greedy algorithm which first checks if F is within d units of the current location (either the start
# or the current station where the vehicle has just re-fueled). If F is within d units of this location, then no more
# stations are needed. Otherwise it chooses the next station on the trip as the furthest one that is within d units of
# the current location.
#
# Uzasadnienie poprawności:
# Załóżmy, że istnieje inna strategia, która pozwala na wybór mniejszej ilości stacji. W takiej strategii co najmniej raz
# musielibyśmy wybrać stację bliższą niż tę najdalszą w zasięgu d od miejsca w którym jesteśmy. W ten sposób wybierzemy
# tyle samo lub więcej stacji niż w oryginalnej strategii. Sprzeczność.
