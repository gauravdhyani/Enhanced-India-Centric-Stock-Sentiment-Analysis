# Enhanced-India-Centric-Stock-Sentiment-Analysis

---

## Project Aim
The aim of this project is to develop an **India-focused stock sentiment analysis system** that can classify financial news and social media headlines related to **NIFTY 50 companies** into **Positive**, **Negative**, or **Neutral** sentiment.

Most publicly available datasets that are centered on the US market, this project introduces a custom dataset [**NifSent50**](https://www.kaggle.com/datasets/grounddominator/nifsent50-nifty-50-stocks-and-news-dataset) tailored for the Indian stock market, while also leveraging global datasets to test cross-market generalization.

---

## Why India-Centric?
Unlike Western markets, the **Indian stock market is driven more by sentiment than by pure numbers**. News, politics, and cultural narratives heavily influence investor behavior. 

- **Optimism, fear, and risk-taking** shaped by uniquely Indian cues often defy models trained on foreign markets.
- This makes the Indian market **a class of its own**, where global sentiment models fail to capture local nuances.

Hence, **building and fine-tuning a model specifically on Indian market behavior becomes crucial** for:
- Accurate sentiment prediction
- Better decision-making for investors and analysts

---

## Objectives
- Build and publish **NifSent50**, the first large-scale India-centric sentiment dataset linking news to NIFTY 50 stock price changes.
- Benchmark **India-only**, **External-only**, and **Mixed (India + Global)** training strategies.
- Fine-tune **Large Language Models (LLMs)** like **BERT** for financial sentiment classification.
- Evaluate models on both domain-specific (India) and general/global datasets.

---

## Methodology

### **Dataset Creation**
- Collected news & social media headlines from:
  - **NewsAPI**, **Investing.com**, and **Reddit**
- Used **Yahoo Finance** for price movement labels.
- Defined sentiment labels based on **±1% stock movement** after news publication.
- Integrated multiple external/global sentiment datasets (financial news & Twitter).

### **Model Training**
- Used **BERT (bert-base-uncased)** as the base model.
- Fine-tuned separately on:
  - India-only data
  - External-only data
  - Mixed data
- Implemented training with **HuggingFace Trainer**, **PyTorch**, and evaluation pipeline.

### **Evaluation**
- Metrics: **Accuracy**, **Precision**, **Recall**, **F1 Score**, **Confusion Matrices**.
- Tested both within-dataset performance and cross-domain generalization.

---

## Why This Project?
- **Gap in resources** → Most financial sentiment research is US-centric.
- **Practical relevance** → Indian investors and analysts need localized sentiment tools.
- **Cross-market testing** → To study whether global datasets help improve Indian predictions or cause domain mismatch.

---

## Results

### Baseline Models (before fine-tuning)
- India-only performed best on Indian test data (~37% accuracy).
- External-only struggled on Indian data (~33%).
- Mixed slightly improved (~40%).
- External performed best on external data (~65%).

| Model                       | Accuracy | Precision | Recall | F1    |
| --------------------------- | -------- | --------- | ------ | ----- |
| India-only (on India)       | 0.375    | 0.374     | 0.375  | 0.374 |
| External-only (on India)    | 0.333    | 0.335     | 0.333  | 0.332 |
| Mixed (on India)            | 0.398    | 0.425     | 0.398  | 0.365 |
| External-only (on External) | 0.649    | 0.648     | 0.649  | 0.648 |
| Mixed (on Mixed)            | 0.615    | 0.614     | 0.615  | 0.613 |

---

### Fine-Tuned LLM (BERT)
- India dataset: Slight improvement (40%).
- External dataset: Very strong within-domain performance (74%), but poor transfer to India (~32%).
- Mixed dataset: Strong generalization, best performance on India test set (~70%).

| Model    | Split Accuracy | Split F1 | Gold Accuracy (India) | Gold F1   |
| -------- | -------------- | -------- | --------------------- | --------- |
| India    | 0.398          | 0.396    | 0.398                 | 0.396     |
| External | 0.736          | 0.736    | 0.320                 | 0.321     |
| Mixed    | 0.680          | 0.679    | **0.702**             | **0.705** |

---

## Key Insights
- Training only on Indian data gives modest accuracy but ensures domain alignment.
- Training only on global data works well for global markets but fails to transfer to Indian news.
- Mixed dataset training provides the best balance — achieving ~70% accuracy on Indian test data after fine-tuning.
