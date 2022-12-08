import asyncio
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from io import BytesIO
import barcode
from barcode.writer import ImageWriter

def sum_of_digits(digit :int) -> int:
    return 0 if digit == 0 else int(digit % 10) + sum_of_digits(int(digit / 10))
def check_digit(code :str) -> int:
    weights = [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1]
    return 10 - (sum(list(map(lambda x,y: sum_of_digits(int(x) * y), code, weights))) % 10)

app = FastAPI()

@app.get("/{code}")
async def gen_barcode(code: str):
    headers = {
        'Content-Dispostion': 'inline; filename="pps.png"'
    }
    rv = BytesIO()
    code128 = barcode.get_barcode_class('code128')
    print(code+str(check_digit(code)))
    #code128(code + str(check_digit(code)), writer=ImageWriter()).write(rv)
    rv.seek(0)
    return StreamingResponse(rv, headers=headers,media_type="image/png")

