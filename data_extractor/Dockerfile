FROM python:3.10
RUN mkdir /data_extractor
WORKDIR /data_extractor
ADD req.txt req.txt
RUN pip install -r req.txt
ADD . .
RUN mkdir -p logs
CMD ["python", "run.py"]