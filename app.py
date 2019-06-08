from flask import Flask,request,Response
from flask_cors import CORS
import pandas as pd
from fund_adviser import pred_func

#from flask_restful import Api

#from resources.todo import Todo

app = Flask(__name__)

cors = CORS(app)
userinfo={
       
"fname": "",
"lname": "",
"age": "",
"email":"",
"income": "",
"loan": "",
"credit": "",
"percentage": "",
"investment": "",
"risk": "",
"purpose":""
         }

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
       
#       check_data = {'Gender':['F'],'Age':[32],'Residential_Status':['Tennent'],'Employment_Status':['Salaried'],'Salary':[33000],'Liabilities_Loan':['Not Available'],'Liabilities_Other':['Credit Card'],
#             'Invest_Per_Month':[10000],'Tenure':[10],'Investment_Purpose':['Plan for wedding'],'Risk_Factor':['Low']} 
#       print(type(check_data))
#       check_data = pd.DataFrame(check_data)
       
       
       
       
       
       print(request.get_json(True,False,True))
       jsonData = request.get_json(True,False,True)
      # data=request.get_json()
       input_table=pd.DataFrame([jsonData],columns=jsonData.keys())
      
       result=pred_func(input_table)
       resp = Response(str(result))
       resp.headers['Access-Control-Allow-Origin'] = '*'
       resp.headers['Access-Control-Allow-Headers']='*'
       print(jsonData)
       
      #user = request.form
    #  return str(user)
   return resp


if __name__ == "__main__":
  app.run()