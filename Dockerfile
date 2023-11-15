FROM python:3-slim AS get-mcbe

WORKDIR /mcbe

RUN apt-get update && apt-get install -y unzip
RUN pip3 install requests beautifulsoup4

COPY get-mcbe.py .
RUN python3 get-mcbe.py

WORKDIR /mcbe/source
RUN unzip /mcbe/bedrock-server.zip

FROM debian:12-slim

WORKDIR /app

RUN apt-get update && \
  apt-get install -y curl && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

RUN useradd -m mcbe && \
  chown -R mcbe:mcbe /app
COPY --chown=mcbe:mcbe --from=get-mcbe /mcbe/source .

USER mcbe
ENV LD_LIBRARY_PATH=/app
CMD ["/app/bedrock_server"]
