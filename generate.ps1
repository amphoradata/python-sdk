rm src/sdk/amphora_api_client
rm src/sdk/test
rm src/sdk/docs
rm src/sdk/dist
docker-compose run generator

echo "numpy" | out-file -append -encoding UTF8 src/sdk/requirements.txt 
echo "pandas" | out-file -append -encoding UTF8 src/sdk/requirements.txt 

