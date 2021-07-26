from dateutil import parser
from datetime import datetime


def format_duration_time(timeString):
      timeInMinAndSec = timeString.split(".")
      totalSecs = 0
      if len(timeInMinAndSec)  > 1 :
            totalSecs = (int(timeInMinAndSec[0])  *  60 )  + int(timeInMinAndSec[1])
      else:
          totalSecs = (int(timeInMinAndSec[0])  *  60 )
    
      return format_time(totalSecs)


def get_end_date(orderDate, duration):
    print("inside")  
    timeArray = duration.split(" ")
    hr=min=sec=0
    for hand in timeArray :
        hand = hand.strip()
        if hand.endswith("hr"):
            hrIndex=hand.index("hr")
            hr = int(hand[0:hrIndex])

        if hand.endswith("min"):
            minIndex=hand.index("min")
            min = int(hand[0:minIndex])
  
        if hand.endswith("sec"):
            secIndex=hand.index("sec")
            sec = int(hand[0:secIndex])
       

    totalSec =(orderDate.second + sec) % 60
    totalMin = ((orderDate.minute + min) % 60) + (totalSec) // 60
    totalHr =orderDate.hour + hr + (totalMin // 60)
        
    return  datetime(orderDate.year,orderDate.month,orderDate.day,
                     totalHr,totalMin,totalSec)
       
def to_date_string(date):
    month = date.month if date.month > 9 else f"0{date.month}"
    second=date.second if date.second > 9  else f"0{date.second}"
    return f"{date.year}-{month}-{date.day}T{date.hour}:{date.minute}:{second}"

def format_time(totalSecs):
    formatedTimeString = ""

    hours = totalSecs // 3600
    if hours > 0:
        formatedTimeString += str(hours) +"hr "
    
    min = ((totalSecs % 3600)) // 60
    if min > 0:
        formatedTimeString += str(min) +"min"
    
    sec = totalSecs % 60
    if sec > 0:
        formatedTimeString += " "+str(sec) +"sec"
   
    return formatedTimeString.strip();

    
 
            


             
      

             



    
                

             

