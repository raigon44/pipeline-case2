FROM alpine

CMD ["echo","Hello World!!"]

RUN apk add --update \
	python \ 
	py-pip \
   && pip install flask

WORKDIR /app

EXPOSE 80

ADD . /app

CMD ["python","/app/hello.py"]



