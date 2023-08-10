# This is a potassium-standard dockerfile, compatible with Banana

# Don't change this. Currently we only support this specific base image.
FROM pytorch/pytorch:1.11.0-cuda11.3-cudnn8-runtime

WORKDIR /

# Install git
RUN apt-get update && apt-get install -y git libgl1-mesa-glx libglib2.0-0

# Install python packages
RUN pip3 install --upgrade pip
ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Set HuggingFace token
ARG HF_AUTH_TOKEN=""
ENV HF_AUTH_TOKEN=${HF_AUTH_TOKEN}

# Set HuggingFace model id
ARG MODEL_ID="stabilityai/stable-diffusion-2-1-base"
ENV MODEL_ID=${MODEL_ID}

# Add your model weight files 
# (in this case we have a python script)
ADD download.py .
RUN python3 download.py

ADD . .

EXPOSE 8000

CMD python3 -u app.py