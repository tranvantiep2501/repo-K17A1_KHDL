tien_doi = 1375000
so_to1 = tien_doi // 500000
con_lai = tien_doi % 500000
so_to2 = con_lai // 200000
con_lai1 = con_lai % 200000
so_to3 = con_lai1 // 100000
con_lai2 = con_lai1 % 100000
so_to4 = con_lai2 // 50000
con_lai3 = con_lai2 % 50000
print('So tien muon doi', tien_doi)
print('So to 500,000 :', so_to1)
print('So to 200,000', so_to2)
print('So to 100,000 :', so_to3)
print('So to 50,000 :', so_to4)
