FROM ubuntu:16.04

RUN mkdir -p /_build/
WORKDIR /_build/
ADD . /_build/

# Install packages and build the environment
# NOTE:
# - A non-priv user named `oscar` will be created with home dir at `/srv/oscar`
# - tmux trigger is `CTRL+t`
RUN apt-get update && apt-get install -y \
    sudo \
    build-essential \
    python3-dev \
    python3-pip \
    python-dev \
    python-pip \
    openssh-server \
    htop \
    curl \
    && curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash - \
    && sudo apt-get install -y nodejs \
    && npm install npm@latest -g \
    && pip3 install -U pip \
    && make init_env \
    && chown funny: -R /srv/funny \
    && mkdir /var/run/sshd

# Clean up
RUN apt-get autoclean \
    && apt-get autoremove \
    && apt-get purge \
    && rm -Rf /_build/
