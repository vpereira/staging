FROM opensuse

RUN zypper in -y osc

COPY oscrc /root/.config/osc/
