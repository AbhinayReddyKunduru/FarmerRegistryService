FROM python:3.8-alpine

WORKDIR /FarmerRegistryService
COPY . /FarmerRegistryService

RUN pip install -r requirments.txt
#RUN apk --no-cache add python3+ py-mysqldb
ENV PYTHONPATH "${PYTHONPATH}:/"
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]


