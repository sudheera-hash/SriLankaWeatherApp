import traceback
import tkinter as tk
from tkinter import messagebox, ttk
from weather import get_weather

# ─── Main App Window ───────────────────────────────────────────
app = tk.Tk()
app.title("Weather App")
app.geometry("420x600")
app.resizable(False, False)
app.configure(bg="#1e1e2e")

# ─── Title Label ───────────────────────────────────────────────
title_label = tk.Label(
    app,
    text="🌤 Weather App",
    font=("Helvetica", 22, "bold"),
    bg="#1e1e2e",
    fg="#cdd6f4"
)
title_label.pack(pady=20)

# ─── Dropdown Label ────────────────────────────────────────────
dropdown_label = tk.Label(
    app,
    text="Select a Sri Lankan city",
    font=("Helvetica", 12),
    bg="#1e1e2e",
    fg="#cdd6f4"
)
dropdown_label.pack(pady=(15, 5))

# ─── All Cities in Sri Lanka (Comprehensive List) ──────────────
sri_lankan_cities = [
    # Western Province
    "Colombo", "Negombo", "Gampaha", "Kalutara", "Moratuwa", "Dehiwala-Mount Lavinia", "Sri Jayawardenepura Kotte",
    # Central Province
    "Kandy", "Matale", "Nuwara Eliya", "Gampola", "Dambulla", "Hatton", "Talawakele",
    # Southern Province
    "Galle", "Matara", "Hambantota", "Tangalle", "Weligama", "Ambalangoda", "Bentota",
    # Northern Province
    "Jaffna", "Kilinochchi", "Mannar", "Mullaitivu", "Vavuniya", "Point Pedro", "Chavakachcheri",
    # Eastern Province
    "Trincomalee", "Batticaloa", "Ampara", "Kalmunai", "Kattankudy", "Eravur",
    # North Western Province
    "Kurunegala", "Puttalam", "Chilaw", "Kuliyapitiya", "Narammala",
    # North Central Province
    "Anuradhapura", "Polonnaruwa", "Kekirawa", "Medawachchiya",
    # Uva Province
    "Badulla", "Monaragala", "Bandarawela", "Haputale",
    # Sabaragamuwa Province
    "Ratnapura", "Kegalle", "Balangoda", "Embilipitiya"
]

# Sort alphabetically for better user experience
sri_lankan_cities.sort()

selected_city = tk.StringVar()
selected_city.set("Select a city")

dropdown = ttk.Combobox(
    app,
    textvariable=selected_city,
    values=sri_lankan_cities,
    font=("Helvetica", 12),
    state="readonly",
    width=28,
    justify="center"
)
dropdown.pack(pady=5)

# ─── Result Frame ──────────────────────────────────────────────
result_frame = tk.Frame(app, bg="#313244", bd=0)
result_frame.pack(pady=20, padx=30, fill="both")

city_label = tk.Label(result_frame, text="", font=("Helvetica", 20, "bold"), bg="#313244", fg="#cdd6f4")
city_label.pack(pady=(20, 0))

desc_label = tk.Label(result_frame, text="", font=("Helvetica", 13, "italic"), bg="#313244", fg="#a6adc8")
desc_label.pack()

temp_label = tk.Label(result_frame, text="", font=("Helvetica", 40, "bold"), bg="#313244", fg="#89b4fa")
temp_label.pack(pady=10)

details_label = tk.Label(result_frame, text="", font=("Helvetica", 11), bg="#313244", fg="#a6adc8", justify="left")
details_label.pack(pady=(0, 20))

# ─── Weather Display Function ──────────────────────────────────
def display_weather(weather):
    city_label.config(text=f"{weather['city']}, {weather['country']}")
    desc_label.config(text=weather["description"])
    temp_label.config(text=f"{weather['temperature']}°C")
    details_label.config(
        text=(
            f"Feels like   :  {weather['feels_like']}°C\n"
            f"Humidity     :  {weather['humidity']}%\n"
            f"Wind Speed   :  {weather['wind_speed']} m/s"
        )
    )

def on_city_select(event):
    city = selected_city.get()
    if city == "Select a city":
        return
    weather, error = get_weather(city)
    if error:
        messagebox.showerror("Error", error)
        return
    display_weather(weather)

# ─── Bind Dropdown Selection ───────────────────────────────────
dropdown.bind("<<ComboboxSelected>>", on_city_select)

# ─── Run App ───────────────────────────────────────────────────
try:
    app.mainloop()
except Exception as e:
    traceback.print_exc()
    input("Press Enter to close...")