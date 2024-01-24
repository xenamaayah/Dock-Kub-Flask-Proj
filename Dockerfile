FROM python

RUN apt-get update && \
    apt-get install -y iputils-ping

WORKDIR /app

RUN pip install --no-cache-dir Flask==3.0.0

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 3030

HEALTHCHECK --interval=5s --timeout=3s \
  CMD curl --fail http://localhost:3030/health || exit 1

CMD ["python", "app.py"]
