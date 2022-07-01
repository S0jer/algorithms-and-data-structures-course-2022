# Dostałeś sejf, który odblokowuje się czterocyfrowym PINem (0000 - 9999). Pod wyświetlaczem znajduje się kilka
# przycisków z liczbami od 1 do 9999 - przykładowo (13, 223, 782, 3902). Sejf ten działa inaczej niż normalny:
# wciśnięcie przycisku z liczbą powoduje dodanie liczby z przycisku do liczby na wyświetlaczu. Jeżeli suma jest
# większa niż 9999, to pierwsza cyfra zostaje obcięta.
#
# Jest tobie znany PIN oraz cyfry, które są aktualnie wyświetlane. Znajdź najkrótszą sekwencję naciśnięć przycisków,
# która pozwoli ci odblokować sejf. Jeżeli taka sekwencja nie istnieje, zwróć None.


# Inspirowane UVa 12160.
#
# Jako reprezentację grafu wybieramy listy sąsiedztwa, bo są szybsze (graf rzadki, kilka krawędzi na wierzchołek).
#
# Tworzymy graf skierowany, w którym wierzchołkami są kody 0000-9999, a krawędzie prowadzą między wierzchołkami takimi,
# że można z jednego do drugiego przejść przez jedno naciśnięcie przycisku. Następnie uruchamiamy BFSa z kodu,
# który jest na początku wyświetlany i znajdujemy najkrótszą ścieżkę do kodu PIN.


def sejf(pin, buttons):
    pass

