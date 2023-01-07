# Filename: Dockerfile
FROM python:3.8-alpine

COPY . /FarmerRegistryService
WORKDIR /FarmerRegistryService

RUN pip install -r requirments.txt
ENV PYTHONPATH "${PYTHONPATH}:/"

EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]


