# Enhanced India-Centric Stock Sentiment Analysis

This repository implements a complete pipeline for **India-centric stock sentiment analysis** using both classical machine learning (**TF-IDF + Logistic Regression**) and modern **LLM fine-tuning** (**BERT-based models**). The focus is on capturing uniquely Indian market behavior, where sentiment is often influenced by **news, politics, and cultural narratives**.

---

## Table of Contents

1. Project Structure  
2. Data Preprocessing  
3. Baseline Models  
4. LLM Fine-Tuning Methodology  
5. Evaluation and Results  
6. Summary  

---

## Project Structure

- `processed_splits/` – Contains cleaned, balanced, and stratified train/test CSV splits for **India**, **External**, and **Mixed** datasets.  
- `bert_finetuned/` – Directory where fine-tuned BERT models and tokenizers are saved.  
- `model_comparison.csv` – Final comparison of baseline and fine-tuned LLM results.  

---

## Data Preprocessing

### 1. Loading & Cleaning
- **Cleaning steps**:
  - Remove URLs, HTML tags, and newline/tab characters
  - Strip extra whitespace
  - Handle non-string inputs (NaN, lists, tuples)
- **Function**: `clean_text()`
- **Input**: Raw headline or social media post
- **Output**: Cleaned string

### 2. Loading Datasets
- India-specific dataset: `final_news_sentiment_analysis.csv`  
- External datasets: DJIA, NASDAQ, Financial Phrasebank, Stock Market sentiment, Twitter train/valid sets  
- Mixed dataset: Concatenation of India + External datasets  
- **Helper function**: `load_csv(path)`

### 3. Balancing
- Ensures equal representation of each sentiment label (**Positive**, **Neutral**, **Negative**)  
- **Function**: `balance_dataset(df)`

### 4. Train/Test Split
- Stratified **80/20 split** to preserve sentiment distribution  
- **Function**: `stratified_split(df)`

**Saved splits**:
```
processed_splits/
├── india_train.csv
├── india_test.csv
├── external_train.csv
├── external_test.csv
├── mixed_train.csv
├── mixed_test.csv
```

---

## Baseline Models (TF-IDF + Logistic Regression)

1. **Vectorization**: TF-IDF with `max_features=5000` and `ngram_range=(1,2)`  
2. **Classifier**: Logistic Regression with class weighting to handle imbalance  
3. **Evaluation**:
   - Accuracy
   - Precision / Recall / F1 (weighted)
   - Confusion matrix

**Reusable Functions**:
- `train_and_eval(train_path, test_df, model_name)` – trains and evaluates model  
- `evaluate_baseline(model, X_test, y_test, model_name)` – prints metrics and confusion matrix

**Baselines Run**:
- India-only on India test set  
- External-only on India test set  
- Mixed on India test set  
- External-only on External test set  
- Mixed on Mixed test set  

---

## LLM Fine-Tuning Methodology

We fine-tune **BERT-based sequence classification models** on **India**, **External**, and **Mixed** datasets.

### 1. Setup
- Downgrade PyArrow to avoid cuDF conflicts  
- Install necessary libraries:  
  ```
  torch, transformers, accelerate, datasets, trl, peft, bitsandbytes
  ```

### 2. Preprocessing
- Normalize text and labels (`Negative=0, Neutral=1, Positive=2`)  
- Tokenization with `AutoTokenizer` (`bert-base-uncased`)  
- Max sequence length: **128**

**Functions**:
- `clean_headlines(df)` – handles missing values and converts tokens/lists to string  
- `tokenize(batch)` – tokenizes text for the model  
- `compute_metrics(eval_pred)` – computes weighted accuracy and F1  

### 3. Training
- **Trainer** from HuggingFace Transformers  
- **Training arguments**:
  - Epochs: **16**
  - Batch size: **16**
  - Gradient accumulation: **3**
  - Learning rate: **5e-5**
  - FP16 enabled
  - Logging to TensorBoard

- Dataset split: Train on specific split (**India / External / Mixed**)  
- Evaluation on split test set and gold India test set  

### 4. Prediction & Evaluation
- Prediction using `model.eval()`  
- Metrics reported:
  - Accuracy
  - Weighted F1
  - Classification report
  - Confusion matrix (plotted with Seaborn)

**Function**: `predict(test_df, model, tokenizer, device)`

---

## Evaluation & Results

- Baseline TF-IDF + Logistic Regression results recorded in a comparison table  
- Fine-tuned BERT models evaluated on **split test** and **gold India test**  
- Results saved to:
```
bert_finetuned/model_comparison.csv
```
- Confusion matrices plotted for visual inspection of label prediction quality  

---

## Summary

This project implements a **full workflow** from raw headline scraping to advanced model fine-tuning:

1. Load → Clean → Balance → Split  
2. Classical baseline model training (**TF-IDF + Logistic Regression**)  
3. Modern LLM fine-tuning (**BERT-based**)  
4. Evaluation across multiple datasets and gold test set  

The pipeline ensures **India-centric sentiment detection** that accounts for unique market cues and investor behavior.

---
