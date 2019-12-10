s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
one_only = (1, 5, 6, 7, 8, 9, 15, 16, 19)
elem_tbl = {}
s_ = s.split(" ")
for i, elem in enumerate(s_, 1):
    if i in one_only:
        elem_tbl[elem[0:1]] = i
    else:
        elem_tbl[elem[0:2]] = i
print(elem_tbl)
