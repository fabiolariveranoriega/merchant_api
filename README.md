# End-to-End E-Commerce Data Analysis Pipeline

## Project Overview

This project is an end-to-end data analysis pipeline built using real-world customer transaction data from a UK-based, registered online retail store. The goal of the project is to ingest, store, visualize, and analyze e-commerce data in a modular way. 

The pipeline ingests data through an API, stores it in a MySQL database, and connects the data to Tableau for interactive dashboards and business insights. The entire system is fully dockerized to ensure reproducibility and ease of deployment on other systems. The current implementation was tested on [E-Commerce Data](https://www.kaggle.com/datasets/carrie1/ecommerce-data), but it is extensible to other transaction datasets.

---

### Project Workflow

```bash
MERCHANT_API/
├─ images/
├─ data/
├─ config.py                    # Configuration for parameters
├─ data_loader.py
├─ data_validation.py           # Data validation
├─ database.py                  # Database connections
├─ docker-compose.yml
├─ Dockerfile
├─ entry point.sh
├─ ingest.py                    # Load data to database
├─ main.py                      # API
├─ README.md
```

## Architecture Overview

**High-level flow:**

1. Raw e-commerce transaction data
2. API ingestion service
3. MySQL relational database
4. Tableau dashboards and insights
5. Docker for containerized deployment


---

## Technologies Used

- **Python** – API development and data ingestion
- **FastAPI** – REST API for data ingestion
- **MySQL** – Relational database for structured storage
- **Tableau** – Data visualization and dashboard creation
- **Docker & Docker Compose** – Containerization and orchestration

---

## Dataset

- Real-world **e-commerce transaction data**
- Customers from a **UK-based online retail company**
- Includes information such as:
  - Invoice details
  - Product descriptions
  - Quantities and prices
  - Customer IDs
  - Transaction timestamps

---

## Tableau Dashboards & Insights

<img src="images/European Sales Overview.png" alt="Customer and Return Insights" width="800">

### 1. Overall Sales Performance

European sales show strong overall performance with more than 5.1 million units sold and nearly £9.0 million in net revenue. The sales per month fluctuated slightly throughout most of the year, but saw a large spike towards the end of the year, followed by a sharp decline immediately after. This oscillation between high and low in a short time period likely reflects year-end demand, promotions, or end of year bulk-purchases. Because of this strong decline, we can see that there exists an opportunity to pull demand forward through earlier promotions or subscription-style purchasing incentives. 

### 2. Geographic Revenue Concentration

Net revenue across Europe is heavily concentrated in the U.K. (> £7.5 million), while all other European countries contribute only marginally. Evidently, the company has achieved strong market hold in the U.K. but has yet to scale effectively across the rest of Europe. This can lead to geographic risk and limit growth potential. Future efforts can focus on underperforming but high-potential markets such as Germany and France that could significantly increase total revenue, while also reducing the dependency on a single country. Future efforts can also focus on identifying countries with similar societal and economical identities to the U.K. For example, The Netherlands is also a highly developed country with strong international trade, high English proficiency and similar consumer expectations around quality and pricing.


<img src="images/Customer and Return Insights.png" alt="Customer and Return Insights" width="800">

### 3. Customer Behavior and Retention Strength

Repeat customers make up 72% of the customer population and generate a majority of the revenue, contributing over £8.5 million compared to just £406k from one-time customers. Additionally, customers place an average of 6.1 orders and generate £2,289 each, which shows repeat engagement and satisfaction. These patterns show that customer lifetime value is a main factor in profitability, and that retention initiatives such as loyalty programs, personalized marketing, and post-purchase engagement can be considered to sustain revenue growth. 


### 4. Revenue Concentration by Customer and Growth Opportunities

Revenue is also concentrated among a relatively small group of high-value clients, with the top 10 customers contributing a disproportionately large amount of total net revenue. This can lead to some risk if a major customer reduces spending. At the same time, the strong performance of repeat customers can pave the path for future efforts to focus on. This suggests that we can focus on converting one-time buyers into repeat customers while also nurturing mid-tier clients into high-value accounts. This can aid in reducing the reliance on a small set of clients. 



---

## How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Start the services
```bash
docker-compose up --build
```
This will launch:
- FastAPI
- MySQL database

#### A. API Endpoints
| Method | Endpoint        | Description                                                  |
|--------|-----------------|--------------------------------------------------------------|
| GET    | `/health`       | Health check endpoint to verify the API is running           |
| GET    | `/transactions` | Retrieves e-commerce transaction data from the database      |
| POST   | `/ingest`       | Ingests raw e-commerce data into the MySQL database          |


### 3. Connect to Tableu
Connect to MySQL from Tableu using the database connection parameters.

### 4. Stop the services
```bash
docker compose down -v
```

