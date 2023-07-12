FROM ubuntu:latest

# RUN echo 'Acquire::http::proxy "http://gateway.iitmandi.ac.in:8080/";' > /etc/apt/apt.conf.d/40proxy

RUN apt-get update 
RUN apt-get install -y python3 python3-pip python3-venv socat

RUN python3 -m venv /home/ctfuser/venv

WORKDIR /home/ctfuser
COPY *.py /home/ctfuser/

ENV FLAG ctf{Cool-stuff-out-here-9a92780b-7d15-462a-bcba-4fd6cf962208}

CMD socat TCP-LISTEN:1337,reuseaddr,fork EXEC:"stdbuf -i0 -o0 -e0 /home/ctfuser/venv/bin/python3 /home/ctfuser/chall.py"