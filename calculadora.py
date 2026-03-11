
def interes_simple(capital, tasa, tiempo):
    return capital * tasa * tiempo

if __name__ == "__main__":
    capital = float(input("Capital inicial: "))
    tasa = float(input("Tasa de interés (ej: 0.05 para 5%): "))
    tiempo = float(input("Tiempo en años: "))

    resultado = interes_simple(capital, tasa, tiempo)
    print(f"El interés generado es: {resultado}")
