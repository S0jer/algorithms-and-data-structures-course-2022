# W pewnym kraju trwa wojna domowa. W ramach sabotażu rebelianci chcą uniemożliwić komunikację telegraficzną z miasta A do B.
# Otrzymujemy listę miast i linii telegraficznych między nimi. Linie telegraficzne są skierowane. Każda z linii
# ma przypisany koszt zniszczenia jej. Chcemy wybrać zbiór połączeń do zniszczenia o łącznym minimalnym koszcie.
# Interesuje nas nie tylko koszt, ale które konkretnie linie telegraficzne mamy zniszczyć.

# Wyjaśnienie w książce “Competitive programming 3”: https://drive.google.com/file/d/1fmgmFy_6SFvEVi7Ovpkmudho_Yr8NurC/view?usp=sharing
#
# Jedyny problem tutaj jest taki, że linie telegraficzne są nieskierowane

# Jakoś max-flow plus znalezienie tych połączeń
