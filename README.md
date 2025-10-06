# Netflix Duration Analysis

This small project analyzes a Netflix dataset and produces a histogram of movie durations for titles released between 1991 and 1998.

Files
- `netflix.py` — Python script that loads `netflix_data.csv`, filters movies released in 1991–1998, counts short Action movies, and displays a styled histogram of movie durations.
- `netflix_data.csv` — Expected CSV dataset (not included in this repo). The script expects this file to be in the same directory as `netflix.py`.
- `requirements.txt` — Python package requirements (created alongside this README).

Quick summary of what `netflix.py` does
- Reads `netflix_data.csv` into a pandas DataFrame.
- Filters movies with `release_year` between 1991 and 1998 (inclusive boundaries in the code are >1990 and <1999).
- Filters action movies and counts how many have `duration` < 90 minutes (the count is computed in the script but not printed).
- Plots a histogram of durations for the filtered set, with a vertical marker at 100 minutes and several styling tweaks.

Required columns in `netflix_data.csv`
- `release_year` (numeric)
- `genre` (string)
- `duration` (numeric, minutes)

Prerequisites
- Python 3.8+ recommended
- The following Python packages (install with pip):
  - pandas
  - matplotlib
  - numpy

Install dependencies

PowerShell (Windows):
```
python -m pip install -r requirements.txt
```

Or install directly:
```
python -m pip install pandas matplotlib numpy
```

How to run
1. Place `netflix_data.csv` in the same folder as `netflix.py`.
2. From that folder, run (PowerShell):
```
python .\netflix.py
```é

Expected behavior
- The script will open a matplotlib window showing a histogram of movie durations for the 1991–1998 range. The plot is styled and includes a dashed vertical line at 100 minutes.

Notes and suggestions
- The script currently computes `short_movie_count` for Action movies under 90 minutes but does not print or save it. If you want to see that value, add a print statement (e.g., `print(short_movie_count)`) or write it to a log/file.
- If `netflix_data.csv` contains missing or malformed values for the required columns, the script may raise errors. Consider adding type checks / NaN handling before filtering.
- To save the histogram to a file, replace `plt.show()` with `plt.savefig('duration_histogram.png', dpi=300)` (or call both: save then show).

Possible next improvements
- Add CLI flags to choose year ranges, genres, or to save figures automatically.
- Add automated tests for the data-loading and filtering logic.
- Export results (counts and summary statistics) to CSV or JSON.

License
This README and the small helper files are provided under the MIT License.

Contact
If you want changes to the README or help extending the script, reply with what you'd like to add.
