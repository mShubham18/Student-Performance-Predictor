from flask import Flask, request, render_template, jsonify
from flask_cors import CORS, cross_origin  # Import CORS
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
import logging  # Import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

application = Flask(__name__)
CORS(application)  # Enable CORS

app = application

# Route for the homepage
@app.route("/")
@cross_origin()
def index():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])  # Change to /predict
@cross_origin()
def predict_datapoint():
    if request.method == "GET":
        return render_template("home.html")
    else:
        try:
            data = CustomData(
                gender=request.form.get("gender"),
                race_ethnicity=request.form.get("ethnicity"),
                parental_level_of_education=request.form.get("parental_level_of_education"),
                lunch=request.form.get("lunch"),
                test_preparation_course=request.form.get("test_preparation_course"),
                reading_score=float(request.form.get("reading_score")),
                writing_score=float(request.form.get("writing_score"))
            )
            pred_df = data.get_data_as_frame()
            print(pred_df)
            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)
            return render_template("home.html", results=results[0])  # Ensure home.html exists
        except Exception as e:
            logging.error(f"Error during prediction: {e}")
            return render_template("home.html", error="Prediction failed.")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
