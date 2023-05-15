from poly import Poly
# раскладывает на неприводимые множители многочлен и
# возвращает лист кортежей вида ([1, x_0], k) и ([1, p, q], k)

def find_dividers(n):
    dividers = []
    for i in range(1, int(n**0.5) + 1):
        if(n % i == 0):
            dividers.append(i)
            if(n // i) != i:
                dividers.append(n//i)
    return sorted(dividers)

def search_rational_roots(poly: Poly):
    dict = {}
    old_k = poly.coefficients[0]
    free_k = poly.coefficients[-1]
    candidates = []
    old_k_dividers = find_dividers(old_k)
    free_k_dividers = find_dividers(free_k)
    free_k_dividers = free_k_dividers + [-x for x in free_k_dividers]
    for i in range(len(free_k_dividers)):
        for j in range(len(old_k_dividers)):
            candidate = free_k_dividers[i] / old_k_dividers[j]
            if poly.is_root(candidate):
                candidates.append(candidate)
    for i in candidates:
        deg = 0
        poly_copy = Poly(poly)
        while(poly_copy.is_root(i)):
            deg+=1
            poly_copy = ~poly_copy
        dict[i] = deg

    return dict
            
p = Poly([1,-6.28*100,3.14*3.14*10000])
print(search_rational_roots(p))
