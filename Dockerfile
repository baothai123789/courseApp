FROM python:3-alpine
WORKDIR /courseApp
COPY ./requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt 
COPY . .
EXPOSE 5000
ENV DEV_DATABASE_URI = 'courseApp.sqlite'
CMD ["flask","run"]
