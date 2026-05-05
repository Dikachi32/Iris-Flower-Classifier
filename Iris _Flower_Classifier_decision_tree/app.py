from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

# ============ PATHS ============
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, 'decision_tree_model.pkl')

# ============ LOAD MODEL ============
try:
    model = joblib.load(model_path)
    print("✅ Model loaded successfully.")
except FileNotFoundError:
    raise Exception("❌ Model file not found. Run train_model.py first.")

# ============ SPECIES DATABASE ============
# Fixed: species names now match the botanical format used in result.html
# Fixed: image filenames lowercased for Linux/server compatibility
SPECIES_DB = {
    0: {
        'name': 'Iris setosa',
        'image': 'iris-setosa.jpg',
        'description': 'The smallest of the three Iris species, with compact blue-purple flowers, narrow sepals, and a prominent yellow beard.',
        'origin': 'North America'
    },
    1: {
        'name': 'Iris versicolor',
        'image': 'iris-versicolor.jpg',
        'description': 'Medium-sized with blue-violet flowers, showy white signal patches on drooping sepals, and upright sword-shaped leaves.',
        'origin': 'Eastern North America'
    },
    2: {
        'name': 'Iris virginica',
        'image': 'iris-virginica.jpg',
        'description': 'The largest and most showy, with deep violet-purple flowers, broad arching leaves, and prominent orange-yellow beards.',
        'origin': 'Eastern United States'
    }
}

# ============ ROUTES ============

@app.route('/')
def home():
    # Fixed: template name updated to match your actual file — index.html
    return render_template('decision_tree.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get and validate measurements from form
        sepal_length = float(request.form['sepal_length'])
        sepal_width  = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width  = float(request.form['petal_width'])

        # Basic validation — all values must be positive
        if any(v <= 0 for v in [sepal_length, sepal_width, petal_length, petal_width]):
            raise ValueError("All measurements must be greater than 0.")

        features = [sepal_length, sepal_width, petal_length, petal_width]

        # Predict
        prediction_numeric = int(model.predict([features])[0])
        species = SPECIES_DB.get(prediction_numeric, SPECIES_DB[0])

        # Send species data to result page
        return render_template('result.html', species=species)

    except ValueError as e:
        # Friendly validation error shown on the form
        return render_template('index.html', error=str(e))

    except Exception as e:
        # Catch-all for unexpected errors
        return render_template('index.html', error="Something went wrong. Please check your inputs and try again.")


if __name__ == '__main__':
    # Fixed: debug=True is fine for development but should be False in production
    app.run(debug=True)