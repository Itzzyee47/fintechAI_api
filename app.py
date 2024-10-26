import json
from flask import Flask,render_template,redirect,request
from flask_cors import CORS
from model import getResponds, getFinancialAdvice



app = Flask(__name__)

app.secret_key = 'wqopi313b'

cors = CORS(app)


@app.route("/")
def index(request):
    
    return render_template('pages/index.html')


@app.route("/getFinancialAdvice",methods=['POST'])
def get_financial_advice():
    raw_data = request.data
    data = json.loads(raw_data)
    try:
        bot_reply = getFinancialAdvice()
        
        return bot_reply
    except Exception as error:
        return error     
    
    
if __name__ == "__main__":
    app.run(host='localhost',debug=True, port=4080)