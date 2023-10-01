FROM python:3.11.4-alpine3.18

RUN     apk --update add \
            git \
            make \
            openssh-client

# COPY    ssh_config /root/.ssh/config
# COPY    ssh_id /root/.ssh/id_ed25519
# RUN     chmod 600 /root/.ssh/id_ed25519

RUN     apk add --no-cache \
            git \
            make \
		    gnupg \
		    tar \
		    xz \
		    findutils \
		    gcc \
		    libc-dev \
            openssh-client

RUN     pip3 install --no-cache virtualenv