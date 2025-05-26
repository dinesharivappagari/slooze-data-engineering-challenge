# 🛠️ Slooze Data Engineering Take-Home Challenge

## 📦 Project Overview

This project demonstrates my ability to collect, clean, and analyze real-world product listing data from an online B2B marketplace (IndiaMART). The challenge is divided into two main parts:

- **Part A: Web Scraping**
- **Part B: Exploratory Data Analysis (EDA)**

---

## ✅ Part A: Web Scraping

Due to dynamic rendering and access limitations, scraping directly using static libraries (requests + BeautifulSoup) was not effective. I pivoted to using **Selenium with ChromeDriver** to simulate a browser and extract product data such as:

- Product Name
- Price
- Location

**File:** `crawler/indiamart_scraper.py`

**Output File:** `data/industrial_machinery.csv`

---

## 📊 Part B: EDA & Insights

Using the scraped dataset (or a realistic sample), I cleaned and analyzed the data using:

- **Pandas** for manipulation
- **Seaborn/Matplotlib** for visualizations

### 🔍 Key Insights
- Price Distribution of Machines
- Top Cities by Number of Listings
- Average Price by City
- High-Priced Product Outliers
- Most Frequent Product Keywords

**Notebook:** `EDA_Industrial_Machinery.ipynb`  
**Clean CSV:** `data/cleaned_industrial_machinery.csv`

---

## 📂 Folder Structure

```
slooze_project/
│
├── crawler/
│   └── indiamart_scraper.py
│
├── data/
│   ├── industrial_machinery.csv
│   └── cleaned_industrial_machinery.csv
│
├── EDA_Industrial_Machinery.ipynb
├── README.md
└── requirements.txt
```

---

## 🚀 How to Run

1. Clone this repo or unzip the project folder.
2. Install dependencies:
   ```bash
   pip install selenium pandas matplotlib seaborn
   ```
3. Download the matching ChromeDriver for your version and place it in the root.
4. Run the scraper:
   ```bash
   python crawler/indiamart_scraper.py
   ```
5. Open and run the EDA notebook:
   ```bash
   jupyter notebook EDA_Industrial_Machinery.ipynb
   ```
