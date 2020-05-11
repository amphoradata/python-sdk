rm src/sdk/amphora_api_client
rm src/sdk/test
rm src/sdk/docs
rm src/sdk/dist
docker-compose run generator

echo "numpy" >> src/sdk/requirements.txt
echo "pandas" >> src/sdk/requirements.txt
