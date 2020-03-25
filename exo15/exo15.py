def jeSuisYield():
    a = range(10)
    for b in a:
        yield b+b

generateur = jeSuisYield()
print(generateur) 

for b in generateur:
    print(b)