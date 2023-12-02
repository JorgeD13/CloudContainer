from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col

# Crear una sesión de Spark
spark = SparkSession.builder.appName("WordCount").getOrCreate()

# Ruta al archivo CSV de películas
input_file = "/app/app/input_file.csv"  # Reemplaza con la ruta correcta al archivo CSV

# Leer el archivo CSV con Spark
movies_df = spark.read.csv(input_file, header=False, inferSchema=True)

# Seleccionar la columna del título y dividir en palabras
words_df = movies_df.select(explode(split(col("_c0"), " ")).alias("word"))

# Contar las palabras
word_count = words_df.groupBy("word").count().orderBy("count", ascending=False)

# Mostrar el conteo de palabras
word_count.show()

# Guardar el resultado en un archivo de salida
output_file = "/app/app/output"  # Reemplaza con la ruta deseada para el archivo de salida
word_count.write.csv(output_file, header=True)