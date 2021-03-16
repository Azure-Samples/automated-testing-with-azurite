---
page_type: sample
languages:
  - python
  - yaml
products:
  - azure
  - azure-devops
  - azure-blob-storage
name: Azure Blob Storage testing Pipeline with Azurite
description: Using Azurite to run blob storage tests in Azure DevOps Pipeline with a sample application
urlFragment: automated-testing-with-azure
---

# Using Azurite to run blob storage tests in Azure DevOps Pipeline

## Overview

This repo demonstrates the approach for writing automated tests with a short feedback loop (i.e. unit tests) against security considerations (private endpoints) for Azure Blob Storage functionality.

Once private endpoints are enabled for the Azure Storage accounts, tests will fail, when executed locally or as part of a pipeline, because this connection will be blocked.

This repo contains a sample for Azure Blob Storage that will upload images from a url and upload files from a local folder. To run, `cp sample_env.txt .env` file to load environment variables for running code on local or pipeline and using `conftest.py` to load environment variables for tests.

## Getting Started

### Folder structure

Here's the folder structure for the sample:

- `build`
  - `azure-pipelines.yml` - Azure Pipelines yaml file
- `data` - Local files examples to be uploaded to Blob Storage
- `src`
  - `azure_blob_storage.py` - Azure Blob Storage Sample Code
- `tests`
  - `conftest.py` - Configuration file for running tests
  - `test_azure_blob_storage.py` - Azure Blob Storage Test Code
- `.env` - Environment variable files for Blob Storage
- `docker-compose.yml` - Docker Compose yaml file to run Azurite Docker Image
- `requirements.txt` - Required pip packages to run python code on your local and pipeline
- `requirements_dev.txt` - Required pip packages to run test code on your local and pipeline

### Prerequisites

- [Azure Subscription](https://docs.microsoft.com/en-us/azure/cost-management-billing/manage/create-subscription#:~:text=Create%20Subscription%20Azure%201%20Sign%20in%20to%20the,for%20each%20type%20of%20billing%20account.%20See%20More.)
- [Azure Resource Group](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal#:~:text=Create%20resource%20groups%201%20Sign%20in%20to%20the,newly%20created%20resource%20group%20to%20open%20it.)
- [Github Account](https://github.com/)
- [Latest Stable Python Version](https://www.python.org/downloads/). When installing python, please add the specific version you will be using to the path. This will ensure a consistent experience when using the python commands in the tutorial.
- [Node JS](https://nodejs.org/en/download/)
- [Docker](https://docs.docker.com/desktop/): if installing Azurite using docker-compose.
- [Azurite](https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azurite#install-and-run-azurite-by-using-npm)
- [Azure Devops Account](https://www.dev.azure.com/) with an available project to house the deployment pipeline.

### Install and Launch Azurite in local environment

There are several different ways to install and run Azurite on your local system as listed [here](https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azurite#install-and-run-azurite-by-using-npm). In this document, we will cover `Install and run Azurite using NPM` and `Install and run the Azurite Docker image`.

#### a. Using NPM

In order to run Azurite V3 you need Node.js >= 8.0 installed on your system. Azurite works cross-platform on Windows, Linux, and OS X.

After the Node.js installation, you can install Azurite simply with npm which is the Node.js package management tool included with every Node.js installation.

```bash
# Install Azurite
npm install -g azurite

# Create azurite directory
mkdir c:/azurite

# Launch Azurite for Windows
azurite --silent --location c:\azurite --debug c:\azurite\debug.log

#Launch Azurite for MacOs or Linux:
azurite -s -l /usr/local/lib/node_modules/azurite -d /usr/local/lib/node_modules/azurite/debug.log
```

#### b. Using docker image

Docker Compose will run the docker image using the `docker-compose.yml` file.

```bash
docker-compose up
```

Either option (a) Using NPM or (b) Using docker image, the output should be:

```shell
Azurite Blob service is starting at http://127.0.0.1:10000
Azurite Blob service is successfully listening at http://127.0.0.1:10000
Azurite Queue service is starting at http://127.0.0.1:10001
Azurite Queue service is successfully listening at http://127.0.0.1:10001
```

### Run tests on local

Python 3.8 is used for this, but it should also work fine on other 3.6+ versions.

1. To test and see how these endpoints are running, you can attach your local blob storage to the [**Azure Storage Explorer**](https://azure.microsoft.com/en-us/features/storage-explorer/). In Azure Storage Explorer:

- right click on `Storage Accounts` and select `Connect to Azure Storage`
  ![connect storage](assets/storage_account.png)

- then select `Attach to a local emulator`  
   ![connect blob](assets/blob_storage_connection.png)

2. Provide a Display name and port number, then your connection will be ready and you can use Storage Explorer to manage your local blob storage.  
   ![attach to local](assets/blob_storage_connection_attach.png)

Do not forget to start your emulator, Storage Explorer will not start it for you.

3. Create a virtual python environment

   `python3 -m venv env`  
   `source env/bin/activate` [on Linux] or `env/scripts/activate` [on Windows]

4. Install the dependencies  
   `python3 -m pip install -r requirements_dev.txt`
5. Run tests:

   ```bash
   python3 -m pytest ./tests
   ```

After the tests run, you can see the files in your local blob storage.

![https local blob](assets/http_local_blob_storage.png)

## Run tests on Azure DevOps Pipelines

After successfully running tests on local, run the `azure-pipelines` build yaml file using Azure DevOps Pipelines.

**Note:** You will need

- an existing [Azure subscription](https://azure.microsoft.com/en-us/free/)
- an existing [Azure DevOps](https://azure.microsoft.com/en-us/services/devops/) organization and project.

1. Login to Azure DevOps

2. Under the Organisation and Project, select the sample folder git Repo and Configure a Pipeline using the `build/azure-pipelines.yml`

3. Run the Pipeline

After a successful set up and running the pipeline in Azure DevOps Pipelines, the result should look like:

![azure pipelines](assets/azure_pipeline.png)

## License:

See [LICENSE](LICENSE).

## Code of Conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Contributing

See [CONTRIBUTING](CONTRIBUTING.MD)
