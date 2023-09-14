FROM python:3-slim as get-mcbe

WORKDIR /mcbe

RUN apt-get update && apt-get install -y unzip
RUN pip3 install requests beautifulsoup4

COPY get-mcbe.py .
RUN python3 get-mcbe.py
RUN unzip bedrock-server.zip
RUN ls

FROM ubuntu:22.04

WORKDIR /app

RUN apt-get update && apt-get install -y curl

ENV LD_LIBRARY_PATH=/app
CMD ["./bedrock_server"]
