FROM python:3.8

# RUN which python
# RUN python --version

WORKDIR /app
ADD . .

# RUN apt-get update && apt-get install -y cmake
ENV PYTHONPATH=/app:/app
EXPOSE 5000

RUN pip install -r requirements.txt

CMD [ "python","app.py" ]
