#!/bin/bash
wmversion="2.25.1"
wmfilename="wiremock-jre8-standalone-$wmversion.jar"

if [ -f "$wmfilename" ]; then
	echo "$wmfilename already exists. No Retrieval necessary"
else
	echo "$wmfilename does not exist. Retrieve jar-file.."
	url="https://repo1.maven.org/maven2/com/github/tomakehurst/wiremock-jre8-standalone/$wmversion/$wmfilename"
	wget $url
fi

java -jar $wmfilename --verbose --port 9998 &
