FROM python:3.9 AS build

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt --target /python-libs

COPY . .


FROM python:3.9-slim-buster AS final

WORKDIR /app

COPY --from=build /python-libs /python-libs

COPY  --from=build /app /app

ENV PYTHONPATH=/python-libs

CMD ["python", "sensors.py"]
