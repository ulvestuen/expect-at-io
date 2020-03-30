# When docker image is built from this file, the image bundles the latest version of Python 3, which is available under
# a "PSF" license. For details, see https://docs.python.org/3/license.html

# When docker image is built from this file, the image bundles the latest version of Node.js, which is available under
# a "MIT" license. For details, see https://github.com/nodejs/node/blob/master/LICENSE

# When docker image is built from this file, the image bundles the latest version of newman, which is available under a
# "Apache-2.0" license. For details, see https://github.com/postmanlabs/newman/blob/develop/LICENSE.md

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