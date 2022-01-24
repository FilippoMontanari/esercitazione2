cubi = [i**3 for i in range(10)]
print('Primi 10 cubi:', cubi)

cubi_filter = list(filter(lambda x: not x%2, cubi))
print('Solo quelli pari:', cubi_filter)

cubi_filter_map = list(map(lambda x: x*3, cubi_filter))
print('Moltiplicati per 3:', cubi_filter_map)