echo [$(date)]:"START"
echo [$(date)]:"creating env with python 3.8 version"
conda create --prefix ./env python=3.8 -y
echo [$(date)]:"activating enviroment"
source activate ./env
echo [$(date)]:"installing the devlopment enviroment"
pip install -r requirements_dev.txt
echo [$(date)]:"END"