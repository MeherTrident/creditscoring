import pickle
import pandas as pd
from flask import Flask, request, make_response
import json


loaded_model = pickle.load(open("KNN_model.sav", 'rb'))


app = Flask(__name__)
@app.route('/', methods=['POST'])
def index():
    
    #d = request.args.to_dict() # data recived from form
    d=request.get_json()
    d["fy"]=2022
    d["libor"]=7
    d["crudOilPrice"]=100
    d["inflation"]=5
    df=pd.DataFrame(data=d,index=[0])
    
   
    
    print(d)        # data recived from form
    
    
    data=make_response(json.dumps({'message': int(loaded_model.predict(df)[0])})) # transform final result to json
    resp=data
    resp.status_code = 200
    resp.headers['Access-Control-Allow-Origin'] = '*' # configiration 
    return resp


    
    
    
if __name__ == "__main__":
    app.run()
    