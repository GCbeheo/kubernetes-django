FROM python:3.10.13-bookworm

ENV PYTHONUNBUFFERED=1
ENV DJANGO_PROJECT_DIR=/code
RUN mkdir $DJANGO_PROJECT_DIR
WORKDIR $DJANGO_PROJECT_DIR

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN python3 manage.py migrate
EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]