# SmartHome-ML  
**Analysis and Classification of Security Vulnerabilities in Smart Home IoT Devices**

## Project overview
This project focuses on the analysis and classification of security vulnerabilities affecting Smart Home IoT devices.
Using textual descriptions from public vulnerability databases, we apply machine learning and natural language processing techniques to automatically predict the severity of security incidents.

The objective is to support security risk assessment and prioritization in Smart Home and Industry 4.0 environments.

---

## Dataset
The dataset is based on vulnerability data from the **National Vulnerability Database (NVD)**.
We extracted and filtered vulnerabilities related to Smart Home IoT devices and processed multiple CVSS schema versions.

Main features:
- CVE identifier
- English vulnerability description
- Severity level (LOW, MEDIUM, HIGH, CRITICAL)
- CVSS v2 and v3 scores
- Publication and last modification dates

Dataset source:  
https://nvd.nist.gov/

---

## Methodology
The project follows a complete machine learning pipeline:

1. **Data preprocessing**
   - JSON parsing and normalization
   - Extraction of English descriptions
   - Severity label construction using CVSS scores
   - Handling missing and inconsistent values

2. **Exploratory Data Analysis (EDA)**
   - Class distribution analysis
   - Text length statistics
   - Identification of class imbalance

3. **Modeling**
   - TF-IDF vectorization
   - Baseline Decision Tree classifier
   - Hyperparameter optimization using GridSearchCV

4. **Advanced models**
   - Support Vector Machine (SVM)
   - Ensemble methods: Voting and Bagging

5. **Evaluation**
   - Accuracy
   - Macro F1-score
   - Confusion matrices
   - Class-wise performance analysis

---

## Results
The experiments show that:
- Hyperparameter tuning improves performance over the baseline model
- SVM and ensemble methods outperform a single Decision Tree
- Macro F1-score is more appropriate than accuracy due to class imbalance
- Ensemble methods improve robustness, especially for minority severity classes

---

## Industry relevance
This work is relevant for **Industry 4.0 and Smart Home security**:
- Automated vulnerability severity prediction
- Security risk prioritization
- Support for predictive maintenance and security monitoring
- Scalability to large IoT infrastructures

---

## Limitations and future work
- Severity labels are sometimes inferred rather than explicitly provided
- The dataset may contain noisy or incomplete information
- Future improvements could include:
  - Deep learning models (e.g. Transformers)
  - Real-time vulnerability monitoring
  - Integration into Smart Home security dashboards

---

## Repository structure
```
├── LAB5_Project_ANDRIANTSIZAFY.ipynb # Final notebook 
├── filterData.py # Dataset filtering utilities  
├── importData.py # Dataset import utilities 
├── README.md
``` 

---

## Authors
Le Beuz Pierre
Andriantsizafy Vonjy
Goder Joshua


