# Zaproponuj klasę reprezentującą strukturę danych, która w konstruktorze dostaje tablicę liczb naturalnych długości n
# o zakresie wartości [0, k]. Ma ona posiadać metodę count_num_in_range(a, b) - ma ona zwracać informację o tym,
# ile liczb w zakresie [a, b] było w tablicy, ma działać w czasie O(1). Można założyć, że zawsze a >= 1, b <= k.



# Coś jak counting sort, ale nie sortujemy, tylko zatrzymujemy się po etapie cumulative sum
# - wystarczy zwrócić cumulative_sum[b] - cumulative_sum[a]