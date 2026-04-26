FROM mcr.microsoft.com/playwright/python:v1.42.0-jammy

ENV ORACLE_HOME=/opt/oracle/instantclient
ENV TNS_ADMIN=/opt/oracle/network_config
ENV LD_LIBRARY_PATH=$ORACLE_HOME
ENV PATH=$PATH:$ORACLE_HOME

WORKDIR /opt/oracle

RUN apt-get update && apt-get install -y --no-install-recommends \
    libaio1 \
    unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY drivers/instantclient-basic-linux.zip /tmp/
RUN unzip /tmp/instantclient-basic-linux.zip -d /opt/oracle \
    && mv /opt/oracle/instantclient_* $ORACLE_HOME \
    && rm /tmp/instantclient-basic-linux.zip

RUN mkdir -p $TNS_ADMIN
COPY network_config/ $TNS_ADMIN/

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /app

CMD ["python"]