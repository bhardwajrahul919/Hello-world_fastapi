# Hello-world_fastapi
python fastapi for Hello world application

- There are 3 files
  1. main1.py : This file is to run the Hello world application using fast api. you should have the python and uvicorn installed and locally and run this command in terminal to run the application
     `python3 -m uvicorn main1:app --reload`
  Application is exposed on 8000 port, so url would be  http://127.0.0.1:8000  to run the application in browser.
2. main.py : This file contains the endpoint who takes value of “integer”, responds with “integer” in json response with value is high or low depending on the number 100. url would be `http://localhost:8000/check_number/number_to_check`. number_to_check would be integer value.
3. test_endoint.py : This is the unit and regression test for one endpoint. it contains all test cases of the integer check endpoint. you can run it by python command `python3 test_endoint.py`
   

  
