# Utilizamos una imagen base de Apache Spark compatible con la versión requerida
FROM bde2020/spark-base:3.2.0-hadoop3.2
#FROM apache/spark

# Establecemos el directorio de trabajo en la imagen
WORKDIR /app

# Copiamos el script de Python al contenedor
COPY app/wordcount.py /app
RUN chmod a+x ./wordcount.py

# Copiamos el archivo CSV de películas al contenedor
COPY app/input_file.csv /app
RUN chmod a+x ./input_file.csv

# Ejecutamos el script de conteo de palabras utilizando spark-submit al iniciar el contenedor
CMD ["/spark/bin/spark-submit", "--master", "local[*]", "/app/app/wordcount.py"]
