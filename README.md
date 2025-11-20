# Weather Data Analysis with NumPy ⛈️☀️

## Project Overview
This project analyzes a large Weather Dataset to extract insights about temperature trends, wind patterns, and specific weather conditions (like Fog or Clear skies). The goal was to move away from standard loops and utilize **NumPy's vectorized operations** for efficient data processing.

## Technical Highlights
* **Vectorization:** Converted temperature units for the entire dataset instantly without using `for` loops.
* **Boolean Masking:** Implemented filter logic to isolate specific conditions (e.g., `temperatures < 0`).
* **Complex Querying:** Used Bitwise AND operators (`&`) to find events that met multiple criteria simultaneously (High Wind + Freezing Temps).
* **Conditional Aggregation:** calculated separate statistics for different weather labels (e.g., Median Humidity specifically during 'Fog').

## How to Run
1. Ensure `Weather Dataset.csv` is in the directory.
2. Run the script:
   ```bash
   python main.py
   
