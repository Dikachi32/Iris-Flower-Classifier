# 🌸 Iris Flower Classifier

> *A full-stack machine learning web application that identifies Iris flower species with elegance and precision — built with love, curated for the lovers of flowers.*

## 🌺 Overview

The **Iris Flower Classifier** is a beautiful, production-ready web application powered by a trained Decision Tree machine learning model. It classifies Iris flowers into one of three species based on four botanical measurements — instantly, accurately, and elegantly.

Users simply enter the **Sepal Length**, **Sepal Width**, **Petal Length**, and **Petal Width** of an Iris flower in centimetres, click **Predict Species**, and the app returns:

- 🌸 The **species name** (Iris setosa, Iris versicolor, or Iris virginica)
- 🖼️ A **real photograph** of the identified species
- 📖 A **botanical description** of the flower
- 🌍 The flower's **native geographic origin**
- 🔗 Learn more link: More information about the species
This project demonstrates that machine learning doesn't have to be cold and technical — it can be beautiful too.

---

## ✨ Features

- 🤖 **100% Accuracy** — Decision Tree model trained on the classic Fisher Iris Dataset
- 🌸 **Botanical UI Design** — Elegant orchid purple and petal pink color palette
- 🔤 **Premium Typography** — Cormorant Garamond (serif) + DM Sans (sans-serif)
- 📱 **Fully Responsive** — Works seamlessly on desktop, tablet, and mobile
- ⚡ **Instant Predictions** — Real-time classification with zero delay
- 🛡️ **Input Validation** — Clean error handling for invalid or missing inputs
- 🖼️ **Species Images** — Each result displays a real photo of the identified flower
- 🌍 **Species Origin** — Learn where each Iris species is native to

---

  ## Watch the demo video

(https://www.linkedin.com/posts/dikachi-baron-a4a380356_machinelearning-python-flask-ugcPost-7457458696797872128-vw11?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFiwEdoBhQHM9RGHGnevgOcCk1gtXoCOlv8)

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Python 3.11, Flask |
| **Machine Learning** | Scikit-learn — Decision Tree Classifier |
| **Model Serialization** | Joblib |
| **Frontend** | HTML5, CSS3 |
| **Typography** | Cormorant Garamond + DM Sans (Google Fonts) |
| **Dataset** | Fisher's Iris Dataset (UCI Repository, 1936) |

---

## 📁 Project Structure

```
iris-flower-classifier/
│
├── static/
│   ├── styles.css                  # Full botanical stylesheet
│   ├
│   └── species_images/
│       ├── iris-setosa.jpg
│       ├── iris-versicolor.jpg
│       └── iris-virginica.jpg
│
├── templates/
│   ├── base.html                   # Base layout (navbar + footer)
│   ├── decision_tree.html                  # Prediction form page
│   └── result.html                 # Results & species details page
│
├── app.py                          # Flask application entry point
├── decision_tree.ipynb             # Model training script
├── decision_tree_model.pkl         # Trained ML model (binary)
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git ignore rules
└── README.md                       # This file
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11
- pip

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/Dikachi32/iris-flower-classifier.git
cd iris-flower-classifier
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Train the model**
```bash
python train_model.py
```

**5. Run the app**
```bash
python app.py
```

**6. Open in your browser**
```
http://127.0.0.1:5000
```

---

## 🌷 How to Use

1. Open the app at `http://127.0.0.1:5000`
2. Enter the **Sepal Length** in centimetres
3. Enter the **Sepal Width** in centimetres
4. Enter the **Petal Length** in centimetres
5. Enter the **Petal Width** in centimetres
6. Click **🌺 Predict Species**
7. View your result — species name, image, description, and origin

---

## 🌍 The Three Iris Species

| | Species | Characteristics | Native Origin |
|-|---------|----------------|---------------|
| 🌱 | *Iris setosa* | Smallest of the three — compact blue-purple flowers, narrow sepals, prominent yellow beard | North America |
| 🌸 | *Iris versicolor* | Medium-sized — blue-violet flowers, showy white signal patches on drooping sepals, upright sword-shaped leaves | Eastern North America |
| 🌺 | *Iris virginica* | Largest and most showy — deep violet-purple flowers, broad arching leaves, prominent orange-yellow beards | Eastern United States |

---

## 📊 Model Details

| Property | Value |
|----------|-------|
| **Algorithm** | Decision Tree Classifier |
| **Dataset** | Fisher's Iris Dataset |
| **Training Samples** | 150 (50 per species) |
| **Features** | 4 (sepal length, sepal width, petal length, petal width) |
| **Classes** | 3 (setosa, versicolor, virginica) |
| **Accuracy** | **100%** |

---

## 📦 Dependencies

```
flask
scikit-learn
joblib
```

Generate your full requirements file with:
```bash
pip freeze > requirements.txt
```

---

## 👤 Author

**Dikachi Sunday**

| Platform | Link |
|----------|------|
| 🐙 GitHub | [@Dikachi32](https://github.com/Dikachi32) |
| 💼 LinkedIn | [Dikachi Sunday](https://www.linkedin.com/in/dikachi-sunday-a4a380356) |
| 🐦 Twitter | [@Baron_dikachi](https://x.com/Baron_dikachi) |
| 📘 Facebook | [Dikachi Sunday](https://www.facebook.com/share/18H6wLY1fW/) |

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and share.
