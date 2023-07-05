FROM python:3.10
RUN mkdir /api_gateway
WORKDIR /api_gateway
ADD req.txt req.txt
RUN pip install -r req.txt
RUN pip install uwsgi gunicorn
ADD . .
RUN mkdir -p logs
CMD ["gunicorn", "-c", "gunicorn.conf", "run:application"]