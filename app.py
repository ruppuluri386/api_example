
#mport sys
#
#ef add (x,y):
#   return x+y
#
#f __name__ == "__main__":
#   x=sys.argv[1]
#   y=sys.argv[2]
#
#   result = add(float(x), float(y))
#   print(f"The sum of {x} and {y} is {result}.")
  

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/add")
def add (x,y):
   return float(x)+float(y)
@app.get("/subtract")
def subtract (x,y):
   return float(x)-float(y)

if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0", port=9321)
