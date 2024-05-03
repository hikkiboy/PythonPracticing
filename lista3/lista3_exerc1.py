arr_sal = []
arr_fil = []
salario100 = 0

for i in range(3):
     sal = float(input(f"Qual seu sal  {i}?"))
     if sal >= 100:
          salario100 += 1
     arr_sal.append(sal)
     fil = int(input(f"quantos filhos {i} ?"))
     arr_fil.append(fil)


percent = salario100 / 3 * 100
avg_sal = sum(arr_sal) / len(arr_sal)
avg_fil = sum(arr_fil) / len(arr_fil)
print(f"Media salarial: {avg_sal:.2f} ")
print(f"media filhos {avg_fil:.2f}")
print(f"avg salario : {percent:.2f}%")
     
