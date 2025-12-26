# web_scrapping-data_analysis
**web_scrapping-data_analysis** is an exploratory data analysis (EDA) project that uses data extracted from the previous web scraping project [top-jobs-scraper](https://github.com/dpm24800/top-jobs-scraper). It focuses on cleaning, transforming, and visualizing job listing data to uncover insights about job posts, companies, experience requirements, salary trends, and more.

---

## Project Structure
```
web_scrapping-data_analysis/
├── data-cleaner.py          # Cleans and preprocesses scraped job data
├── web-scrapping-eda.py     # Performs EDA and generates visualizations
├── cleaned_top_jobs.csv     # Exported cleaned dataset
├── README.md
```

---

## Features
### 1. Data Cleaning (`data-cleaner.py`)
* Standardizes column names and formats.
* Encodes `experience` and `level` into numeric values.
* Extracts date components (year, month, day) from deadlines.
* Parses salary strings into numeric columns: `salary_min`, `salary_max`, `salary_avg`.
* Exports cleaned dataset to `cleaned_top_jobs.csv`.

### 2. Exploratory Data Analysis (`web-scrapping-eda.py`)
* Dataset overview and summary statistics (numerical & categorical).
* Missing value analysis.
* **Univariate Analysis**: Top job posts, top companies, experience distribution, job level distribution.
* **Bivariate Analysis**: Average salary per job level.
* **Correlation Analysis**: Heatmap of numerical features.

---

## Visualizations
* Top posts and companies (horizontal bar charts).
* Experience requirements distribution.
* Job levels distribution (Entry, Medium, Senior, Top).
* Average salary vs job level (scatter plot with labels).
* Correlation heatmap of numerical features.

---

## Getting Started

1. **Clone the repository**

```bash
git clone https://github.com/dpm24800/web_scrapping-data_analysis.git
cd web_scrapping-data_analysis
```

2. **Install dependencies**

```bash
pip install pandas numpy matplotlib seaborn
```

3. **Run the data cleaner**

```bash
python data-cleaner.py
```

4. **Perform EDA**

```bash
python web-scrapping-eda.py
```

---

## Notes

* This project relies on `top-jobs-scraper` for the raw job listing data.
* Visualizations are generated using `matplotlib` and `seaborn`
