# 🏗️ Project Architecture — Sales Analytics Pipeline

## Overview
This project demonstrates a simple **data analytics pipeline** that processes sales data, performs ETL operations, and visualizes results through notebooks and dashboards.

---

## 🔄 Data Flow Diagram

RRaw Orders CSV  
│  
▼  
ETL Script (Pandas/PySpark)  
│  
▼  
Aggregated Sales Data (by Month, by Product)  
│  
▼  
Exploratory Analysis Notebook (Matplotlib / Seaborn)  
│  
▼  
Dashboard Notebook (Plotly)


---

## 🧰 Components
- **data/** → Contains raw and processed data files.
- **scripts/** → ETL logic for cleaning and aggregating data.
- **notebooks/** → Jupyter notebooks for exploratory and dashboard analysis.
- **docs/** → Documentation and architecture overview.
