FROM python:3-slim as get-mcbe

WORKDIR /mcbe

RUN apt-get update && apt-get install -y unzip
RUN pip3 install requests beautifulsoup4

COPY get-mcbe.py .
RUN python3 get-mcbe.py

WORKDIR /mcbe/source
RUN unzip /mcbe/bedrock-server.zip

FROM ubuntu:22.04

WORKDIR /app

RUN apt-get update && apt-get install -y curl
COPY --from=get-mcbe /mcbe/source .

ENV LD_LIBRARY_PATH=/app
CMD ["./bedrock_server"]
