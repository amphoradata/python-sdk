rm -rf src/sdk/amphora_api_client
rm -rf src/sdk/test
rm -rf src/sdk/docs
rm -rf src/sdk/dist
docker-compose run generator

echo "numpy" >> src/sdk/requirements.txt
echo "pandas" >> src/sdk/requirements.txt
