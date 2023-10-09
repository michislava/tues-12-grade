FROM python:3.9-slim-buster
# tva e lightweight linux os with python installed
WORKDIR /app
# relative file paths
COPY requirements.txt requirements.txt
#copy requirements.txt into the image
RUN pip install -r requirements.txt
# pip installs modules into the image
COPY . .
# adding source code into the image (all files in the working directory)
CMD ["python3", "app.py"]