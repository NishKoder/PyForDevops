FROM python:3.12.9-slim

RUN mkdir -p /app
COPY . main.py /app/
WORKDIR /app
RUN pip install -r requirements.txt
RUN python -m textblob.download_corpora
EXPOSE 8081
CMD ["main.py"]
ENTRYPOINT [ "python" ]