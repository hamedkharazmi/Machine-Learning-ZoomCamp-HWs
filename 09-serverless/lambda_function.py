from io import BytesIO
from urllib import request
from PIL import Image
import numpy as np
import tflite_runtime.interpreter as tflite


def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img

def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img

def predict(url):
    img = prepare_image(download_image(url), (150, 150))

    x = np.array(img, dtype='float32')
    x_ = np.array([x])
    X = x_/255.0

    interpreter = tflite.Interpreter('cats-dogs-v2.tflite')
    interpreter.allocate_tensors()

    input_index = interpreter.get_input_details()[0]['index']
    interpreter.set_tensor(input_index, X)

    interpreter.invoke()

    output_index = interpreter.get_output_details()[0]['index']
    preds = interpreter.get_tensor(output_index)

    return preds[0].tolist()

def lambda_handler(event, context):
    url  = event['url']
    result = predict(url)
    return result