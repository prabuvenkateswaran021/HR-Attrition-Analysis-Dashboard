# 📊 HR Attrition Analysis Dashboard

![Dashboard Preview](https://img.shields.io/badge/Dashboard-Interactive-blue?style=for-the-badge&logo=html5)
![Chart.js](https://img.shields.io/badge/Chart.js-4.4.1-FF6384?style=for-the-badge&logo=chartdotjs)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

---

## 📌 Project Overview

This project analyzes **employee attrition** in an organization to uncover patterns, identify high-risk segments, and provide actionable insights for HR teams to improve **workforce retention**.

The project replicates a **Power BI-style interactive dashboard** built entirely with HTML, CSS, and Chart.js — making it fully viewable in any browser without any software installation.

> **Dataset:** IBM HR Analytics Employee Attrition & Performance  
> **Total Records:** 1,470 employees  
> **Attrition Count:** 237 employees (16.1%)

---

## 🎯 Project Objectives

- Analyze overall employee attrition rate and distribution
- Visualize workforce **demographics** (gender, marital status, dependents)
- Understand the impact of **tenure** on attrition risk
- Identify key **churn drivers** (overtime, income, travel, satisfaction scores)
- Build a fully interactive, multi-tab **dashboard** for HR decision-making

---

## 📁 Repository Structure

```
HR-Attrition-Analysis/
│
├── 📊 HR_Attrition_Dashboard.html     # Interactive dashboard (open in browser)
├── 📓 HR_Attrition_Analysis.py        # Python data analysis & EDA script
├── 📂 HR_Attrition_Analysis.xlsx      # Source dataset
└── 📄 README.md                       # Project documentation (this file)
```

---

## 🚀 How to Run

### Option 1 — View the Dashboard (No Installation Needed)
1. Download `HR_Attrition_Dashboard.html`
2. Open it in any modern browser (Chrome, Firefox, Edge, Safari)
3. All 4 tabs are fully interactive — no server or software required

### Option 2 — Run the Python Analysis
```bash
# 1. Clone the repository
git clone https://github.com/YOUR-USERNAME/HR-Attrition-Analysis.git
cd HR-Attrition-Analysis

# 2. Install dependencies
pip install pandas numpy matplotlib seaborn openpyxl

# 3. Run the analysis script
python HR_Attrition_Analysis.py
```

---

## 📊 Dashboard Tabs & Features

### Tab 1 — 📈 Overview
| Visual | Description |
|--------|-------------|
| **5 KPI Cards** | Attrition Rate, Total Employees, Total Attrition, Active Employees, Avg Income |
| **Donut Chart** | Overall attrition rate (16.1%) — Yes vs No |
| **Bar Chart** | Attrition count by Department |
| **Horizontal Bar** | Top job roles by attrition rate |
| **Stacked Bar** | Job satisfaction score vs attrition (1–4 scale) |
| **Donut Chart** | Business travel frequency vs churn |

### Tab 2 — 👥 Demographics
| Visual | Description |
|--------|-------------|
| **Pie Chart** | Gender distribution (Male 60% / Female 40%) |
| **Donut Chart** | Marital status breakdown |
| **Stacked Bar** | Dependent count vs attrition |
| **Stacked Bar** | Gender × Attrition split |
| **Progress Bars** | Attrition rate by marital status & education field |

### Tab 3 — 📅 Tenure Analysis
| Visual | Description |
|--------|-------------|
| **Histogram** | Distribution of years at company |
| **Line Chart** | Attrition rate trend by tenure cohort |
| **Bar Chart** | Years since last promotion distribution |
| **Stacked Bar** | Age group × Attrition |
| **Stats Panel** | Avg tenure, median, highest risk window, manager tenure |

### Tab 4 — 🔍 Churn Factors
| Visual | Description |
|--------|-------------|
| **Stacked Bar** | Overtime vs No Overtime attrition comparison |
| **Bar Chart** | Monthly income bracket vs attrition rate |
| **Heatmap** | Department × Job Level attrition intensity |
| **Bar Charts** | Work-Life Balance & Environment Satisfaction scores |
| **Risk Table** | Top high-risk employee segments |

---

## 🔍 Key Findings

| Finding | Detail |
|---------|--------|
| 🔴 **Overall Attrition** | 16.1% — 237 of 1,470 employees left |
| 🔴 **Highest Risk Role** | Sales Representatives at **39.8%** attrition rate |
| 🔴 **Overtime Impact** | Employees working overtime churn at **30.5%** vs 10.4% |
| 🔴 **Tenure Risk Window** | First **0–2 years** has the highest churn (34%) |
| 🔴 **Income Correlation** | Employees earning **<$2K/month** churn at 38.1% |
| 🟡 **Marital Status** | Single employees churn at **2× the rate** of married ones |
| 🟡 **Travel Frequency** | Frequent travelers churn at **24.9%** vs 8% for non-travelers |
| 🟢 **Lowest Risk Role** | Research Directors at only **2.5%** attrition |

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| **HTML5 / CSS3** | Dashboard structure and styling |
| **JavaScript (ES6+)** | Interactivity and tab switching |
| **Chart.js 4.4.1** | All charts and visualizations |
| **Python 3.x** | Data analysis and preprocessing |
| **Pandas** | Data manipulation and aggregation |
| **NumPy** | Numerical computation |
| **Matplotlib / Seaborn** | Static Python visualizations |
| **OpenPyXL** | Excel file reading |

---

## 📈 Dashboard Screenshots

> Open `HR_Attrition_Dashboard.html` in your browser to view the live interactive version.

**Overview Tab** — KPIs, attrition rate donut, department & role breakdowns  
**Demographics Tab** — Gender, marital status, education field analysis  
**Tenure Tab** — Histogram, tenure vs churn line chart, age distribution  
**Churn Factors Tab** — Overtime impact, income heatmap, risk table  

---

## 📂 Dataset Description

The dataset contains **1,470 rows** and **35 columns** covering:

| Category | Columns |
|---------|---------|
| **Demographics** | Age, Gender, MaritalStatus, NumCompaniesWorked |
| **Job Info** | Department, JobRole, JobLevel, BusinessTravel |
| **Compensation** | MonthlyIncome, PercentSalaryHike, StockOptionLevel |
| **Performance** | PerformanceRating, TrainingTimesLastYear |
| **Satisfaction** | JobSatisfaction, EnvironmentSatisfaction, WorkLifeBalance |
| **Tenure** | YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion |
| **Target** | **Attrition** (Yes / No) |

---

## 💡 Business Recommendations

1. **Retention Bonuses** for employees in their first 2 years of tenure
2. **Overtime Policy Review** — employees on overtime have 3× higher churn
3. **Sales Rep Engagement Programs** — 39.8% attrition is critically high
4. **Salary Benchmarking** for employees earning below $2,000/month
5. **Travel Reduction Initiatives** for frequent business travelers
6. **Single Employee Wellness Programs** to improve engagement

---

## 🤝 Contributing

Contributions are welcome!

```bash
# Fork → Clone → Create feature branch → Commit → Push → Pull Request
git checkout -b feature/your-feature-name
git commit -m "Add: your feature description"
git push origin feature/your-feature-name
```

---

## 📜 License

This project is open source under the [MIT License](LICENSE).

---

## 👤 Author

**HR Attrition Analysis Project**  
Built as part of a Data Analytics internship project  
Dashboard replicates Power BI methodology using open web technologies

---

> ⭐ If you found this project helpful, please consider giving it a star!


https://prabuvenkateswaran021.github.io/HR-Attrition-Analysis-Dashboard/
