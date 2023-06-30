from flask import Flask, render_template, request
from datetime import datetime
import time

app = Flask(__name__)# interface between my server and my application wsgi

import pickle
model = pickle.load(open(r'C:/Users/jeeva/OneDrive/Desktop/Rmodel.pkl','rb'))

@app.route('/')#binds to an url
def helloworld():
    return render_template("index.html")

@app.route('/login', methods =['POST'])#binds to an url
def login():
    
    dest_Back_Bay=0
    dest_Beacon_Hill=0
    dest_Boston_University=0
    dest_Fenway=0
    dest_Financial_District=0
    dest_Haymarket_Square=0
    dest_North_End=0
    dest_North_Station=0
    dest_Northeastern_University=0
    dest_South_Station=0
    dest_Theatre_District=0
    dest_West_End=0
    
    
    src_Back_Bay=0
    src_Beacon_Hill=0
    src_Boston_University=0
    src_Fenway=0
    src_Financial_District=0
    src_Haymarket_Square=0
    src_North_End=0
    src_North_Station=0
    src_Northeastern_University=0
    src_South_Station=0
    src_Theatre_District=0
    src_West_End=0
    
    nm_Black=0
    nm_Black_SUV=0
    nm_Lux=0
    nm_Lux_Black=0
    nm_Lux_Black_XL=0
    nm_Lyft=0
    nm_Lyft_XL=0
    nm_Shared=0
    nm_Uber_Pool=0
    nm_Uber_X=0
    nm_Uber_XL=0
    nm_Uber_XL=0
    nm_WAV=0
    
    
    cab =request.form["cab"]
    cab_type= request.form["status"]
    source= request.form["source"]
    destination= request.form["destination"]
    
    time_str = request.form["time"]
    date = request.form["date"]

    time_str = time_str + ":00"
       
    date_string = date + " " + time_str
    
    # Convert to datetime object
    date_time = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
    
    time_now = date_time.time()
    
    # Convert to Unix timestamp
    unix_timestamp = int(time.mktime(date_time.timetuple()))
    
    
    today12am = time_now.replace(hour=0, minute=0, second=0, microsecond=0)
    today6am = time_now.replace(hour=6, minute=0, second=0, microsecond=0)
    today12pm = time_now.replace(hour=12, minute=0, second=0, microsecond=0)
    today6pm = time_now.replace(hour=18, minute=0, second=0, microsecond=0)
    today1159pm = time_now.replace(hour=23, minute=59, second=0, microsecond=0)
    
    
    
    
    time_stamp=unix_timestamp*1000
    
    surge_multiplier = 0
    
    if (time_now > today12am and time_now < today6am):
        surge_multiplier = 3
    elif(time_now > today6am and time_now < today12pm):
        surge_multiplier = 1.75
    elif(time_now > today12pm and time_now < today6pm):
        surge_multiplier = 1.25
    elif(time_now > today6pm and time_now < today1159pm):
        surge_multiplier = 2

    
    
    if (cab=="lyft"):
        c=0
    else:
        c=1
        
        
    if(destination=="Back_Bay"):
        dest_Back_Bay =1
    elif(destination=="Beacon_Hill"):
        dest_Beacon_Hill=1
    elif(destination=="Boston_University"):
        dest_Boston_University=1
    elif(destination=="Fenway"):
        dest_Fenway=1
    elif(destination=="Haymarket_Square"):
        dest_Haymarket_Square=1
    elif(destination=="North_End"):
        dest_North_End =1
    elif(destination=="North_Station"):
        dest_North_Station =1
    elif(destination=="Financial_District"):
        dest_Financial_District=1
    elif(destination=="South_Station"):
        dest_South_Station =1
    elif(destination=="Theatre_District"):
        dest_Theatre_District =1
    elif(destination=="West_End"):
        dest_West_End =1
    elif(destination=="Northeastern_University"):
        dest_Northeastern_University =1
        
        
        
        
    if(source=="Back_Bay"):
        src_Back_Bay =1
    elif(source=="Beacon_Hill"):
        src_Beacon_Hill=1
    elif(source=="Boston_University"):
        src_Boston_University=1
    elif(source=="Fenway"):
        src_Fenway=1
    elif(source=="Haymarket_Square"):
        src_Haymarket_Square=1
    elif(source=="North_End"):
        src_North_End =1
    elif(source=="North_Station"):
        src_North_Station =1
    elif(source=="Financial_District"):
        src_Financial_District=1
    elif(source=="South_Station"):
        src_South_Station =1
    elif(source=="Theatre_District"):
        src_Theatre_District =1
    elif(source=="West_End"):
        src_West_End =1
    elif(source=="Northeastern_University"):
        src_Northeastern_University =1
    
    
    
    
    if(cab_type=="Black"):
        nm_Black=1
    elif(cab_type=="Black_SUV"):
        nm_Black_SUV =1
    elif(cab_type=="Lux"):
         nm_Lux =1
    elif(cab_type=="Lux_Black"):
         nm_Lux_Black =1
    elif(cab_type=="Lux_Black_XL"):
        nm_Lux_Black_XL =1
    elif(cab_type=="Lyft"):
         nm_Lyft =1
    elif(cab_type=="Lyft_XL"):
         nm_Lyft_XL =1    
    elif(cab_type=="Shared"):
        nm_Shared =1
    elif(cab_type=="Uber_Pool"):
         nm_Uber_Pool =1
    elif(cab_type=="Uber_X"):
         nm_Uber_X =1   
    elif(cab_type=="Uber_XL"):
        nm_Uber_XL  =1
    elif(cab_type=="Uber_XL"):
         nm_Uber_XL =1   
    elif(cab_type=="WAV"):
         nm_WAV =1
    
    if(source=="Back_Bay"):

        source_temp = 39.082122
        source_clouds = 0.678432
        source_pressure = 1008.447820
        source_rain = 0.007925
        source_humidity = 0.764073
        source_wind = 6.778528

    elif(source=="Beacon_Hill"):

        source_temp = 39.047285
        source_clouds = 0.677801
        source_pressure = 1008.448356
        source_rain = 0.008297
        source_humidity = 0.765048
        source_wind = 6.810325

    elif(source=="Boston_University"):

        source_temp = 39.047744
        source_clouds = 0.679235
        source_pressure = 1008.459254
        source_rain = 0.007738
        source_humidity = 0.763786
        source_wind = 6.692180

    elif(source=="Fenway"):

        source_temp = 38.964379
        source_clouds = 0.679866
        source_pressure = 1008.453289
        source_rain = 0.007343
        source_humidity = 0.767266
        source_wind = 6.711721

    elif(source=="Financial_District"):

        source_temp = 39.410822
        source_clouds = 0.676730
        source_pressure = 1008.435793
        source_rain = 0.008563
        source_humidity = 0.754837
        source_wind = 6.860019

    elif(source=="Haymarket_Square"):

        source_temp = 39.067897
        source_clouds = 0.676711
        source_pressure = 1008.445239
        source_rain = 0.008660
        source_humidity = 0.764837
        source_wind = 6.843193

    elif(source=="North_End"):

        source_temp = 39.090841
        source_clouds = 0.676730
        source_pressure = 1008.441912
        source_rain = 0.008644
        source_humidity = 0.764054
        source_wind = 6.853117

    elif(source=="North_Station"):

        source_temp = 39.035315
        source_clouds = 0.676998
        source_pressure = 1008.442811
        source_rain = 0.008649
        source_humidity = 0.765545
        source_wind = 6.835755
    
    elif(source=="Northeastern_University"):

        source_temp = 38.975086
        source_clouds = 0.678317
        source_pressure = 1008.444168
        source_rain = 0.007358
        source_humidity = 0.767648
        source_wind = 6.749426

    elif(source=="South_Station"):

        source_temp = 39.394092
        source_clouds = 0.677495
        source_pressure = 1008.438031
        source_rain = 0.008310
        source_humidity = 0.755468
        source_wind = 6.848948

    elif(source=="Theatre_District"):

        source_temp = 39.986711
        source_clouds = 0.677763
        source_pressure = 1008.444742
        source_rain = 0.008405
        source_humidity = 0.767992
        source_wind = 6.834302

    elif(source=="West_End"):

        source_temp = 39.983403
        source_clouds = 0.677247
        source_pressure = 1008.441090
        source_rain = 0.008657
        source_humidity = 0.767266
        source_wind = 6.816233


    if(destination=="Back_Bay"):

        destination_temp = 39.082122
        destination_clouds = 0.678432
        destination_pressure = 1008.447820
        destination_rain = 0.007925
        destination_humidity = 0.764073
        destination_wind = 6.778528

    elif(destination=="Beacon_Hill"):

        destination_temp = 39.047285
        destination_clouds = 0.677801
        destination_pressure = 1008.448356
        destination_rain = 0.008297
        destination_humidity = 0.765048
        destination_wind = 6.810325

    elif(destination=="Boston_University"):

        destination_temp = 39.047744
        destination_clouds = 0.679235
        destination_pressure = 1008.459254
        destination_rain = 0.007738
        destination_humidity = 0.763786
        destination_wind = 6.692180

    elif(destination=="Fenway"):

        destination_temp = 38.964379
        destination_clouds = 0.679866
        destination_pressure = 1008.453289
        destination_rain = 0.007343
        destination_humidity = 0.767266
        destination_wind = 6.711721

    elif(destination=="Financial_District"):

        destination_temp = 39.410822
        destination_clouds = 0.676730
        destination_pressure = 1008.435793
        destination_rain = 0.008563
        destination_humidity = 0.754837
        destination_wind = 6.860019

    elif(destination=="Haymarket_Square"):

        destination_temp = 39.067897
        destination_clouds = 0.676711
        destination_pressure = 1008.445239
        destination_rain = 0.008660
        destination_humidity = 0.764837
        destination_wind = 6.843193

    elif(destination=="North_End"):

        destination_temp = 39.090841
        destination_clouds = 0.676730
        destination_pressure = 1008.441912
        destination_rain = 0.008644
        destination_humidity = 0.764054
        destination_wind = 6.853117

    elif(destination=="North_Station"):

        destination_temp = 39.035315
        destination_clouds = 0.676998
        destination_pressure = 1008.442811
        destination_rain = 0.008649
        destination_humidity = 0.765545
        destination_wind = 6.835755
    
    elif(destination=="Northeastern_University"):

        destination_temp = 38.975086
        destination_clouds = 0.678317
        destination_pressure = 1008.444168
        destination_rain = 0.007358
        destination_humidity = 0.767648
        destination_wind = 6.749426

    elif(destination=="South_Station"):

        destination_temp = 39.394092
        destination_clouds = 0.677495
        destination_pressure = 1008.438031
        destination_rain = 0.008310
        destination_humidity = 0.755468
        destination_wind = 6.848948

    elif(destination=="Theatre_District"):

        destination_temp = 39.986711
        destination_clouds = 0.677763
        destination_pressure = 1008.444742
        destination_rain = 0.008405
        destination_humidity = 0.767992
        destination_wind = 6.834302

    elif(destination=="West_End"):

        destination_temp = 39.983403
        destination_clouds = 0.677247
        destination_pressure = 1008.441090
        destination_rain = 0.008657
        destination_humidity = 0.767266
        destination_wind = 6.816233
    
    distance = 0
    
    if (source=="Back_Bay" and destination=="Beacon_Hill"):
        distance = 1
    elif(source=="Back_Bay" and destination=="Boston_University"):
        distance = 1.4
    elif(source=="Back_Bay" and destination=="Fenway"):
        distance = 1.4
    elif(source=="Back_Bay" and destination=="Financial_District"):
        distance = 1
    elif(source=="Back_Bay" and destination=="Haymarket_Square"):
        distance = 2.3
    elif(source=="Back_Bay" and destination=="North_End"):
        distance = 3.19
    elif(source=="Back_Bay" and destination=="North_Station"):
        distance = 1
    elif(source=="Back_Bay" and destination=="Northeastern_University"):
        distance = 1.08
    elif(source=="Back_Bay" and destination=="South_Station"):
        distance = 2.61
    elif(source=="Back_Bay" and destination=="Theatre_District"):
        distance = 1
    elif(source=="Back_Bay" and destination=="West_End"):
        distance = 1
        
    elif (source=="Beacon_Hill" and destination=="Back_Bay"):
        distance = 1
    elif(source=="Beacon_Hill" and destination=="Boston_University"):
        distance = 2.35
    elif(source=="Beacon_Hill" and destination=="Fenway"):
        distance = 2.36
    elif(source=="Beacon_Hill" and destination=="Financial_District"):
        distance = 1
    elif(source=="Beacon_Hill" and destination=="Haymarket_Square"):
        distance = 1.39
    elif(source=="Beacon_Hill" and destination=="North_End"):
        distance = 2.07
    elif(source=="Beacon_Hill" and destination=="North_Station"):
        distance = 1
    elif(source=="Beacon_Hill" and destination=="Northeastern_University"):
        distance = 1.97
    elif(source=="Beacon_Hill" and destination=="South_Station"):
        distance = 2.48
    elif(source=="Beacon_Hill" and destination=="Theatre_District"):
        distance = 1
    elif(source=="Beacon_Hill" and destination=="West_End"):
        distance = 1
        
        
    elif(source=="Boston_University" and destination=="Back_Bay"):
         distance = 1.4
    elif(source=="Boston_University" and destination=="Beacon_Hill"):
         distance = 2.35  
    elif(source=="Boston_University" and destination=="Fenway"):
        distance = 1
    elif(source=="Boston_University" and destination=="Financial_District"):
        distance = 4.5
    elif(source=="Boston_University" and destination=="Haymarket_Square"):
        distance = 1
    elif(source=="Boston_University" and destination=="North_End"):
        distance = 1
    elif(source=="Boston_University" and destination=="North_Station"):
        distance = 3.48
    elif(source=="Boston_University" and destination=="Northeastern_University"):
        distance = 1
    elif(source=="Boston_University" and destination=="South_Station"):
        distance = 1
    elif(source=="Boston_University" and destination=="Theatre_District"):
        distance = 2.93
    elif(source=="Boston_University" and destination=="West_End"):
        distance = 3.04
        
    elif(source=="Fenway" and destination=="Back_Bay"):
        distance = 1.4
    elif(source=="Fenway" and destination=="Beacon_Hill"):
        distance = 2.36
    elif(source=="Fenway" and destination=="Boston_University"):
        distance = 1       
    elif(source=="Fenway" and destination=="Financial_District"):
        distance = 4.43
    elif(source=="Fenway" and destination=="Haymarket_Square"):
        distance = 1
    elif(source=="Fenway" and destination=="North_End"):
        distance = 1
    elif(source=="Fenway" and destination=="North_Station"):
        distance = 3.07
    elif(source=="Fenway" and destination=="Northeastern_University"):
        distance = 1
    elif(source=="Fenway" and destination=="South_Station"):
        distance = 1
    elif(source=="Fenway" and destination=="Theatre_District"):
        distance = 2.47
    elif(source=="Fenway" and destination=="West_End"):
        distance = 2.82
        
    elif(source=="Financial_District" and destination=="Back_Bay"):
        distance = 1
    elif(source=="Financial_District" and destination=="Beacon_Hill"):
        distance = 1
    elif(source=="Financial_District" and destination=="Boston_University"):
        distance = 4.5
    elif(source=="Financial_District" and destination=="Fenway"):
        distance = 4.43
    elif(source=="Financial_District" and destination=="Haymarket_Square"):
        distance = 1
    elif(source=="Financial_District" and destination=="North_End"):
        distance = 1.03
    elif(source=="Financial_District" and destination=="North_Station"):
        distance = 1
    elif(source=="Financial_District" and destination=="Northeastern_University"):
        distance = 7.46
    elif(source=="Financial_District" and destination=="South_Station"):
        distance = 0.39
    elif(source=="Financial_District" and destination=="Theatre_District"):
        distance = 1
    elif(source=="Financial_District" and destination=="West_End"):
        distance = 1
    
    elif(source=="Haymarket_Square" and destination=="Back_Bay"):
        distance = 2.3
    elif(source=="Haymarket_Square" and destination=="Beacon_Hill"):
        distance = 1.39
    elif(source=="Haymarket_Square" and destination=="Boston_University"):
        distance = 1
    elif(source=="Haymarket_Square" and destination=="Fenway"):
        distance = 1
    elif(source=="Haymarket_Square" and destination=="Financial_District"):
        distance = 1
    elif(source=="Haymarket_Square" and destination=="North_End"):
        distance = 1
    elif(source=="Haymarket_Square" and destination=="North_Station"):
        distance = 0.44
    elif(source=="Haymarket_Square" and destination=="Northeastern_University"):
        distance = 1
    elif(source=="Haymarket_Square" and destination=="South_Station"):
        distance = 1
    elif(source=="Haymarket_Square" and destination=="Theatre_District"):
        distance = 1.23
    elif(source=="Haymarket_Square" and destination=="West_End"):
        distance = 0.71
    
    elif(source=="North_End" and destination=="Back_Bay"):
        distance = 3.19
    elif(source=="North_End" and destination=="Beacon_Hill"):
        distance = 2.07
    elif(source=="North_End" and destination=="Boston_University"):
        distance = 1
    elif(source=="North_End" and destination=="Fenway"):
        distance = 1
    elif(source=="North_End" and destination=="Financial_District"):
        distance = 1.03
    elif(source=="North_End" and destination=="Haymarket_Square"):
        distance = 1
    elif(source=="North_End" and destination=="North_Station"):
        distance = 1.01
    elif(source=="North_End" and destination=="Northeastern_University"):
        distance = 1
    elif(source=="North_End" and destination=="South_Station"):
        distance = 1
    elif(source=="North_End" and destination=="Theatre_District"):
        distance = 1.5
    elif(source=="North_End" and destination=="West_End"):
        distance = 1.11
        
    elif(source=="North_Station" and destination=="Back_Bay"):
        distance = 1
    elif(source=="North_Station" and destination=="Beacon_Hill"):
        distance = 1
    elif(source=="North_Station" and destination=="Boston_University"):
        distance = 3.48
    elif(source=="North_Station" and destination=="Fenway"):
        distance = 3.07
    elif(source=="North_Station" and destination=="Financial_District"):
        distance = 1
    elif(source=="North_Station" and destination=="Haymarket_Square"):
        distance = 0.44
    elif(source=="North_Station" and destination=="North_End"):
        distance = 1.01
    elif(source=="North_Station" and destination=="Northeastern_University"):
        distance = 3.24
    elif(source=="North_Station" and destination=="South_Station"):
        distance = 1.76
    elif(source=="North_Station" and destination=="Theatre_District"):
        distance = 1
    elif(source=="North_Station" and destination=="West_End"):
        distance = 1   
     
    elif(source=="Northeastern_University" and destination=="Back_Bay"):
        distance = 1.08
    elif(source=="Northeastern_University" and destination=="Beacon_Hill"):
        distance = 1.97
    elif(source=="Northeastern_University" and destination=="Boston_University"):
        distance = 1      
    elif(source=="Northeastern_University" and destination=="Fenway"):
        distance = 1
    elif(source=="Northeastern_University" and destination=="Financial_District"):
        distance = 7.46
    elif(source=="Northeastern_University" and destination=="Haymarket_Square"):
        distance = 1
    elif(source=="Northeastern_University" and destination=="North_End"):
        distance = 1
    elif(source=="Northeastern_University" and destination=="North_Station"):
        distance = 3.24  
    elif(source=="Northeastern_University" and destination=="South_Station"):
        distance = 1
    elif(source=="Northeastern_University" and destination=="Theatre_District"):
        distance = 2.81
    elif(source=="Northeastern_University" and destination=="West_End"):
        distance = 2.78   
    
    elif(source=="South_Station" and destination=="Back_Bay"):
        distance = 2.61
    elif(source=="South_Station" and destination=="Beacon_Hill"):
        distance = 2.48
    elif(source=="South_Station" and destination=="Boston_University"):
        distance = 1
    elif(source=="South_Station" and destination=="Fenway"):
        distance = 1
    elif(source=="South_Station" and destination=="Financial_District"):
        distance = 0.39
    elif(source=="South_Station" and destination=="Haymarket_Square"):
        distance = 1
    elif(source=="South_Station" and destination=="North_End"):
        distance = 1
    elif(source=="South_Station" and destination=="North_Station"):
        distance = 1.76
    elif(source=="South_Station" and destination=="Northeastern_University"):
        distance = 1
    elif(source=="South_Station" and destination=="Theatre_District"):
        distance = 1.08
    elif(source=="South_Station" and destination=="West_End"):
        distance = 2.05
        
    elif(source=="Theatre_District" and destination=="Back_Bay"):
        distance = 1
    elif(source=="Theatre_District" and destination=="Beacon_Hill"):
        distance = 1
    elif(source=="Theatre_District" and destination=="Boston_University"):
        distance = 2.93
    elif(source=="Theatre_District" and destination=="Fenway"):
        distance = 2.47
    elif(source=="Theatre_District" and destination=="Financial_District"):
        distance = 1
    elif(source=="Theatre_District" and destination=="Haymarket_Square"):
        distance = 1.23
    elif(source=="Theatre_District" and destination=="North_End"):
        distance = 1.5
    elif(source=="Theatre_District" and destination=="North_Station"):
        distance = 1
    elif(source=="Theatre_District" and destination=="Northeastern_University"):
        distance = 2.81
    elif(source=="Theatre_District" and destination=="South_Station"):
        distance = 1.08
    elif(source=="Theatre_District" and destination=="West_End"):
        distance = 1
        
    elif(source=="West_End" and destination=="Back_Bay"):
        distance = 1
    elif(source=="West_End" and destination=="Beacon_Hill"):
        distance = 1
    elif(source=="West_End" and destination=="Boston_University"):
        distance = 3.04
    elif(source=="West_End" and destination=="Fenway"):
        distance = 2.82
    elif(source=="West_End" and destination=="Financial_District"):
        distance = 1
    elif(source=="West_End" and destination=="Haymarket_Square"):
        distance = 0.71
    elif(source=="West_End" and destination=="North_End"):
        distance = 1.11
    elif(source=="West_End" and destination=="North_Station"):
        distance = 1
    elif(source=="West_End" and destination=="Northeastern_University"):
        distance = 2.78
    elif(source=="West_End" and destination=="South_Station"):
        distance = 2.05
    elif(source=="West_End" and destination=="Theatre_District"):
        distance = 1
        

    t=[[distance, c, time_stamp, surge_multiplier, source_temp,
       source_clouds, source_pressure, source_rain, source_humidity,
       source_wind, destination_temp, destination_clouds,
       destination_pressure, destination_rain, destination_humidity,
       destination_wind, 
       
       dest_Back_Bay, dest_Beacon_Hill,
       dest_Boston_University, dest_Fenway, dest_Financial_District,
       dest_Haymarket_Square, dest_North_End, dest_North_Station,
       dest_Northeastern_University, dest_South_Station,
       dest_Theatre_District, dest_West_End, 
       
       
       src_Back_Bay,
       src_Beacon_Hill, src_Boston_University, src_Fenway,
       src_Financial_District, src_Haymarket_Square, src_North_End,
       src_North_Station, src_Northeastern_University, src_South_Station,
       src_Theatre_District, src_West_End, nm_Black, nm_Black_SUV,
       nm_Lux,nm_Lux_Black, nm_Lux_Black_XL, nm_Lyft, nm_Lyft_XL,
       nm_Shared, nm_Uber_Pool, nm_Uber_X, nm_Uber_XL, nm_WAV]]
    output= model.predict(t)
    print(output)  
        
    return render_template("index.html",y = "The predicted Cab price is $ " + str(output[0]) )

#@app.route('/admin')#binds to an url
#def admin():
   # return "Hey Admin How are you?"

if __name__ == '__main__' :
    app.run(debug= False)
    