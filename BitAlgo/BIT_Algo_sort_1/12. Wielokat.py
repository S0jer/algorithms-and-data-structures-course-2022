# Dany jest zawierający n wierzchołków wielokąt, niekoniecznie wypukły. Jest reprezentowany jako tablica par struktur:
# class Point:
# 	x
# 	y
# w której (p1, p2) oznacza, że obiekty p1 i p2 klasy Point są połączone odcinkiem. Dany jest również punkt q,
# leżący poza wielokątem. Zaimplementuj/zaproponuj algorytm, który wyznaczy jak należy poprowadzić półprostą,
# zaczynającą się w punkcie q, tak aby przecięła jak najwięcej odcinków wielokąta. Uwaga!: zakładamy,
# że jeśli punkt p jest wspólny dla dwóch odcinków, to prosta przechodząc przez ten punkt przecina oba.
# Algorytm powinien działać w czasie O(nlog(n)).



# Należy “skanować” punkty wielokąta, posortowane po współrzędnej x , linią wychodzącą z q.

