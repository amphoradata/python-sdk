pushd generated
python setup.py sdist
twine upload --skip-existing dist/*
echo "Deleting dist/*"
rm dist/*
popd
