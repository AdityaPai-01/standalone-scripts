# TEMPERATURE DATA ANALYSER
import numpy as np

Cities = ["Pallet Town", "Morganstown", "Leighton City", "Westerfield", "Berreily"]
Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def generate_temperature_data(months=12, cities=5, low=20.0, high=50.0, seed=42):
    rng = np.random.default_rng(seed) 
    data = rng.uniform(low, high, size=(months, cities)) 
    return np.round(data, 1)

Temperature_Data = generate_temperature_data()

# --- THE NUMPY WAY: Calculate everything upfront without loops! ---
# axis=0 crunches data DOWN the rows (calculating stats for each city across all 12 months)
avg_temps = np.mean(Temperature_Data, axis=0)
max_temps = np.max(Temperature_Data, axis=0)
min_temps = np.min(Temperature_Data, axis=0)

# Get indices of max and min months for all cities instantly
max_month_indices = np.argmax(Temperature_Data, axis=0)
min_month_indices = np.argmin(Temperature_Data, axis=0)

# --- THE PRINT LOOP (Only for display purposes) ---
for i, city in enumerate(Cities):
    print(f"=== {city.upper()} ===")
    
    # Clean slicing: get all 12 months for city 'i'
    city_temps = Temperature_Data[:, i] 
    
    # Optional: Zip makes printing monthly data cleaner if you want to show it
    # for month, temp in zip(Months, city_temps):
    #     print(f"{month}: {temp}°C")
    
    # Print the pre-calculated stats smoothly
    print(f"Average Temperature: {avg_temps[i]:.1f}°C")
    
    peak_month = Months[max_month_indices[i]]
    print(f"Peak Temperature:    {max_temps[i]}°C in {peak_month}")
    
    lowest_month = Months[min_month_indices[i]]
    print(f"Lowest Temperature:  {min_temps[i]}°C in {lowest_month}")
    print("-" * 30)