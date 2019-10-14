pushd generated
python setup.py sdist
twine upload dist/*
popd
