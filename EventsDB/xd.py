from pymongo import MongoClient

# Establecer la conexión con la base de datos
client = MongoClient("mongodb+srv://project:project@datos.ltwggtv.mongodb.net/?retryWrites=true&w=majority&appName=Datos")
db = client["Datos"]  # Reemplaza <database_name> con el nombre de tu base de datos
collection = db["Datos"]  # Reemplaza <collection_name> con el nombre de tu colección

# Definir el documento que deseas insertar
documento = {
    "titulo": "Mi documento",
    "contenido": "Este es el contenido de mi documento",
    "autor": "Nombre del autor"
}

# Insertar el documento en la colección
insertion_result = collection.insert_one(documento)

# Imprimir el ID del documento insertado
print("Documento insertado con el ID:", insertion_result.inserted_id)
