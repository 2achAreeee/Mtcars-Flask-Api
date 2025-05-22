# Mtcars Flask API 

This project builds a linear regression model to predict `mpg` from the `mtcars.csv` dataset, serves it via a Flask API, containerizes it with Docker, and deploys it to Google Cloud Run.

---

##  Local Usage (via Docker)

### Build & Run Locally

```bash
docker build -t mtcars-api .
docker run -p 5001:5001 mtcars-api
```

Then test:

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"cyl":6, "disp":160, "hp":110, "drat":3.9, "wt":2.62, "qsec":16.46, "vs":0, "am":1, "gear":4, "carb":4}' \
  http://localhost:5001/predict
```

---

##  Deployed Cloud API

**URL:**  
[https://mtcars-api-349535554801.us-central1.run.app](https://mtcars-api-349535554801.us-central1.run.app)

### Test via curl

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"cyl":6, "disp":160, "hp":110, "drat":3.9, "wt":2.62, "qsec":16.46, "vs":0, "am":1, "gear":4, "carb":4}' \
  https://mtcars-api-349535554801.us-central1.run.app/predict
```

Expected response:

```json
{"predicted_mpg": <float>}
```

---

## Project Structure

```
Mtcars-Flask-Api/
├── app/
│   ├── mtcars.csv
│   ├── predict.py
│   └── requirements.txt
├── Dockerfile
├── .dockerignore
├── README.md
└── zachary_huang_hw3.md
```
