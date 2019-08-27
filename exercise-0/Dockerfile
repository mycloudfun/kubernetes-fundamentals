FROM python:3.6.8-alpine

COPY ./app /app

COPY ./app/website.html /data/website.html

WORKDIR /app

RUN apk add --update curl && rm -rf /var/cache/apk/*

RUN pip install -r requirements.txt

RUN adduser -S myapp

USER myapp

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["/app/app.py"]
