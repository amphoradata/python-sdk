FROM python:3.7-alpine
WORKDIR /test
COPY ./generated generated

WORKDIR /test/samples
COPY ./samples .
RUN pip install -e ../generated

ENTRYPOINT [ "python" ] 