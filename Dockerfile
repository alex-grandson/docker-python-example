FROM python:3.11.4-alpine3.18

RUN apk --update --no-cache add \
  git==2.40.1-r0 \
  make==4.4.1-r1 \
  openssh-client==9.3_p2-r0

RUN apk add --no-cache \
  gnupg==2.4.3-r0 \
  tar==1.34-r3 \
  xz==5.4.3-r0 \
  findutils==4.9.0-r5 \
  gcc==12.2.1_git20220924-r10 \
  libc-dev==0.7.2-r5

RUN pip3 install --no-cache-dir \
  virtualenv==20.24.5 \
  pip==23.3.1

RUN apk add --no-cache \
  nghttp2==1.57.0-r0 \
  nghttp2-libs==1.57.0-r0 \
  libssl3==3.1.4-r1 \
  libcurl==8.4.0-r0 \
  libcrypto3==3.1.4-r1
