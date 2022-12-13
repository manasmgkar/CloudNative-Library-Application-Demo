# start by pulling the python image
FROM python:3.6.9-alpine

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install apt dependencies frozen by pip
RUN apk add gcc musl-dev python3-dev libffi-dev libressl-dev

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT ["python3"]

CMD ["main.py"]