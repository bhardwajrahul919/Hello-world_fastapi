from fastapi import FastAPI  
  
app = FastAPI()  
  
@app.get("/check_number/{value}")  
def check_number(value: int):  
    if value > 100:  
        result = "high"  
    elif value < 100:  
        result = "low"  
    else:  
        result = "equal"  
    return {"result": result}  
  
