from flask import Flask,render_template,request
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/home')
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/prediction", methods=["GET","POST"])
def prediction():
    return render_template("prediction.html")

@app.route("/predict", methods=["GET","POST"])
def predict():

    # Race = request.form['Race_input']
    # Gender = request.form['Gender_input']
    Age = request.form['Age_input']
    # admission_type_id = request.form['admission_type_id_input']
    discharge_disposition_id = request.form['discharge_disposition_id_input']
    admission_source_id = request.form['admission_source_id_input']
    # time_in_hospital = request.form['time_in_hospital_input']
    # num_lab_procedures = request.form['num_lab_procedures_input']
    # num_procedures = request.form['num_procedures_input']
    num_medications = request.form['num_medications_input']
    number_outpatient = request.form['number_outpatient_input']
    number_emergency = request.form['number_emergency_input']
    number_inpatient = request.form['number_inpatient_input']
    # diag_1 = request.form['diag_1_input']
    # diag_2 = request.form['diag_2_input']
    # diag_3 = request.form['diag_3_input']
    number_diagnoses = request.form['number_diagnoses_input']
    # A1Cresult = request.form['A1Cresult_input']
    # metformin = request.form['metformin_input']
    # glipizide = request.form['glipizide_input']
    # glyburide = request.form['glyburide_input']
    # pioglitazone = request.form['pioglitazone_input']
    # rosiglitazones = request.form['rosiglitazones_input']
    # insulin = request.form['insulin_input']
    # change = request.form['change_input']
    # diabetesMed = request.form['diabetesMed_input']

    # form_array = np.array([[Race,Gender, Age, admission_type_id, 
    # discharge_disposition_id, admission_source_id, time_in_hospital, num_lab_procedures,
    # num_procedures, num_medications, number_outpatient, number_emergency, number_inpatient,
    # number_diagnoses, A1Cresult, metformin, glipizide, glyburide,
    # pioglitazone, rosiglitazones, insulin, change, diabetesMed]])

    form_array = np.array([[Age, 
    discharge_disposition_id, admission_source_id, 
     num_medications, number_outpatient, number_emergency, number_inpatient,
    number_diagnoses]])

    model = pickle.load(open(r"D:/A1. ESILV/Annee 4/S7/Python/PROJET/FLASK/GB_prediction.pkl","rb"))
    prediction = model.predict(form_array)[0]


    if prediction == 1:
        result = r"Readmited under 30 days (58,13% accuracy)"

    elif prediction == 2:
        result = r"Readmited over 30 days (58,13% accuracy)"

    elif prediction == 3:
        result = r"No readmission (58,13% accuracy)"

    return render_template("results.html",result = result)

@app.route("/database")
def database():
    return render_template("database.html")

@app.route("/results")
def results():
    return render_template("results.html")

if __name__ == "__main__":
    app.run(debug=True)