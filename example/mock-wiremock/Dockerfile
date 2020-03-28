FROM openjdk:8

RUN groupadd -g 999 expect-at-io && \
    useradd -r -u 999 -g expect-at-io expect-at-io

RUN mkdir /expect-at-io
RUN chown -R expect-at-io:expect-at-io /expect-at-io
WORKDIR /expect-at-io
ADD __files __files
ADD mappings mappings
ADD start_wiremock.sh start_wiremock.sh
RUN chmod 777 start_wiremock.sh

USER expect-at-io
ENTRYPOINT ["/bin/bash","start_wiremock.sh"]
