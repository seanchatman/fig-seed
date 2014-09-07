FROM ruby
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev
RUN mkdir /code
WORKDIR /code
ADD Gemfile /code/Gemfile
RUN bundle install
ADD . /code
