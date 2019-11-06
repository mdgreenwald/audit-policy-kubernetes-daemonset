FROM python:3-alpine

WORKDIR /opt/audit-policy

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .