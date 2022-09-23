FROM python:3.10.7-bullseye

# Create app directory
WORKDIR /usr/src/app

# Bundle app source
COPY . .

# Python 3 and packages
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

RUN pip install -r requirements.txt

ENV TZ America/Sao_Paulo
EXPOSE 8080
EXPOSE 8008

RUN cd app
ENTRYPOINT ["bash"]