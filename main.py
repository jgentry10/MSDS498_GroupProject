from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def predict():
    import requests
    
    url = "https://6l6l7n7vtb.execute-api.us-east-2.amazonaws.com/test/predict"

    payload="{\"data\":\"0,-0.34147611300851444,0.18202662446267728,310000.0,2.0,2.0,1.0,44.0,-1.0,-1.0,-2.0,-2.0,-2.0,-2.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0\"}"
    headers = {'Content-Type': 'application/json'}

    response = requests.request("POST", url, headers=headers, data=payload)
    name = str(response.text)
    return render_template("form.html",name=name)

@app.route('/', methods =["GET", "POST"])
def predict():
    if request.method == "POST":
        payload = request.form.get("payload")
        url = "https://6l6l7n7vtb.execute-api.us-east-2.amazonaws.com/test/predict"
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=payload)
        pvalue = str(response.text)
        return render_template("form.html", pvalue= pvalue)
    return render_template("form.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port='8080')
