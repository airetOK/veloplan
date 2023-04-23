FROM python:3.10-slim-bullseye
WORKDIR /veloplan

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_APP=index.py
ENV PASSWORD={password}

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
EXPOSE 5000