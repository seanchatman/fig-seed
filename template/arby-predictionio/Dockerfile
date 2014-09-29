FROM phusion/baseimage:0.9.13
MAINTAINER Sean Chatman <xpointsh@gmail.com>

ENV JAVA_VERSION 8u40

RUN apt-get update && apt-get install -y \
    curl \
    openjdk-7-jdk \
    unzip \
    wget \
    git

WORKDIR root

RUN wget http://download.prediction.io/PredictionIO-0.8.0.tar.gz

RUN tar zxvf PredictionIO-0.8.0.tar.gz

RUN wget http://d3kbcqa49mib13.cloudfront.net/spark-1.1.0-bin-hadoop2.4.tgz

RUN tar zxvf spark-1.1.0-bin-hadoop2.4.tgz

RUN wget https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.3.2.tar.gz

RUN tar zxvf elasticsearch-1.3.2.tar.gz

RUN wget http://archive.apache.org/dist/hbase/hbase-0.98.6/hbase-0.98.6-hadoop2-bin.tar.gz

RUN tar zxvf hbase-0.98.6-hadoop2-bin.tar.gz

RUN echo '/usr/lib/jvm/java-7-openjdk-amd64/' > /etc/container_environment/JAVA_HOME

RUN rm PredictionIO-0.8.0.tar.gz zxvf spark-1.1.0-bin-hadoop2.4.tgz elasticsearch-1.3.2.tar.gz hbase-0.98.6-hadoop2-bin.tar.gz