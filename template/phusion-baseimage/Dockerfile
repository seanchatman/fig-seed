# Use phusion/baseimage as base image. To make your builds reproducible, make
# sure you lock down to a specific version, not to `latest`!
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for
# a list of version numbers.
FROM phusion/baseimage:<VERSION>

# Set correct environment variables.
ENV HOME /root

# Regenerate SSH host keys. baseimage-docker does not contain any, so you
# have to do that yourself. You may also comment out this instruction; the
# init system will auto-generate one during boot.
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# ...put your own build instructions here...

RUN mkdir -p /etc/my_init.d
ADD logtime.sh /etc/my_init.d/logtime.sh

#RUN echo Apachai Hopachai > /etc/container_environment/MY_NAME

#RUN echo -e "Apachai Hopachai\n" > /etc/container_environment/MY_NAME_NEWLINE

#RUN chmod 755 /etc/container_environment

#RUN chmod 644 /etc/container_environment.sh /etc/container_environment.json

#RUN /usr/bin/workaround-docker-2267

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*