# When docker image is built from this file, the image bundles OpenJDK 8, which is available under a
# "GNU GPLv2" license with Classpath Exception. For details, see https://openjdk.java.net/legal/gplv2+ce.html

# When docker image is built from this file, the image bundles the latest version of WireMock, which is available under
# a "Apache-2.0" license. For details, see https://github.com/tomakehurst/wiremock/blob/master/LICENSE.txt

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
