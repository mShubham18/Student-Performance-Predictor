# Student Performance Indicator

### Project Overview
- This project aims to predict student performance using various machine learning algorithms. 
- The model takes into account several factors such as demographics, test scores, and parental education levels to provide accurate predictions of students' academic performance in mathematics.

### Models Used
The following regression models have been implemented in this project:

- `Decision Tree Regressor`: A tree-based model that captures non-linear relationships.
- `Random Forest Regressor`: An ensemble of decision trees that enhances prediction accuracy and reduces overfitting.
- `Gradient Boosting Regressor`: Builds trees sequentially to correct errors from previous trees.
- `Linear Regression`: Establishes a linear relationship between input features and the target variable.
- `XGBoost Regressor`: An efficient gradient boosting model known for its speed and performance.
- `CatBoost Regressor`: Specifically designed to handle categorical features effectively.
- `AdaBoost Regressor`: Focuses on improving weak learners to create a strong predictive model.

### Features
- Parent/Teacher/Student can Predict their Math score by entering their details 
- Easy to use UI
- WebAPP is trained in all the mentioned Models and selects the best model with highest Accuracy.

### Project Advantages
- Adapts to Modular Programming for better code management and revision
- Uses Logging to track the entire workflow
- Custom Exception Handling to handle the abnormal actions correctly

### Technologies Used
- Python
    - pandas
    - numpy
    - seaborn
    - matplotlib
    - scikit-learn
    - catboost
    - xgboost
    - dill
    - flask
    - flask_cors
- Jupyter Notebook
- GIT and Github
- Flask
- Azure (for Deployment)

### Installation
To set up the project, follow these steps:
```bash
git clone https://github.com/mShubham18/Student-Performance-Predictor.git
cd Student-Performance-Predictor
```
### Create and activate a virtual environment:
```bash
python -m venv venv
# for macOS/Linux
source venv/bin/activate  
# On Windows use `venv\Scripts\activate`
```
### Usage
Run the application:
```bash
python app.py # to run Flask App
```
- Open a web browser and go to `http://127.0.0.1:5000` or `http://127.0.0.1:5500` to access the application. 

- Fill in the required fields with the student data and click on the Predict button to get the predicted math score.

### Notes
- Remove the comment from `#-e`  in the `requirements.txt` file to build the packages
- While deploying to Azure cloud, make sure to use `Python 3.12` as runtime stack
- Currently Web App can be tried at : https://studentperformancepredictor.azurewebsites.net/
- NOTE: working of the link is subjected to availability

## Project Screenshots
- **Landing Page :** <br /><br />
    <img src="Resources/landing_page.png">
- **Prediction Page :** : <br /><br />
    <img src="Resources/prediction_page.png">
- **Working :** <br /><br />
    <img src="Resources/working.gif">

### Contribution
Contributions are welcome! If you have suggestions for improvements or additional features, please fork the repository and submit a pull request.

**That's it folks, Happy Learning :)**