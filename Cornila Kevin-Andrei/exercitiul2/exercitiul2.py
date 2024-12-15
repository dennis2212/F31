import pandas as pd
import matplotlib.pyplot as plt

#Procesarea datelor din CSV, intr-un DataFrame(specific pandas)
data_file = "data.csv"
data = pd.read_csv(data_file)

#Primul grafic pentru toate valorile
data.plot()
plt.title("Toate valorile")
plt.xlabel("Nr.crt.")
plt.ylabel("Valori")
plt.legend(title="Lista parametrii")
plt.grid()
plt.savefig("all_values.png")
plt.show()
plt.close()

#Al doilea grafic pentru primele X valori
data[:7].plot()
plt.title("Primele 7 valori")
plt.xlabel("Nr.crt.")
plt.ylabel("Valori")
plt.legend(title="Lista parametrii")
plt.grid()
plt.savefig("first7_values.png")
plt.show()
plt.close()

#Al treilea grafic pentru ultimele Y valori, afisand doar Durata si Puls
(data[["Durata", "Puls"]].tail(11)).plot()
plt.title("Ultimele 11 valori")
plt.xlabel("Nr.crt.")
plt.ylabel("Valori")
plt.legend(title="Lista parametrii")
plt.grid()
plt.savefig("last11_values.png")
plt.show()
plt.close()
