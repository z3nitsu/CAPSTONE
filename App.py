#import libraries
import numpy as np
from flask import Flask, render_template,request,send_from_directory
import pickle#Initialize the flask App

def predictValue(model, dic):
    dic.popitem()
    new_dic = dic
    predict_list = list(map(float, list(new_dic.values())))
    values = np.asarray(predict_list) 
    prediction = model.predict(values.reshape(1, -1))[0]
    return prediction
def predictModel(dic):
    if list(dic.values())[-1] == 'heart':
        print("Heart")
        model = pickle.load(open('Models/heart.pkl','rb'))
        return predictValue(model, dic)
    elif list(dic.values())[-1] == 'diabetes':
        print("kindey")
        model = pickle.load(open('Models/diabetes.pkl','rb'))
        return predictValue(model, dic)
    else:
        return
    
    
app = Flask(__name__)

@app.route("/static/<path:path>")
def static_dir(path):
    return send_from_directory("static", path) 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/details')
def deatils():
    return render_template('details.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/heart',methods=['POST', 'GET'])
def heart():
    return render_template('heart.html')

@app.route('/diabetes',methods=['POST', 'GET'])
def diabetes():
    return render_template('diabetes.html')

@app.route('/predict',methods=['POST', 'GET'])
def predict():
            to_predict_dict = request.form.to_dict()
            pred = predictModel(to_predict_dict)
            return render_template('predict.html', prediction_text='Predict :{}'.format(pred))
if __name__ == '__main__':
	app.run(debug = True)
 