<h2> Instruction on running this program </h2>
git clone https://github.com/Dong34/SI699.git

cd SI699
cd backend
python3 app.py

<h4> A new console </h4>

cd frontend

npm start

<h2>AWS</h2>
Elastic Block Store -> Volumns -> Modify volume
Network & Security -> Security Groups -> launch-wizard-1 -> inbound rules -> edit inboud rules -> Custom TCP


<h3> To run this program on your own server, you need: </h3>

<h4>Install python env</h4>

wget https://bootstrap.pypa.io/get-pip.py
python3 -m pip install pandas

python3 -m pip install Flask

<h4>install packages</h4>
python3 -m pip install pandas numpy Flask 

python3 -m pip install -U scikit-learn

python3 -m pip install nltk

python3 -m pip install seaborn

python3 -m pip install matplotlib

python3 -m pip install mysql-connector-python 

sudo apt-get update

sudo apt-get install redis

python3 -m pip install redis

nltk.download('wordnet')

<h4>Set mysql database</h4>
sudo apt install mysql-server

sudo systemctl start mysql.service

sudo mysql -u root -p (No password)

CREATE USER ‘si699’@‘localhost’ IDENTIFIED BY ‘SI699_password’;

CREATE USER ‘si699_remote’@‘%’ IDENTIFIED BY ‘SI699_password’;

GRANT ALL ON *.* TO ‘si699’@‘localhost’;

GRANT ALL ON *.* TO ‘si699_remote’@‘%’;

FLUSH PRIVILEGES;

CREATE DATABASE si699_db;

<h4>install npm</h4>
sudo apt install npm
(after git clone)

cd frontend

npm install

