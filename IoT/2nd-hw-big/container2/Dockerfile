FROM python:3.9-slim-buster AS build

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .


FROM alpine AS final

WORKDIR /app

RUN apk --no-cache add python3

COPY  --from=build /app /app

CMD ["python3", "sensors.py"]