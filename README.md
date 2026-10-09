# 💳 Credit Card Fraud Detection

A machine learning web app that predicts whether a credit card transaction is fraudulent, using a Random Forest classifier.

## What's in this repo

| Folder / file | What it is |
|---|---|
| `app.py`, `templates/`, `static/` | The Flask web app that serves the model and makes predictions |
| `rfc_model.pkl` | The trained Random Forest model |
| `Procfile`, `netlify.toml`, `requirements.txt` | Deployment and dependency settings |
| `github-pages-site/` | A static website version of the app (originally its own repo, `ccfraud`, merged here with its history) |

## How it works

The model was trained on anonymised credit card transaction features (V1 to V28, plus Time and Amount). An earlier experiment using only Time and Amount was less effective, so the app uses the full feature set.

## Run it locally

```bash
pip install -r requirements.txt
python app.py
```

Then open http://localhost:5000 in your browser.

## History

This repo combines two earlier repos into one timeline. Commits from both are kept, so the history shows the project going from first upload (December 2023) to the deployed web app.
