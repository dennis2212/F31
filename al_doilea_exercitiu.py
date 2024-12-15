import matplotlib.pyplot as plt
import pandas as pd 

df=pd.read_csv("data.csv")

df.plot()
plt.title("Toate valorile")
plt.xlabel("Index")
plt.ylabel("Valori")
plt.legend(title="Parametrii")
plt.savefig("Toate valorile.png")
plt.show()

df[:5].plot(color=['orange','cyan','magenta','lime'])
plt.title("Primele 5 valori")
plt.xlabel("Index")
plt.ylabel("Valori")
plt.legend(title="Parametrii")
plt.savefig("Primele 5 valori.png")
plt.show()

df[-13:].plot()
plt.title("Ultimele 13 valori")
plt.xlabel("Index")
plt.ylabel("Valori")
plt.legend(title="Parametrii")
plt.savefig("Ultimele 13 valori.png")
plt.show()