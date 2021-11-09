FROM python:3.8-slim-buster

# Add application sources to a directory that the assemble script expects them 
# and set permissions so that the container runs without root access 
USER 0

# app directory
WORKDIR /app

RUN chown -R 1001:0 /app
USER 1001

# Install app dependencies
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt


# Bundle app source
COPY . .

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

