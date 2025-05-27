def generuj_raport(suma_emisji):
    print("\n=== PODSUMOWANIE ===")
    print(f"Twój dzienny ślad węglowy: {suma_emisji:.2f} kg CO₂")

    if suma_emisji > 30:
        print("🔴 Wysoki ślad węglowy. Zastanów się nad zmianą nawyków.")
    elif suma_emisji > 15:
        print("🟠 Średni poziom. Możesz coś poprawić.")
    else:
        print("🟢 Niski ślad. Dobra robota!")
