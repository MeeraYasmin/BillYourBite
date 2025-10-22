# BillYourBite 🍽️

**BillYourBite** is an AI agent–powered meal billing system designed to bring **fairness, transparency, and automation** to university dining. Students pay only for what they actually consume, while administrators get actionable insights to optimize operations and reduce food waste.

---

## 🌟 Features

- **Student Registration**: Capture student name, registration number, department, and year.  
- **Personalized Billing**: Track meal attendance and compute real-time bills.  
- **AI Agent Automation (Kiro)**:  
  - Orchestrates workflows like meal attendance logging and bill calculation.  
  - Maintains smooth automation between frontend, data layer, and computations.  
- **Interactive Dashboard**: Streamlit interface to select meals, quantities, and view summaries.  
- **Data Management**: Menu, attendance, and billing stored in structured Pandas DataFrames.  
- **Visualization**: Track attendance patterns, most consumed/skipped meals, and weekly trends.  
- **Downloadable Bill**: Export personalized CSV summaries.  
- **Rating & Feedback**: Rate dishes and provide comments to improve the mess experience.

---

## 🛠️ Installation

1. **Clone the repository**
   git clone https://github.com/MeeraYasmin/BillYourBite.git
cd BillYourBite

2. **Install dependencies**
  pip install -r requirements.txt

3. **Run the app**
   streamlit run app.py

---
## 📂 Data

**mess_menu.csv**: Synthetic dataset of campus mess menu with columns:
Week_Type, Day, Meal_Type, Dish_Name, Average_Price

**Attendance & Billing**: Managed internally in Pandas DataFrames, dynamically updated by the Kiro agent.

---
## ⚡ Technology Stack

**Frontend**: Streamlit

**Backend Automation**: Kiro AI agent

**Data Management**: Pandas

**Dataset**: Custom synthetic CSV based on real mess menu
---




cd BillYourBite
