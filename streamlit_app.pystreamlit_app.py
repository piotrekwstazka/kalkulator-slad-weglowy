from dane import wspolczynniki_emisji
from raport import generuj_raport

def uruchom_kalkulator():
    print("=== Kalkulator śladu węglowego ===")

    kilometry = float(input("Ile km przejechałeś samochodem benzynowym? "))
    dieta = input("Twoja dieta (miesna/wegetarianska/wegańska): ").strip().lower()
    zuzycie_pradu = float(input("Ile kWh prądu zużyłeś dziś? "))
    zuzycie_wody = float(input("Ile litrów wody zużyłeś dziś? "))

    suma = 0
    suma += kilometry * wspolczynniki_emisji["transport"]["samochod_benzyna"]
    suma += wspolczynniki_emisji["dieta"].get(dieta, 5.0)
    suma += zuzycie_pradu * wspolczynniki_emisji["energia"]["prad_kwh"]
    suma += zuzycie_wody * wspolczynniki_emisji["energia"]["woda_litr"]

    generuj_raport(suma)
