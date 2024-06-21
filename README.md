
## Check used existing libraries

```bash

pip freeze > req.txt 
pip freeze > requirements.txt 

```





## Setup of Virtual Environment

```bash
# clone repo
git clone https://github.com/asdasdasd

# create virtual environment
python -m venv venv

# activate virtual environment
## for MACOS
source venv/bin/activate
## for Windows
source venv/Scripts/activate


# install requirements
pip install -r requirements.txt

```





## Extracting Library Dependencies

```bash

pip install pipreqs

# overwrite requirements.txt
pipreqs . --force

```
