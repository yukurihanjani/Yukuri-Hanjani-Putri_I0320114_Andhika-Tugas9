# mengonversi string ke dalam array.array

import array

B = array.array('b')
B.frombytes(str.encode("Python"))

for karakter in B:
    print("%c"%karakter,end=' ')