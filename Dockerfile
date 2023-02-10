FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip \
    python3-dev \
    build-essential \
    cmake \
    libgtk-3-dev \
    libboost-all-dev
    boost \
    boost-python

COPY . /app
WORKDIR /app
RUN pip3 install --upgrade pip
RUN pip3 install flask
RUN pip3 install dlib
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]