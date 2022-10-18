FROM python:3.9
WORKDIR /new-notes
COPY requirements.txt /new-notes/
RUN pip install -r requirements.txt
COPY . /new-notes/
