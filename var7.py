def cek_palindrom(kata):
    kata = kata.lower()
    if kata == kata[::-1]:
        return f"{kata} = palindrom"
    else:
        return f"{kata} = bukan palindrom"
print(cek_palindrom("kasur"))