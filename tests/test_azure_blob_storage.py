import src.azure_blob_storage 
import os

def test_get_random_images():
    result = src.azure_blob_storage.get_random_images()
    assert len(result) == 10

def test_create_blob_from_url():
    # get storage account settings
    storage_connection_string = os.environ.get("STORAGE_CONNECTION_STRING")
    container_name = os.environ.get("STORAGE_CONTAINER")

    result = src.azure_blob_storage.create_blob_from_url(storage_connection_string,container_name)
    assert result == True

def test_create_blob_from_path():
    # get storage account settings
    storage_connection_string = os.environ.get("STORAGE_CONNECTION_STRING")
    container_name = os.environ.get("STORAGE_CONTAINER")

    result = src.azure_blob_storage.create_blob_from_path(storage_connection_string,container_name)
    assert result == True