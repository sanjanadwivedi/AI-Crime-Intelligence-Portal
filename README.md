# 🛡️ AI Crime Intelligence Portal

🌐 **Live Demo:** https://ai-crime-predictive-analysis.streamlit.app/

💻 **GitHub Repository:** https://github.com/sanjanadwivedi/AI-Crime-Intelligence-Portal

An AI-powered web application that analyzes historical crime data, predicts future crime trends, and visualizes crime statistics through interactive dashboards and maps.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![Plotly](https://img.shields.io/badge/Plotly-Interactive-success)

---

## 📌 Overview

The AI Crime Intelligence Portal is designed to help users explore historical crime trends, visualize crime statistics, and forecast future crime levels using machine learning.

The application provides an intuitive dashboard with interactive charts, forecasting, heatmaps, and an AI-based prediction system, making crime analytics more accessible for researchers, students, and decision-makers.

---

## ✨ Features

- 📊 Interactive Crime Dashboard
- 🤖 AI Crime Prediction
- 📈 Crime Forecasting
- 🗺️ India Crime Heatmap
- 📉 Crime Analytics & Trends
- 📂 Dataset Upload (Admin Panel)
- 💾 Download Processed Dataset
- 🌙 Modern Dark Theme UI

---

## 🧠 Machine Learning

The prediction model is trained using historical NCRB crime data.

### Workflow

- Data Collection
- Data Cleaning & Preprocessing
- Feature Selection
- Model Training
- Crime Prediction
- Visualization

---

## 📂 Project Structure

```text
crime-project-portal/
│
├── app_streamlit.py
├── train_model.py
├── requirements.txt
├── README.md
├── india_states.geojson
├── state_name_map.json
│
├── data/
│   ├── 2000-22.xlsx
│   └── Total IPC Crimes byState_UT(2011-2022).xlsx
│
├── models/
│   └── crime_model.pkl
│
└── uploads/
```

---

## 🚀 Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Plotly
- Folium
- OpenPyXL
- Joblib

---

## 📊 Dataset

The project uses crime datasets based on NCRB (National Crime Records Bureau) reports.

Dataset includes:

- Murder
- Robbery
- Theft
- Burglary
- Kidnapping
- Rape
- Riots
- Dowry Deaths
- Other IPC Crimes

along with yearly crime statistics for analysis and prediction.

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/sanjanadwivedi/crime-project-portal.git
```

Go inside the project

```bash
cd crime-project-portal
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app_streamlit.py
```

---

## 📷 Screenshots

### Dashboard

![Dashboard](screenshots/dashboard.png)

---

### AI Prediction

![Prediction](screenshots/prediction.png)

---

### Crime Analytics

![Analytics](screenshots/analytics.png)

---

### Forecasting

![Forecasting](screenshots/forecasting.png)

---

### Heatmap

![Heatmap](screenshots/heatmap.png)

---

### Admin Panel

![Admin Panel](screenshots/admin.png)

---

## 🎯 Future Enhancements

- Multi-user authentication
- Live crime dataset integration
- Advanced forecasting models
- Cloud deployment
- Automated report generation

---

## 👩‍💻 Developer

**Sanjana Dwivedi**

B.Sc. (Hons.) Computer Science

Passionate about Data Analytics, Machine Learning, and AI-powered applications.

---

## ⭐ If you found this project useful, consider giving it a star!
