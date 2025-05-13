# 🌍 COVID-19 Global Data Tracker

![Dashboard Preview](https://i.imgur.com/JQ8W0xl.png) 

A Streamlit-powered dashboard and Jupyter Notebook analysis tracking global COVID-19 trends (cases, deaths, vaccinations) using real-time data from Our World in Data.

## 🚀 Features

- **Interactive Dashboard**
  - Country comparison tool
  - Timeseries visualization
  - Vaccination progress tracking
- **Data Analysis**
  - Exploratory Data Analysis (EDA)
  - Death rate calculations
  - Choropleth world maps
- **Automation Ready**
  - Daily data refresh capability

## 📦 Project Structure
covid19-tracker/
├── data/ # Dataset storage
│ └── owid-covid-data.csv
├── dashboard/ # Streamlit files
│ ├── app.py # Main dashboard
│ └── helpers.py # Shared functions
├── analysis.ipynb # Jupyter Notebook analysis
├── requirements.txt # Python dependencies
└── README.md # This file


## 🛠️ Installation

1. **Clone repository**
   ```bash
   git clone https://github.com/yourusername/covid19-tracker.git
   cd covid19-tracker

2. **Install dependencies**
    pip install -r requirements.txt

▶️ Usage
  **Local Development**
    Jupyter Notebook Analysis:

  '''bash
  jupyter notebook analysis.ipynb
  Streamlit Dashboard:

'''bash
    cd dashboard
    streamlit run app.py


