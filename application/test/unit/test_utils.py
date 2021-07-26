from datetime import datetime
import application.utils as utils


def test_formatTimeDuration():
    testCase =[
        ("25.3", "25min 3sec"),
        ("65.40", "1hr 5min 40sec")
    ] 

    for input, output in testCase:
            assert utils.format_duration_time(input) == output
            

def test_getEndDate():
        testCase =[
            (datetime(2021,7,11,21,13,22), "45min 20sec","2021-07-11T21:58:42")
        ]

        for input1,input2,output in testCase:
            date=utils.get_end_date(input1,input2)
            expected = utils.to_date_string(date)
            assert expected == output 
  
 



