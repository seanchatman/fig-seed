FROM arbiterofcool/jdk8-baseimage-docker:0.1
MAINTAINER Sean Chatman <xpointsh@gmail.com>

##### Installing Jenkins #####

RUN apt-get -y install wget git

RUN echo "deb http://pkg.jenkins-ci.org/debian binary/" > /etc/apt/sources.list.d/jenkins.list
RUN wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | apt-key add -
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y jenkins

VOLUME /var/lib/jenkins

RUN echo "/var/lib/jenkins" > /etc/container_environment/JENKINS_HOME

# Start Jenkins
RUN mkdir /etc/service/jenkins
ADD jenkins/run /etc/service/jenkins/run

# Clean up APT when done.
RUN apt-get clean && rm -rf /tmp/* /var/tmp/*
