FROM python:3.8

RUN python -m venv /opt/venv

USER root

WORKDIR /app

RUN . /opt/venv/bin/activate && pip install --upgrade pip

# Install dependencies
COPY requirements.txt /app/
RUN . /opt/venv/bin/activate && pip install -r requirements.txt

# Run job
COPY beam-flink-pipeline.py  /app
CMD . /opt/venv/bin/activate && exec python beam-flink-pipeline.py