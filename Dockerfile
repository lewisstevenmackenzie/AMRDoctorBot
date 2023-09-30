FROM rasa/rasa:latest-spacy-en

WORKDIR '/app'
COPY . /app
USER root

COPY ./train_model.sh /app/train_model.sh
COPY ./data /app/data
COPY ./models /app/models

RUN rasa train

VOLUME /app
VOLUME /app/data
VOLUME /app/models

CMD ["run","-m","/app/models","--enable-api","--cors","*","--debug" ,"--endpoints", "endpoints.yml", "--log-file", "out.log", "--debug"]