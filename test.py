import banana_dev as client
from io import BytesIO
from PIL import Image
import base64
import time

# Localhost test
my_model = client.Client(
    api_key="",
    model_key="",
    url="http://localhost:8000",
)

inputs = {
    "prompt": "An astronaut riding a green horse",
}

# Call your model's inference endpoint on Banana.
# If you have set up your Potassium app with a
# non-default endpoint, change the first
# method argument ("/")to specify a
# different route.
t1 = time.time()
result, meta = my_model.call("/", inputs)
t2 = time.time()

result_img = result["output"]
image_encoded = result_img.encode('utf-8')
image_bytes = BytesIO(base64.b64decode(image_encoded))
image = Image.open(image_bytes)
image.save("output.jpg")
print("Time to run: ", t2 - t1)