VIRTUAL_ENV_NAME=".env"
REQUIREMENTS_PATH="requirements/main.md"

# create virtual env
python3 -m venv $VIRTUAL_ENV_NAME

# ignore virtual env
echo $VIRTUAL_ENV_NAME >> .gitignore

# activate and install dependencies in virtual environment
source $VIRTUAL_ENV_NAME/bin/activate
python3 -m pip install --upgrade pip
pip install -r $REQUIREMENTS_PATH