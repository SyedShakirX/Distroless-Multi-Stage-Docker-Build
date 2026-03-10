#------- STAGE I -------#

FROM python:3.13-slim AS builder

WORKDIR /basedir

COPY . /basedir

RUN pip install -r requirements.txt  --target /basedir/requirements

#------- STAGE II -------#

FROM gcr.io/distroless/python3-debian12

WORKDIR /lessdir

COPY --from=builder /basedir/app.py /lessdir
COPY --from=builder /basedir/requirements /lessdir

EXPOSE 5000

CMD ["app.py"]
