FROM python:3.12-slim AS base

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install "fastapi[standard]"
COPY ./ /code/app
EXPOSE 3000

CMD ["fastapi", "run", "app/main.py", "--port", "3000"]

# http://localhost:3000/docs#/
# docker run -p 3000:3000 ontology