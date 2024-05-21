from google.cloud import storage

def copy_files_to_folder(source_bucket_name, destination_bucket_name, destination_folder):
    storage_client = storage.Client()

    source_bucket = storage_client.bucket(source_bucket_name)
    destination_bucket = storage_client.bucket(destination_bucket_name)

    blobs = source_bucket.list_blobs()
    
    for blob in blobs:
        # Obtener solo el nombre del archivo sin la ruta
        filename = blob.name.split('/')[-1]
        
        # Crear un nuevo blob en el bucket de destino dentro de la carpeta especificada
        destination_blob_name = f"{destination_folder}/{filename}"
        new_blob = destination_bucket.blob(destination_blob_name)
        
        # Copiar el contenido del blob de origen al nuevo blob
        new_blob.rewrite(blob)
        print(f"Copied {blob.name} to {destination_blob_name} in {destination_bucket_name}")

# Reemplaza con los nombres de tus buckets y la carpeta de destino
source_bucket_name = 'gs://test-ces-infra-cc-dev'
destination_bucket_name = 'gs://test2-ces-infra-cc-dev'
destination_folder = 'ahi'

copy_files_to_folder(source_bucket_name, destination_bucket_name, destination_folder)
