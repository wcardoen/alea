# Development install (Locally)
python3 -m pip install -e Alea-0.1a1

# Create Zipped & .whl file
python3 -m pip install --upgrade build
# Create dist directory with .whl and and .tar.gz file
cd Alea-0.1a1
python3 -m build

# To use 
python3 alea.py --file wim.txt  --type MM  --begin 06/01/2016
or use 
alea --file wim.txt  --type MM  --begin 06/01/2016
