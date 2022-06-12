from fastapi import FastAPI 
import uvicorn
import tensorflow as tf
from tensorflow import keras
from starlette.responses import RedirectResponse

app = FastAPI(debug=True)
model = tf.keras.models.load_model("app/model/estpricekiloswhitepaper.h5")

@app.get('/')
async def index():
    return RedirectResponse(url="/docs")

@app.post('/ predict')
async def predict(amount: float):
    prediction = model.predict([amount])
    output = prediction[0]
    print(output)
    return{
        'amount': float(amount),
        'price': output.tolist(),
        'type': "kertas",
         }

if __name__ == '__main__':
    uvicorn.run("app", port=8000, reload=True)