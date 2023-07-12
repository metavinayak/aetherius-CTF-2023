FROM ubuntu:latest

# RUN echo 'Acquire::http::proxy "http://gateway.iitmandi.ac.in:8080/";' > /etc/apt/apt.conf.d/40proxy

RUN useradd --no-create-home ctfuser && mkdir -p /home/ctfuser

RUN apt-get update 
RUN apt-get install -y python3 python3-pip

WORKDIR /home/ctfuser
COPY *.py .
COPY *.txt .
COPY templates/ ./templates/

# RUN python3 -m venv /home/ctfuser/venv
RUN pip3 install -r requirements.txt

RUN chown -R root:root /home && \
    find /home -type d -exec chmod 555 {} \; && \
    find /home -type f -exec chmod 444 {} \;

USER ctfuser

EXPOSE 5000
CMD ["python3","app.py"]