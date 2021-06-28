FROM python:3
ADD app.py /
run pip install flask
EXPOSE 5000
CMD ["python", "./app.py"]

