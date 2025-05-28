import streamlit as st

# Tytuł aplikacji
st.title("🌍 Kalkulator Śladu Węglowego")
st.markdown("Oblicz swój przybliżony wpływ na klimat na podstawie codziennych wyborów.")

# Wprowadzenie danych
st.header("🚗 Transport")

samochod_km = st.number_input("Ile kilometrów tygodniowo pokonujesz samochodem?", min_value=0, step=1)
samochod_emisja = samochod_km * 0.192  # kg CO2/km

transport_publiczny_km = st.number_input("Ile kilometrów tygodniowo pokonujesz transportem publicznym?", min_value=0, step=1)
transport_publiczny_emisja = transport_publiczny_km * 0.05

st.header("⚡ Energia")

prad_kWh = st.number_input("Ile kWh prądu zużywasz miesięcznie?", min_value=0, step=1)
prad_emisja = prad_kWh * 0.426  # kg CO2/kWh (średnia UE)

gaz_m3 = st.number_input("Ile m³ gazu ziemnego zużywasz miesięcznie?", min_value=0, step=1)
gaz_emisja = gaz_m3 * 1.9  # kg CO2/m3

st.header("🍔 Żywność")

mieso_dni = st.slider("Ile dni w tygodniu jesz mięso?", 0, 7, 3)
mieso_emisja = mieso_dni * 7 * 2.5  # przybliżona emisja: 2.5 kg CO2 dziennie z diety mięsnej

st.header("✈️ Loty")

loty_km = st.number_input("Ile km rocznie pokonujesz samolotem?", min_value=0, step=10)
loty_emisja = loty_km * 0.15  # kg CO2/km

# Obliczanie łącznej emisji
if st.button("Oblicz mój ślad węglowy"):
    emisja_razem = (
        samochod_emisja * 52 +  # tygodniowo na rok
        transport_publiczny_emisja * 52 +
        prad_emisja * 12 +      # miesięcznie na rok
        gaz_emisja * 12 +
        mieso_emisja * 52 +
        loty_emisja
    )

    emisja_razem_tony = emisja_razem / 1000  # kg → tony

    st.subheader("📊 Wynik")
    st.success(f"Twój roczny ślad węglowy to około **{emisja_razem_tony:.2f} ton CO₂e**.")

    st.markdown("### Porównanie:")
    st.markdown("- 🌱 Ślad zrównoważony dla klimatu: **~2 tony rocznie**")
    st.markdown("- 🌍 Średni Europejczyk: **~7–10 ton**")
    st.markdown("- 🇺🇸 Średni mieszkaniec USA: **~15–20 ton**")

    st.markdown("### 💡 Jak zmniejszyć swój ślad?")
    st.markdown("- Ogranicz podróże samolotem i jazdę samochodem")
    st.markdown("- Jedz mniej mięsa, szczególnie czerwonego")
    st.markdown("- Oszczędzaj energię: wyłączaj urządzenia, korzystaj z LED")
    st.markdown("- Wybieraj energię z odnawialnych źródeł")

st.markdown("---")
st.caption("Projekt edukacyjny wykonany w Pythonie i Streamlit 🌿")
