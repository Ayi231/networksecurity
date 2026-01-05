### Network security Projects for Phishing Data
Train/evaluate phishing classifiers, track experiments with MLflow, and serve predictions via FastAPI (Dockerized).

Features:

-Schema validation on input CSV (rejects malformed rows)

-Feature engineering for URL/text fields

-Train + compare multiple models (LogReg/SVM/RF/etc.)

-Metrics logged to MLflow (F1/precision/recall + artifacts)

-FastAPI inference endpoint

-Docker + reproducible run commands

-Optional CI (GitHub Actions) for lint/tests/build

Quick Start commands:

python -m venv .venv

source .venv/bin/activate  # windows: .venv\Scripts\activate

pip install -r requirements.txt


python src/train.py --data data/phishing.csv

mlflow ui

uvicorn app.main:app --reload



Example of results
<img width="1354" height="150" alt="image" src="https://github.com/user-attachments/assets/f1ac703b-b418-4806-a0e1-5d991c2ffc1e" />
