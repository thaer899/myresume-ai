# Create Azure Function App

npm install -g azure-functions-core-tools@3 --unsafe-perm true

az login

RESOURCE_GROUP=myresume-ai
STORAGE_ACCOUNT=myresumestorage1989
FUNCTION_APP_NAME=myresume-express
LOCATION="West Europe"

### Create Storage Account
az storage account create --name $STORAGE_ACCOUNT --location "$LOCATION" --resource-group $RESOURCE_GROUP --sku Standard_LRS

### Create Function App
az functionapp create --resource-group $RESOURCE_GROUP --consumption-plan-location "$LOCATION" --runtime node --functions-version 4 --name $FUNCTION_APP_NAME --storage-account $STORAGE_ACCOUNT --os-type Linux
