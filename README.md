# Maven Fuzzy Factory E-Commerce Analysis

A business-focused analytics case study built on the Maven Fuzzy Factory e-commerce dataset. This project examines how the business grew between March 2012 and March 2015, which channels drove scale versus efficiency, how product expansion affected basket economics, and where conversion and refund issues still limited performance.

## Business Problem
Maven Fuzzy Factory experienced strong growth over a three-year period, but growth alone is not enough. The goal of this project was to identify:

- how traffic, orders, and revenue changed over time
- which marketing channels drove scale and which delivered higher-quality traffic
- whether product expansion improved order economics
- where customer conversion was being constrained
- which products created refund risk and weakened net revenue quality

## Dataset
Time coverage:
- March 2012 to March 2015

Core tables used:
- `website_sessions`
- `website_pageviews`
- `orders`
- `order_items`
- `order_item_refunds`
- `products`

High-level data volume:
- 472,871 website sessions
- 1,188,124 pageviews
- 32,313 orders
- 40,025 order items
- 1,731 refunded order items
- 4 products

## Tools
- Python
- SQLite
- SQL
- Power BI
- Markdown / DOCX documentation

## Project Workflow
This project followed a practical analytics workflow rather than jumping directly into dashboarding.

1. **Data ingestion**  
   Raw CSV files were collected and loaded into a local SQLite database.

2. **Validation**  
   Row counts, joins, time coverage, and aggregation sanity checks were reviewed before analysis began.

3. **Transformation**  
   Monthly summary outputs were created for trend analysis, channel comparison, product analysis, and refund review.

4. **Analysis**  
   SQL was used to answer the core business questions around growth, channel efficiency, conversion, product mix, and refund quality.

5. **Visualization**  
   Power BI was used to organize the findings into stakeholder-friendly dashboard pages.

6. **Recommendation building**  
   Final outputs focused on business actions, not just charts.

## Data Pipeline
`CSV files -> SQLite database -> SQL analysis -> summary outputs -> Power BI dashboard -> business recommendations`

## Data Quality Checks
Before writing conclusions, the following checks were completed:

- verified row counts after loading each raw table into SQLite
- confirmed expected table coverage across sessions, pageviews, orders, order items, refunds, and products
- tested joins between:
  - sessions and orders
  - orders and order items
  - order items and refunds
  - order items and products
- validated minimum and maximum dates for sessions and orders
- checked that monthly trend outputs were directionally consistent across sessions, orders, conversion, and revenue
- reviewed whether key KPI values were commercially plausible after aggregation
- checked metric scaling issues during BI visualization and corrected numeric formatting and transformation logic where needed

## Key Findings
### 1. Growth came from both scale and efficiency
The business did not grow by traffic acquisition alone. Sessions increased substantially, but orders grew even faster, showing that conversion performance also improved.

### 2. Nonbrand paid search scaled growth, but higher-intent traffic monetized better
Paid nonbrand search contributed the most volume, while brand, direct, and organic traffic produced stronger conversion and revenue efficiency.

### 3. Mobile was the clearest performance gap
Desktop conversion materially outperformed mobile conversion, making mobile experience one of the largest optimization opportunities.

### 4. Product expansion improved basket economics
As the catalog expanded, average order value increased and multi-item baskets became more valuable.

### 5. Not all product growth was equally healthy
Some products generated stronger refund pressure, meaning gross sales alone were not enough to judge performance quality.

### 6. Revenue remained concentrated in the flagship product
The Original Mr. Fuzzy remained the main revenue driver, which is both a strength and a concentration risk.

## Dashboard

![Cyclistic Dashboard](C:\Users\Emir\Documents\GitHub\toy-store-ecommerce-analysis\outputs\charts)


## Recommendations
1. Prioritize mobile conversion optimization.
2. Expand cross-sell and bundling strategy.
3. Re-evaluate low-quality acquisition channels.
4. Investigate high-refund SKUs for expectation or quality issues.

## Limitations
- No advertising spend data was available, so true ROI and CPA could not be calculated.
- No demographic or geographic customer detail was available.
- No explicit return-reason field was available for root-cause diagnosis.
- Product launch effects were interpreted directionally, not as strict causal proof.
- Repeat purchase analysis was limited by the observation window.

## Lessons Learned
- Good SQL alone is not enough. Aggregation logic and BI formatting can still distort the story.
- Business metrics that look reasonable in a query can still be displayed incorrectly in dashboard tools if numeric scaling is not validated.
- Product expansion can improve average order value, but refund quality must be checked before calling expansion a success.
- Channel volume and channel quality are different things and should be analyzed separately.
- A strong portfolio project needs both analysis quality and packaging discipline.

## Repository Structure
```text
toy_store/
├── data/
│   ├── raw/
│   └── toy_store.db
├── sql/
│   ├── 01_growth_trends.sql
│   ├── 02_channel_analysis.sql
│   ├── 03_device_analysis.sql
│   ├── 04_product_analysis.sql
│   └── 05_refund_analysis.sql
├── powerbi/
│   └── toy_store_dashboard.pbix
├── outputs/
│   ├── charts/
│   └── summary_tables/
├── docs/
│   ├── case_study_report.md
│   └── toy_store_findings_summary.docx
└── README.md
```

## Project Status
Core analysis completed. Documentation and dashboard packaging are being refined for final portfolio presentation.
