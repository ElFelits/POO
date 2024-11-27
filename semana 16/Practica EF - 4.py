import matplotlib.pyplot as plt
import random

ingresos = []
gastos = []

for i in range(18):
    ingresos.append(random.randint(1000, 10000))
    gastos.append(random.randint(1000, 10000))

meses = list(range(1, 19))

plt.figure(figsize=(10, 6))
plt.scatter(meses, ingresos, label="Ingresos", color="b", marker="o")
plt.scatter(meses, gastos, label="Gastos", color="r", marker="x")
plt.title("Evolución de ingresos y gastos")
plt.xlabel("Meses")
plt.ylabel("Monto en USD")
plt.legend()  
plt.ylim(0)  
plt.grid(True)
plt.show()
