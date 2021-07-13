def formatDurationTime(timeString):
      timeInMinAndSec = timeString.split(".")
      print(timeInMinAndSec)
      totalSecs = 0
      if len(timeInMinAndSec)  > 1 :
            totalSecs = (int(timeInMinAndSec[0])  *  60 )  + int(timeInMinAndSec[1])
      else:
          totalSecs = (int(timeInMinAndSec[0])  *  60 )
    
      return formatTime(totalSecs)

    

def formatTime(totalSecs):
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
   
    return formatedTimeString;

    
 
            


             
      

             



    
                

             

