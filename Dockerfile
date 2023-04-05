FROM python:3.8-buster

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

RUN curl -fsSL https://deb.nodesource.com/setup_19.x | bash - &&\
apt-get install -y nodejs

RUN npm install

RUN npm run styles

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]