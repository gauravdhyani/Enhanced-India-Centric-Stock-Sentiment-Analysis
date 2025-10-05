# Basic Web Page Pipeline for India-Centric Stock Sentiment Analysis

This documentation explains the three key components of the web-based sentiment analysis pipeline for Indian stock market news. The system extracts news, predicts sentiment using a fine-tuned model, and serves results on a web page.

 <figure>
  <img width="1896" height="948" alt="Screenshot 2025-10-05 030539" src="https://github.com/user-attachments/assets/be5c217f-df1f-4135-a35b-bd0a5dea0208" /><br>
  <figcaption><b> Delhi Shapefile (Region of Interest) </b></figcaption>
</figure>

---

## 1. UpStoxNewsExtractor

### **What it is**
A Python script using **Selenium** to scrape stock-related news headlines from the UpStox website (or similar sources).  

### **Why it’s done**
- Stock sentiment analysis requires fresh and relevant news data.  
- Automated scraping allows continuous collection without manual intervention.  
- Headlines are the primary textual input for sentiment prediction.  

### **How it works**
1. **Chrome WebDriver Setup**:
   - Uses `webdriver_manager` to automatically manage the ChromeDriver.
   - Configured with user-agent to mimic a real browser and bypass restrictions.
2. **Open Website**:
   - URL is opened in a headless Chrome instance.
   - Waits until at least one `<h2>` tag is loaded (usually news headline container).
3. **Extract Headlines**:
   - Finds all `<h2>` tags.
   - Filters out empty or whitespace-only entries.
4. **Save to CSV**:
   - Headlines are stored in `headlines.csv` using Pandas for further processing.

---

## 2. SentimentAnalysisGenerator

### **What it is**
A Python script that **loads a fine-tuned BERT-based model** and predicts sentiment for each news headline, saving the results in **JSON format**.

### **Why it’s done**
- Headlines alone are not useful without sentiment classification.  
- JSON format provides **structured data** for web display and API access.  
- Enables **downstream analytics or visualization**.

### **How it works**

#### 1. Load Model & Tokenizer
- Loads the fine-tuned model and tokenizer from directories (`final_model` and `final_tokenizer`).  
- Runs the model on **GPU (if available)** for faster predictions.

#### 2. Prepare Input Data
- Reads `headlines.csv`.  
- Ensures the `Headline` column is **clean and string-typed**.

#### 3. Tokenization & Model Prediction
- Converts text to **token IDs** with padding and truncation.  
- Performs a **forward pass** through the model without gradient computation.  
- Applies **softmax** to get probabilities.  
- Determines predicted label: `Negative`, `Neutral`, or `Positive` and the confidence score.

#### 4. Save Predictions
- Stores results in `output.json` as an array of objects, for example:

---

## 3. MainWebPage

### **What it is**
A **Flask web application** that displays predicted sentiment for news headlines and exposes an **API endpoint** for JSON access.

### **Why it’s done**
- Provides a **user-friendly interface** for investors, analysts, or developers.  
- Enables **real-time visualization** and programmatic access via API.  
- Integrates the **scraping and sentiment pipeline** into a full-stack workflow.

### **How it works**

#### 1. Flask App Setup
- Flask handles **routing** and serving HTML templates.  
- Two routes:
  - `/` → Renders the web page with sentiment results.  
  - `/api/data` → Returns JSON data for programmatic access.

#### 2. Load Predictions
- Reads `output.json` produced by **SentimentAnalysisGenerator**.

#### 3. Render HTML Page
- Passes the list of headlines with **sentiment and score** to `index.html`.  
- Dynamic rendering via **Jinja2 templates**.

#### 4. API Endpoint
- Returns JSON payload directly, enabling integration with other tools or dashboards.

#### 5. Run Server
- `app.run(debug=True)` launches a **development server** accessible locally.

---
