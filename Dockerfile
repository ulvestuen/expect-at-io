FROM python:3
RUN curl -sL https://deb.nodesource.com/setup_13.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g newman

RUN groupadd -g 999 expect-at-io && \
    useradd -r -u 999 -g expect-at-io expect-at-io

ADD --chown=expect-at-io:expect-at-io src src/
WORKDIR /src

RUN pip install -r requirements.txt

USER expect-at-io
ENTRYPOINT ["python3", "application.py"]