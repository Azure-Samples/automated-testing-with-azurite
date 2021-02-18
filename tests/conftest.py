from azure.storage.blob import BlobServiceClient
import os

def pytest_generate_tests(metafunc):
    os.environ['STORAGE_CONNECTION_STRING'] = 'DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;'
    os.environ['STORAGE_CONTAINER'] = 'test-container'

    # Crete container for Azurite for the first run
    blob_service_client = BlobServiceClient.from_connection_string(os.environ.get("STORAGE_CONNECTION_STRING"))
    try:
        blob_service_client.create_container(os.environ.get("STORAGE_CONTAINER"))
    except Exception as e:
        print(e)