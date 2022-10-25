FROM featureoverload/uvicorn-gunicorn:python3.9

LABEL maintainer="FeatureOverload <featureoverload@gmail.com>"

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./app /app
