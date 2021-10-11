from math import *


# PROBLEMA 1.
def get_largest_prime_below(n):


    nr_prim = 0

    if n <= 2:
        return None
#Nu exista numar prim mai mic decat 2

    else:
        for i in range(2, n):
            q = 0
            for j in range(2, floor(i/2)+1):
                if i%j == 0:
                    q = q+1
            if q==0:
                nr_prim=i
# Pentru fiecare numar de la 2 la n-1, verificam daca numarul este prim.
# nr_prim ia ultima valoare de numar prim mai mica decat n

    return nr_prim

def test_get_largest_prime_below():
    assert get_largest_prime_below(67) == 61
    assert get_largest_prime_below(15) == 13
    assert get_largest_prime_below(9) == 7


# PROBLEMA 10. Vom calcula combinari de n luate cate k

def get_n_choose_k(n, k):
    if n < k:
        return False

# Nu exista Combinari de n luate cate k, cand n este mai mic decat k

# Vom introduce niste variabile locale pe care sa le folosim in while loops
    else:
        i = 1
        j = 1
        x = 1
        n_factorial = 1
        k_factorial = 1
        n_minus_k_factorial = 1
        combinari_n_luate_cate_k = 1

# Calculam factorialele lui n, k si n-k  (Combinari de n luate cate k = n!/ (k! * (n-k)!)

        while i < n:
            n_factorial = n_factorial * (i + 1)
            i = i + 1

        while j < k:
            k_factorial = k_factorial * (j + 1)
            j = j + 1

        while x < n - k:
            n_minus_k_factorial = n_minus_k_factorial * (x + 1)
            x = x + 1

        combinari_n_luate_cate_k = n_factorial / ( k_factorial * n_minus_k_factorial )

        return combinari_n_luate_cate_k

# Returneaza Combinari de n luate cate k


def test_get_n_choose_k():
    assert get_n_choose_k(5, 2) == 10
    assert get_n_choose_k(4, 1) == 4
    assert get_n_choose_k(6, 3) == 20




# PROBLEMA 5.

def is_palindrome(n):
    palindrom = 0
    while n != 0:
        a = n
        palindrom= palindrom * 10 + (a % 10)
        a = floor(a/10)
    if palindrom == n:
        return True

def test_is_palindrome():
    assert is_palindrome(1221) == True
    assert is_palindrome(123) == False
    assert is_palindrome (45454) == True


def main():
    optiune = """
    Introduceti cifra corespunzatoare optiunii pe care o alegeti:
    1. Găsește ultimul număr prim mai mic decât un număr dat.
    2. Calculează combinări de n luate câte k (n și k date).
    3. Verifica daca numarul dat este palindrom.
    4. Iesire.
    """

    a = input(optiune)
    while a != "4":
        if a=="1":
            get_largest_prime_below(int(input("Introduceti un numar: ")))
        elif a=="2":
            get_n_choose_k(int(input("Introduceti n si k: ")))
        elif a=="3":
            is_palindrome(int(input("Introduceti un numar: ")))
        else:
            print("Optiune gresita. Alegeti din nou optiunea.")
        a = input(optiune)


main()



