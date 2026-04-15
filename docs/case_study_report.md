# Maven Fuzzy Factory E-Commerce Analysis

## Growth, Channel Efficiency, Device Performance, and Product Portfolio Health

**Prepared by:** Emir Polat  
**Date:** April 2026  
**Analysis Period:** March 2012 to March 2015

---

## 1. Business Problem

Maven Fuzzy Factory is an online teddy bear retailer. The goal of this case study is to understand how the business grew over time and which factors most influenced commercial performance.

The core questions were:

- Did the business grow only by attracting more traffic, or did efficiency improve as well?
- Which channels drove scale, and which channels delivered higher-quality traffic?
- How large is the mobile performance gap?
- Did product expansion improve order economics?
- Which products created healthy revenue, and which products carried higher refund risk?

---

## 2. Dataset and Scope

This project used seven relational tables from the Maven Fuzzy Factory e-commerce database:

- `website_sessions`
- `website_pageviews`
- `orders`
- `order_items`
- `order_item_refunds`
- `products`
- `maven_fuzzy_factory_data_dictionary`

### Data coverage

- **472,871** website sessions
- **1,188,124** pageviews
- **32,313** orders
- **40,025** order items
- **1,731** refunded items
- **4** products
- Time period from **March 2012 to March 2015**

---

## 3. Tools and Workflow

### Tools used

- **Python** for file handling and database loading
- **SQLite** for relational querying
- **Power BI** for dashboard design
- **Markdown / DOCX** for case study documentation

### Project workflow

1. Raw CSV files were collected and organized.
2. Data was loaded into SQLite.
3. Core table relationships were validated.
4. SQL queries were written for growth, channel, device, product, and refund analysis.
5. Aggregated outputs were reviewed and exported.
6. Final business findings were translated into a dashboard and written case study.

### Architecture summary

**CSV files → SQLite → SQL analysis → Power BI dashboard → business recommendations**

---

## 4. Data Quality Checks

Before interpreting business results, the data structure and outputs were validated.

### Validation steps completed

- Raw tables were loaded into SQLite and row counts were verified.
- Key joins were tested across sessions, orders, order items, refunds, and products.
- Session and order date ranges were checked for consistency.
- Monthly trend outputs were reviewed against source aggregations.
- KPI calculations and BI display logic were manually validated.

### Why this matters

This project included multiple related tables and several derived KPIs. Without validating joins, date ranges, and aggregation logic, it would have been easy to produce attractive but misleading conclusions.

---

## 5. Method

This analysis followed a practical version of the Google Data Analytics process:

- **Ask**: Define the business questions
- **Prepare**: Organize the raw files and understand the schema
- **Process**: Load data into SQLite and test relationships
- **Analyze**: Build SQL queries for business metrics and segmentation
- **Share**: Summarize insights in written form and dashboard pages
- **Act**: Translate findings into business recommendations

This project prioritized business clarity over technical showmanship.

---

## 6. Key Findings

### Finding 1. Growth came from both scale and improved efficiency

The business did not grow only because more people visited the site. It also became better at monetizing traffic.

- Sessions increased from roughly **1,879** to more than **23,000** monthly
- Orders increased from **60** to more than **2,000** monthly
- Conversion rate improved from **3.19%** to **8.69%**
- Revenue per session increased from **$1.60** to **$5.43**

**Interpretation:** Maven Fuzzy Factory improved both traffic volume and commercial efficiency over time.

---

### Finding 2. Paid nonbrand search drove scale, but brand, direct, and organic traffic were more efficient

The channel mix showed a clear split between **volume drivers** and **quality drivers**.

- **gsearch nonbrand** was the largest source of sessions and orders
- **brand search**, **organic**, and **direct** traffic had higher conversion rates and stronger revenue per session
- **socialbook** underperformed on conversion and revenue efficiency relative to other channels

**Interpretation:** The business relied on nonbrand search to scale, but higher-intent channels monetized traffic more effectively.

---

### Finding 3. Mobile is the clearest performance gap

Device performance revealed the biggest optimization opportunity in the business.

- Desktop conversion rate: **8.50%**
- Mobile conversion rate: **3.09%**

This gap persisted across major channels.

**Interpretation:** Mobile traffic was meaningful in volume but substantially weaker in monetization. Future growth will likely depend more on fixing the mobile experience than simply buying more traffic.

---

### Finding 4. Product expansion improved basket economics

As the product portfolio expanded, order economics improved.

- One-item orders averaged **$50.82**
- Two-item orders averaged **$89.25**
- Revenue per order increased after product expansion
- Revenue per session also improved during launch periods

**Interpretation:** New products did not just add catalog depth. They increased basket value and improved commercial efficiency.

**Important caution:** Launch-period improvements aligned with product expansion, but they should not be treated as pure causation. Channel mix changes, site changes, and seasonality may also have contributed.

---

### Finding 5. Product quality varied across the portfolio

Not all revenue was equally healthy.

Refund rates showed meaningful differences by product:

- **Birthday Sugar Panda**: **6.04%** refund rate
- **Original Mr. Fuzzy**: **5.11%**
- **Forever Love Bear**: **2.23%**
- **Hudson River Mini Bear**: **1.28%**

**Interpretation:** Some SKUs generated more friction after purchase. Gross revenue alone was not enough to judge product performance.

---

### Finding 6. The flagship product remained dominant, but concentration risk exists

The Original Mr. Fuzzy remained the core product and the main revenue driver.

**Interpretation:** A strong flagship is valuable, but revenue concentration around one SKU creates strategic risk. Product diversification improved economics, but the business still depended heavily on its core product.

---

## 7. Deep Dive Sections

### 7.1 Growth Trends

The company experienced substantial growth in traffic and orders over the analysis period. The important point was not just volume growth, but the fact that efficiency metrics improved at the same time.

This means the business matured commercially rather than merely spending more to generate traffic.

### 7.2 Marketing Performance

Paid nonbrand search was the scale engine. It brought the largest volume of traffic and the highest order count.

However, not all channels were equally valuable. Brand, organic, and direct traffic showed better monetization. This suggests that demand already familiar with the brand was more likely to convert and produce stronger revenue efficiency.

This channel split is strategically important:

- some channels bring volume
- others bring quality

A good acquisition strategy should understand both roles.

### 7.3 Device Performance

The desktop versus mobile gap was the most actionable performance issue in the project.

Mobile did not simply underperform slightly. It lagged at a structural level. That makes mobile optimization a more attractive growth lever than simply increasing acquisition.

### 7.4 Product Portfolio Performance

Product expansion improved average order value and likely supported cross-sell behavior.

The Hudson River Mini Bear appeared especially useful as a lower-price companion item. The Forever Love Bear also showed strong margin quality. This suggests that product strategy was not just about adding more SKUs, but about improving the economics of each order.

### 7.5 Refund and Net Revenue Quality

Refund behavior added an important layer of realism to the analysis. A product with strong gross revenue can still be weaker in net commercial terms if refund rates are high.

This is why Birthday Sugar Panda and Original Mr. Fuzzy require more scrutiny than a simple revenue chart would suggest.

---

## 8. Business Recommendations

### Recommendation 1. Prioritize mobile conversion optimization

Mobile performance is the clearest revenue leakage point.

Suggested actions:

- audit mobile landing pages
- simplify mobile navigation and checkout
- improve mobile page speed
- test device-specific UX changes

### Recommendation 2. Expand cross-sell and bundle strategy

The rise in average order value for multi-item purchases shows that cross-sell mechanics work.

Suggested actions:

- bundle flagship and companion products
- show “pair with” recommendations on product pages
- test cart and checkout cross-sell modules

### Recommendation 3. Rebalance acquisition focus toward higher-quality traffic

Paid nonbrand search remains important for scale, but weaker channels should be reconsidered.

Suggested actions:

- reassess low-efficiency social acquisition
- protect and strengthen brand search visibility
- support direct and organic demand generation

### Recommendation 4. Investigate high-refund SKUs

Sugar Panda and Original Mr. Fuzzy deserve further quality review.

Suggested actions:

- review product page clarity and imagery
- inspect fulfillment and handling issues
- look for expectation gaps between product promise and delivered experience

---

## 9. Limitations

This case study has several important limitations:

- No ad spend data was available, so true ROI and cost-per-acquisition could not be calculated.
- No customer demographic data was available for segmentation.
- No return-reason dataset was available, so refund analysis remained directional.
- Launch-period improvements should not be treated as pure causation.
- Repeat purchase analysis is limited by the observation window.

These limits do not invalidate the findings, but they do set boundaries on interpretation.

---

## 10. Lessons Learned

This project surfaced several practical lessons:

- Good SQL is not enough. Aggregation logic must also be validated carefully.
- BI tools can distort correct metrics if numeric formatting and display units are not checked.
- Product expansion can improve AOV, but refund behavior must also be reviewed before calling the strategy successful.
- A technically simple stack can still support a strong case study if the business framing is clear.

---

## 11. Conclusion

Maven Fuzzy Factory grew by combining traffic growth with meaningful gains in conversion and monetization efficiency.

The most important takeaway is that future performance improvement will likely come less from simply increasing traffic and more from improving **traffic quality**, **mobile conversion**, and **product portfolio health**.

This project shows that strong e-commerce analysis depends not only on identifying growth, but also on separating healthy growth from inefficient or fragile growth.
