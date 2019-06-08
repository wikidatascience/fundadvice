# Importing the required packages 
import pandas as pd 
from sklearn.naive_bayes import GaussianNB 

data = pd.read_csv('Fund_Advice_Data.csv')
data.head()

# Flag creation
data['gender_flag'] = data.gender.map({'F':0, 'M':1})
#data['employment_status_flag'] = data.employment_status.map({'Business':0, 'Salaried':1})
data['loan_flag'] = data.loan.map({'No':0, 'Yes':1})
data['investments_flag'] = data.investments.map({'No':0, 'Yes':1})
data['risk_flag'] = data.risk.map({'High':1, 'Mid':2,'Low':3})
data['goal_flag'] = data.goal.map({'Long Term Goal':1, 'Mid Term Goal':2,'Short Term Goal':3})

data['inv_purp_flag'] = data.investment_purpose.map({'Build a nest egg for retirement':1,'Buy a vacation home':2
                                             ,'Have the funds to start a new business':3,'Income stream for retirement':4
                                             ,'Leave a financial legacy to your family':5,'Plan for wedding':6
                                             ,'Save a down payment for a home':7,'Save for you childrens education':8
                                             ,'Take a vacation':9})

data['target_flag'] = data.target.map({'Arbitrage funds':1,'Debt-oriented funds':2,
                                       'Dividend yield funds':3,'ELSS':4,'Equity diversified funds':5,
                                       'Equity-oriented funds':6,'Floating rate funds/ short-term income funds':7,
                                       'FMPs':8,'Gilt funds ST':9, 'Gilt funds LT':10,
                                       'Income funds LT':11,'Index funds':12,
                                       'Liquid funds':13,'MIPs':14,
                                       'Sector funds':15,'Thematic funds':16})

# Seperating the target variable 
X = data[['income','inv_purp_flag','contribute','goal_flag','risk_flag']] 
y = data[['target_flag']] 

# training a Naive Bayes classifier 
gnb = GaussianNB().fit(X, y) 

###############################################################################
# Test data creation
def pred_func(data):
        data = pd.DataFrame(data)
        #data['gender_flag'] = data.gender.map({'F':0, 'M':1})
        #data['employment_status_flag'] = data.employment_status.map({'Business':0, 'Salaried':1})
        data['loan_flag'] = data.loan.map({'No':0, 'Yes':1})
        data['investments_flag'] = data.investments.map({'No':0, 'Yes':1})
        data['risk_flag'] = data.risk.map({'High':1, 'Mid':2,'Low':3})
        data['goal_flag'] = data.goal.map({'Long Term Goal':1, 'Mid Term Goal':2,'Short Term Goal':3})
        
        data['inv_purp_flag'] = data.investment_purpose.map({'Build a nest egg for retirement':1,'Buy a vacation home':2
                                                     ,'Have the funds to start a new business':3,'Income stream for retirement':4
                                                     ,'Leave a financial legacy to your family':5,'Plan for wedding':6
                                                         ,'Save a down payment for a home':7,'Save for you childrens education':8
                                                     ,'Take a vacation':9})
        
        model_data = data[['income','inv_purp_flag','contribute','goal_flag','risk_flag']]
        gnb_predictions = gnb.predict(model_data)
        return(gnb_predictions)
        
