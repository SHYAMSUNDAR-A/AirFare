from flask import Flask, render_template, request
import pickle
import datetime
import pandas as pd
import numpy as np

app = Flask(__name__)
model = pickle.load(open("FlightFare-RandomForest.pkl","rb"))

@app.route("/")
def home():
    return render_template("index2.html")

@app.route("/check", methods = ["POST"])
def check():
    
    if request.method == "POST":
        
        # Date of Departure
        dep_date = request.form["Departure_Time"]
        Journey_date = int(pd.to_datetime(dep_date, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(dep_date, format="%Y-%m-%dT%H:%M").month)
        
        # Departure Timing
        Dep_hr = int(pd.to_datetime(dep_date,format="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(dep_date, format="%Y-%m-%dT%H:%M").minute)
        
        # Date of Arrival
        arr_date = request.form["Arrival_Time"]
        Arrival_date = int(pd.to_datetime(arr_date, format="%Y-%m-%dT%H:%M").day)
        Arrival_month = int(pd.to_datetime(arr_date, format="%Y-%m-%dT%H:%M").month)           
    
        # Arrival Timing
        Arr_hr = int(pd.to_datetime(arr_date,format="%Y-%m-%dT%H:%M").hour)
        Arr_min = int(pd.to_datetime(arr_date, format="%Y-%m-%dT%H:%M").minute)
        
        # Time Duration
        Duration_in_hr = Arr_hr - Dep_hr
        Duration_in_min = Arr_min - Dep_min
       
        # Totalstops
        Totalstops = int(request.form["Stops"])
        
        # Destination
        destination = request.form["destination"]
        if destination == "KOCHI":
            Destination_Cochin = 1
            Destination_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
            
        elif destination == "HYDERABAD":
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_Hyderabad = 1
            Destination_Kolkata = 0
            
        elif destination == "BANGALORE":
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
            
        elif destination == "KOLKATA":
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 1
            
        else:
            Destination_Cochin = 0
            Destination_Delhi = 1
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
            
        # Origin
        origin = request.form["origin"]
        if origin == "DELHI":
            Source_Chennai = 0
            Source_Delhi = 1
            Source_Kolkata = 0
            Source_Mumbai = 0
            
        elif origin == "CHENNAI":
            Source_Chennai = 1
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 0
            
        elif origin == "BANGALORE":
            Source_Chennai = 0
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 0
            
        elif origin == "KOLKATA":
            Source_Chennai = 0
            Source_Delhi = 0
            Source_Kolkata = 1
            Source_Mumbai = 0
            
        else:
            Source_Chennai = 0
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 1
            
        
        # Airline
        airline = request.form["airline"]
        if airline == "AirIndia":
            Airline_Air_India = 1
            Airline_GoAir = 0
            Airline_IndiGo = 0
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 0
            Airline_Trujet = 0
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 0
            
        elif airline == "GoAir":
            Airline_Air_India = 0
            Airline_GoAir = 1
            Airline_IndiGo = 0
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 0
            Airline_Trujet = 0
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 0
            
        elif airline == "Indigo":
            Airline_Air_India = 0
            Airline_GoAir = 0
            Airline_IndiGo = 1
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 0
            Airline_Trujet = 0
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 0
            
        elif airline == "Jet_Airways":
            Airline_Air_India = 0
            Airline_GoAir = 0
            Airline_IndiGo = 0
            Airline_Jet_Airways = 1
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 0
            Airline_Trujet = 0
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 0
            
        elif airline == "Jet_Airways_Business":
            Airline_Air_India = 0
            Airline_GoAir = 0
            Airline_IndiGo = 0
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business = 1
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 0
            Airline_Trujet = 0
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 0
            
        elif airline == "Multiple_carriers":
            Airline_Air_India = 0
            Airline_GoAir = 0
            Airline_IndiGo = 0
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 1
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 0
            Airline_Trujet = 0
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 0
            
        elif airline == "Multiple_carriers_Premium_economy":
            Airline_Air_India = 0
            Airline_GoAir = 0
            Airline_IndiGo = 0
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 1
            Airline_SpiceJet = 0
            Airline_Trujet = 0
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 0
            
        elif airline == "Spice_Jet":
            Airline_Air_India = 0
            Airline_GoAir = 0
            Airline_IndiGo = 0
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 1
            Airline_Trujet = 0
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 0
            
        elif airline == "Trujet":
            Airline_Air_India = 0
            Airline_GoAir = 0
            Airline_IndiGo = 0
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 0
            Airline_Trujet = 1
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 0
            
        elif airline == "Vistara":
            Airline_Air_India = 0
            Airline_GoAir = 0
            Airline_IndiGo = 0
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 0
            Airline_Trujet = 0
            Airline_Vistara = 1
            Airline_Vistara_Premium_economy = 0
            
        elif airline == "Vistara_Premium_economy":
            Airline_Air_India = 0
            Airline_GoAir = 0
            Airline_IndiGo = 0
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 0
            Airline_Trujet = 0
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 1
            
        else:
            Airline_Air_India = 0
            Airline_GoAir = 0
            Airline_IndiGo = 0
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 0
            Airline_Trujet = 0
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 0
            
        arr = np.array([[Journey_date, Journey_month, Dep_hr, Dep_min, Arr_hr,
                                Arr_min, Duration_in_hr, Duration_in_min, Totalstops,
                                Destination_Cochin, Destination_Delhi, Destination_Hyderabad,
                                Destination_Kolkata, Source_Chennai, Source_Delhi,
                                Source_Kolkata, Source_Mumbai, Airline_Air_India, Airline_GoAir,
                                Airline_IndiGo, Airline_Jet_Airways, Airline_Jet_Airways_Business,
                                Airline_Multiple_carriers,
                                Airline_Multiple_carriers_Premium_economy, Airline_SpiceJet,
                                Airline_Trujet, Airline_Vistara, Airline_Vistara_Premium_economy]])
        
        
        Fare = model.predict(arr)
        Fare1 = int(round(Fare[0],2))
        return render_template('index2.html',myfare = "Approx fare is Rs. {}".format(Fare1))
        print(Fare1)
    return render_template("index2.html")

if __name__ == "__main__":
    app.run(debug= True)









