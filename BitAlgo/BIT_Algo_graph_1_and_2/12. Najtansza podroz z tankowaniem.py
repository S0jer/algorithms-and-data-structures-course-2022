# Dostajemy na wejściu graf, w którym wierzchołkami są miasta, a krawędziami drogi między nimi. Dla każdego miasta
# znamy cenę paliwa w złotych na litr, a dla każdej drogi jej długość w kilometrach.
# Nasz samochód ma zbiornik pojemności 100 litrów i pali jeden litr na kilometr.
# Startujemy z miasta A z pustym zbiornikiem. Ile minimalnie musimy zapłacić za paliwo, aby dotrzeć do miasta B?


# Rozwiązanie polega na powiększeniu otrzymanego grafu do reprezentacji która zawiera wierzchołki
# odpowiadające dotarciu do miasta k z i-toma litrami paliwa, dla tak stworzonego grafu
# (będzie on t razy większy od wyjściowego gdzie t - pojemność zbiornika na paliwo)
# uruchamiamy algorytm dijkstra który oblicza nam minimalną cenę.
