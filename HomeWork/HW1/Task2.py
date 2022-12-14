 # 2. Напишите программу для проверки ложности утверждения
 # (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) для всех значений предикат.

print("w y z")
for w in [False, True]:
    for y in [False, True]:
       for z in [False, True]:
           if (not w or y or z) != (not w or y or z):
               print('Выражение: ¬(W ⋁ Y ⋁ Z) = ¬W ⋀ ¬Y ⋀ ¬Z - False')
    break
else:
    print('Выражение: ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - True')
