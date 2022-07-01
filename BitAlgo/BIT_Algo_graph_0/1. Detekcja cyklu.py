# Napisz algorytm sprawdzający, czy graf nieskierowany posiada cykl.


# Rozwiązanie: zauważmy, że jeżeli wejdziemy w cykl w grafie nieskierowanym, to przeglądając poddrzewo pierwszego
# wierzchołka cyklu do którego weszliśmy, będziemy ponownie próbowali się do niego dostać, przed wyjściem z niego.
#
# Łopatologicznie: jak już coś pokolorowaliśmy, to tam byliśmy, więc jak tam chcemy wejść, to znaczy, że mamy cykl.


# def DFSvisit(Graph, vertex):
#     vertex.color = Gray
#     isCycle = false
#     for v in vertex.adj:
#         if Graph[v].color == WHITE:
#             isCycle = isCycle or DFSvisit(Graph, Graph[v])
#         elif Graph[v].color == GRAY:
# 	        isCycle = True
#  	vertex.color = BLACK
# 	return isCycle
