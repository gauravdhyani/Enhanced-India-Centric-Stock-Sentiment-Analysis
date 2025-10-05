# Datasets Used in Enhanced India-Centric Stock Sentiment Analysis

---

# NifSent50: NIFTY 50 Stocks and News Dataset

## Overview
NifSent50 is a **comprehensive India-centric sentiment dataset** designed for **NIFTY 50** stock market analysis.  
It links **company-specific news and social media posts** to **subsequent stock price movements**, enabling sentiment classification tuned to the Indian market.

---

## Dataset Details
- **Companies Covered**: All NIFTY 50 stocks
- **Sources**: NewsAPI, Investing.com, Reddit (r/WorldNews, r/news, r/IndiaNews)
- **Stock Data**: Yahoo Finance (manual yearly merges for full historical coverage)
- **Sentiment Labels**:
  - `Positive` → Stock increased > 1% after news/post
  - `Negative` → Stock decreased > 1%
  - `Neutral` → Price change within ±1% or insufficient forward data

### Fields
| Field          | Description                  |
|----------------|------------------------------|
| `Company Name` | Full company name            |
| `Symbol`       | NSE stock ticker             |
| `Headline`     | News headline or Reddit post |
| `Publish Date` | Publication timestamp        |
| `Sentiment`    | Positive / Negative / Neutral|

---

## Data Construction
The dataset was built using three integrated pipelines:

1. **NewsAPI + Yahoo Finance**
   - Headlines fetched via NewsAPI for each company.
   - Stock prices sourced from Yahoo Finance (manual yearly merges).
   - Sentiment calculated from **post-news price changes**.

2. **Investing.com Scraper**
   - Headlines scraped using Selenium + BeautifulSoup.
   - Dates aligned with NIFTY 50 stock history.
   - Sentiment derived from **two-day percentage change** in stock price.

3. **Reddit Scrapers**
   - Posts from subreddits: r/WorldNews, r/news, r/IndiaNews.
   - Company mentions mapped via `Info.csv`.
   - Sentiment assigned based on **stock movement after publication**.

---

## Access
The full dataset is hosted on Kaggle:  
👉 [NifSent50 Dataset](https://www.kaggle.com/datasets/gauravdhyani/nifsent)

Clone/download it using the Kaggle API:

    ```bash
    kaggle datasets download -d gauravdhyani/nifsent
    unzip nifsent.zip -d data/
    ```
---

## External Datasets Referenced

### 1. [News Sentiment Analysis for Stock Data by Company](https://www.kaggle.com/datasets/sidarcidiacono/news-sentiment-analysis-for-stock-data-by-company)
- **Source**: Kaggle
- **Contents**: Headlines with stock symbol and sentiment label
- **Notes**: Mostly U.S. stocks. Useful for benchmarking and cross-market evaluation.

### 2. [Sentiment Analysis for Financial News](https://www.kaggle.com/datasets/ankurzing/sentiment-analysis-for-financial-news)
- **Source**: Kaggle
- **Contents**: Columns `Sentiment`, `News Headline`
- **Notes**: General financial news dataset. Doesn’t map to specific stocks.

### 3. [Stock Market Sentiment Dataset](https://www.kaggle.com/datasets/yash612/stockmarket-sentiment-dataset)
- **Source**: Kaggle
- **Contents**: Tweets and market-related news annotated with sentiment
- **Notes**: Social media-based dataset; useful for training or transfer learning.

### 4. [Twitter Financial News Sentiment Dataset](https://www.kaggle.com/datasets/borhanitrash/twitter-financial-news-sentiment-dataset)
- **Source**: Kaggle
- **Contents**: Finance-related tweets with sentiment labels
- **Notes**: Helps in building robust sentiment classification models.

---
