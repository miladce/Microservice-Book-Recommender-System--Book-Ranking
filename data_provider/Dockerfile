FROM python:3.10
RUN mkdir /data_provider
WORKDIR /data_provider
ADD req.txt req.txt
RUN pip install -r req.txt
ADD . .
RUN mkdir -p logs
CMD ["python", "run.py"]
