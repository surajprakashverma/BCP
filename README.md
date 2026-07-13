# 🎗️ Breast Cancer Prediction

A modern, AI-powered web application that predicts whether a breast tumor is **malignant (Cancer)** or **benign (Not Cancer)** based on 30 diagnostic features from the Wisconsin Breast Cancer dataset. Built with Flask, scikit-learn, and a beautiful glassmorphism UI.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0-black.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3-orange.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## ✨ Features

- 🤖 **ML-powered prediction** using a trained Logistic Regression model
- 🎨 **Modern glassmorphism UI** with dark gradient theme and Poppins font
- 🌸 **Gradient pink-yellow title** with Font Awesome icons
- 📊 **Color-coded result cards** — green for Not Cancer, red for Cancer
- 🔄 **Post/Redirect/Get (PRG) pattern** — prediction shows once, then resets on refresh
- 📱 **Fully responsive** design that works on all screen sizes
- 🔐 **Session-based state management** using Flask sessions

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| **Backend** | Python 3.10+, Flask 3.0 |
| **ML/Data** | scikit-learn, NumPy, Pandas |
| **Frontend** | HTML5, CSS3, Bootstrap 5.3, Jinja2 |
| **Fonts/Icons** | Google Fonts (Poppins), Font Awesome 6.4 |
| **Model** | Logistic Regression (pickled as `model.pkl`) |

---

## 📸 Screenshots

> _Add screenshots of your app here after deployment._

- Home page with input form
- Prediction result (Not Cancer)
- Prediction result (Cancer)

---

## 📁 Project Structure

```
BCP/
├── app.py                      # Flask application (routes, PRG pattern)
├── model.pkl                   # Trained ML model (Logistic Regression)
├── breast cancer.csv           # Wisconsin Breast Cancer dataset
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── templates/
│   └── index.html              # Main UI template (Jinja2)
└── static/
    ├── img.jpg                 # Hero banner image
    ├── okay_img.jpg            # Shown when result is 'Not Cancer'
    └── alert_imge.jpg          # Shown when result is 'Cancer'
```

---

## 🚀 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/surajprakashverma/BCP.git
cd BCP
```

### 2. Create a virtual environment (recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Flask app
```bash
python app.py
```

### 5. Open your browser
Visit **http://127.0.0.1:5000/**

---

## 💡 Usage

1. Open the web app in your browser.
2. Enter **30 comma-separated diagnostic feature values** in the input field.
3. Click the **Predict** button.
4. View the result — either "Not Cancer" (green card) or "Cancer" (red card).

### Example input (30 features):
```
17.99, 10.38, 122.8, 1001, 0.1184, 0.2776, 0.3001, 0.1471, 0.2419, 0.07871,
1.095, 0.9053, 8.589, 153.4, 0.006399, 0.04904, 0.05373, 0.01587, 0.03003, 0.006193,
25.38, 17.33, 184.6, 2019, 0.1622, 0.6656, 0.7119, 0.2654, 0.4601, 0.1189
```

---

## 📊 Dataset

This project uses the **Wisconsin Breast Cancer Diagnostic Dataset** from the UCI Machine Learning Repository (also available in `sklearn.datasets`).

- **Instances:** 569
- **Features:** 30 numeric features computed from digitized images of fine needle aspirates (FNA) of breast masses
- **Target:** Binary classification — Malignant (1) or Benign (0)

**Feature categories** (each computed as mean, standard error, and worst-case):
- Radius, Texture, Perimeter, Area, Smoothness
- Compactness, Concavity, Concave points, Symmetry, Fractal dimension

---

## 🧠 Model

- **Algorithm:** Logistic Regression
- **Trained on:** Wisconsin Breast Cancer dataset (80/20 train-test split)
- **Serialized as:** `model.pkl` using `pickle`
- **Input shape:** `(1, 30)` — a single sample with 30 features

---

## ⚠️ Disclaimer

> **This tool is for educational purposes only.**
> It is not a substitute for professional medical advice, diagnosis, or treatment.
> Always seek the advice of a qualified healthcare provider with any questions you may have regarding a medical condition.

---

## 👨‍💻 Author

**Suraj Prakash Verma**
- 🌐 GitHub: [@surajprakashverma](https://github.com/surajprakashverma)

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---
## 🌐 Live Demo
Try it out: **https://breast-cancer-prediction.onrender.com**

## 🌟 Show your support

If you found this project useful, give it a ⭐ on GitHub!
