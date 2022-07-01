# Dany jest ciąg przedziałów postaci [ai, bi]. Dwa przedziały można skleić, jeśli mają dokładnie jeden punkt wspólny.
# Podaj algorytm, który sprawdza, czy da się uzyskać przedział [a, b] poprzez sklejanie odcinków.


# Na dobry początek trzeba w ogóle stworzyć graf z tych odcinków. Każdy wierzchołek to początek lub koniec odcinka,
# krawędzie są między tymi wierzchołkami, które tworzą odcinek (początek -> koniec).
# Optymalna reprezentacja: zależy od grafu, listowo będzie pewnie prościej

# Rozwiązanie: jeżeli w słowniku nie ma klucza a, to zwracamy False. Jeżeli klucz a jest, to puszczamy DFSa po grafie,
# aż dojdziemy do b i wtedy zwracamy True. Jeżeli po przeszukaniu całego grafu nie doszliśmy, to zwracamy False.

# Złożoność: O(Vlog(V)) + O(V + E) = O(Vlog(V) + E), konstrukcja grafu + algorytm




