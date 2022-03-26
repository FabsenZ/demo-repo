FROM python:3.9-bullseye
COPY . /python_files
WORKDIR /python_files
RUN pip install -r requirements.txt
CMD ["python", "app.py"]