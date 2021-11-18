from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/predict')
def predict():
    import requests
    
    url = "https://6l6l7n7vtb.execute-api.us-east-2.amazonaws.com/test/predict"

    payload="{\"data\":\"0,-0.34147611300851444,0.18202662446267728,310000.0,2.0,2.0,1.0,44.0,-1.0,-1.0,-2.0,-2.0,-2.0,-2.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0\"}"
    headers = {'Content-Type': 'application/json'}

    response = requests.request("POST", url, headers=headers, data=payload)
    name = str(response.text)
    #return render_template("predict.html",name=name)
    return name


@app.route('/form-predict', methods=['GET', 'POST'])
def form_predict():
    #Handle the post request and process the request
    if request.method == 'POST':
        education = request.form.get('education')
        age = request.form.get('age')
        chunk1 = "{\"data\":\"0,-0.34147611300851444,0.18202662446267728,310000.0,2.0,"
        chunk_edu = education
        chunk_sex = ",1.0,"
        chunk_age = age
        chunk2 = ",-1.0,-1.0,-2.0,-2.0,-2.0,-2.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0\"}"
        #payload="{\"data\":\"0,-0.34147611300851444,0.18202662446267728,310000.0,2.0,2.0,1.0,44.0,-1.0,-1.0,-2.0,-2.0,-2.0,-2.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0\"}"
        new_load = chunk1 + chunk_edu + chunk_sex + chunk_age + chunk2
        import requests
    
        url = "https://6l6l7n7vtb.execute-api.us-east-2.amazonaws.com/test/predict"

        #payload="{\"data\":\"0,-0.34147611300851444,0.18202662446267728,310000.0,2.0,2.0,1.0,44.0,-1.0,-1.0,-2.0,-2.0,-2.0,-2.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0\"}"
        headers = {'Content-Type': 'application/json'}

        response = requests.request("POST", url, headers=headers, data=new_load)
        name = str(response.text)
        #return render_template("predict.html",name=name)


        return '''
            <h1>The education is: {}</h1>
            <h1>The age is : {}</h1>
            <h1>Percent default : {}</h1>'''.format(education, age, name)
#'Label,PAY_AMT1,BILL_AMT1,LIMIT_BAL,SEX,EDUCATION,MARRIAGE,AGE,PAY_0,PAY_2,PAY_3,PAY_4,PAY_5,PAY_6,BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6'
    #Handle the GET request and create the input form
    return '''<form method="POST">
                <h2>Please select </h2>
                <div><label>Level of Education: <input type="text" name="education"></label></div>
                <div><label>Age: <input type="text" name="age"></label></div>
                <input type="submit" value="Submit">
            </form>'''



if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port='8080')

