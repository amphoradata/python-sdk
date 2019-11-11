pushd generated
python setup.py sdist
twine upload dist/*
echo "Deleting dist/*"
rm dist/*
popd
