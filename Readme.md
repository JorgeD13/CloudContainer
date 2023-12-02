# Comandos usados en el video:
docker build -t spark-wordcount:latest .
docker run -v "$(pwd)":/app spark-wordcount:latest
