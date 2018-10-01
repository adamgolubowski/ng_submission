FROM python:3.6
WORKDIR /ng
COPY requirements.txt /ng/
RUN pip install -r /ng/requirements.txt
COPY . /ng
EXPOSE 8000
STOPSIGNAL SIGINT
RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
