import pandas as pd
import numpy as np

def main():
    print("--- Weather Data Analysis with NumPy ---")

    # --- 1. Setup & Data Loading ---
    print("\n[1] Loading Data...")
    try:
        # Reading the CSV into a DataFrame
        df = pd.read_csv("Weather Dataset.csv")
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("Error: 'Weather Dataset.csv' not found. Please ensure it is in the same directory.")
        return

    # Convert columns to NumPy arrays 
    temperatures = df['Temp_C'].to_numpy()
    wind_speeds = df['Wind Speed_km/h'].to_numpy()
    weather_conditions = df['Weather'].to_numpy()
    rel_humidity = df['Rel Hum_%'].to_numpy()


    # --- 2. Basic Statistical Analysis ---
    print("\n[2] Basic Statistical Analysis")
    
    # Temperature Stats
    print(f"Mean Temperature: {np.mean(temperatures):.2f}°C")
    print(f"Median Temperature: {np.median(temperatures):.2f}°C")
    print(f"Standard Deviation: {np.std(temperatures):.2f}°C")
    print(f"Range: {np.min(temperatures):.2f}°C to {np.max(temperatures):.2f}°C")

    # Wind Stats
    print(f"\nMean Wind Speed: {np.mean(wind_speeds):.2f} km/h")
    print(f"Max Wind Speed: {np.max(wind_speeds):.2f} km/h")


    # --- 3. Vectorization (Temperature Conversion) ---
    print("\n[3] Temperature Conversion (Vectorization)")
    
    temperatures_f = (temperatures * 9/5) + 32
    
    print("Sample Conversions (First 5):")
    for i in range(5):
        print(f"  {temperatures[i]:.1f}°C  ->  {temperatures_f[i]:.1f}°F")


    # --- 4. Advanced Filtering (Boolean Masking) ---
    print("\n[4] Filtering & Analysis")

    # Analysis 1: Freezing Days
    freezing_mask = temperatures < 0
    freezing_count = np.sum(freezing_mask)
    print(f"Hours with Freezing Temps (< 0°C): {freezing_count}")

    # Analysis 2: High Wind
    high_wind_mask = wind_speeds > 24
    high_wind_count = np.sum(high_wind_mask)
    print(f"Hours with High Winds (> 24 km/h): {high_wind_count}")

    # Analysis 3: 'Clear' Weather Specifics
    print("\n--- Conditional Analysis: 'Clear' Weather ---")
    clear_mask = (weather_conditions == 'Clear')
    clear_temps = temperatures[clear_mask]
    clear_winds = wind_speeds[clear_mask]
    
    print(f"Average Temp during Clear skies: {np.mean(clear_temps):.2f}°C")
    print(f"Max Wind during Clear skies: {np.max(clear_winds):.2f} km/h")

    # Analysis 4: 'Fog' Weather Specifics
    print("\n--- Conditional Analysis: 'Fog' Weather ---")
    fog_mask = (weather_conditions == 'Fog')
    fog_temps = temperatures[fog_mask]
    fog_humidity = rel_humidity[fog_mask]
    
    print(f"Median Temp during Fog: {np.median(fog_temps):.2f}°C")
    print(f"Median Humidity during Fog: {np.median(fog_humidity):.2f}%")


    # --- 5. Complex Query (Wind Chill) ---
    print("\n[5] Complex Query: High Wind AND Freezing")
    wind_chill_mask = (freezing_mask) & (high_wind_mask)
    wind_chill_count = np.sum(wind_chill_mask)
    
    print(f"Events with BOTH Freezing Temps & High Wind: {wind_chill_count}")


if __name__ == "__main__":
    main()