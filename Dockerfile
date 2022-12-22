# Filename: Dockerfile
FROM python:3.8-alpine

COPY . /code
WORKDIR /code

RUN pip install -r FarmerRegistryService/requirments.txt
ENV PYTHONPATH "${PYTHONPATH}:/FarmerRegistryService"
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "FarmerRegistryService/app.py" ]


