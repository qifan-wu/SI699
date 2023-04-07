<h2> Instruction on installing environment </h2>
git clone https://github.com/Dong34/SI699.git
cd SI699

**Install python env**
wget https://bootstrap.pypa.io/get-pip.py
python3 -m pip install pandas
python3 -m pip install Flask

cd backend

sudo python3 app.py

<h4> A new console </h4>

cd frontend

npm start

<h2>AWS</h2>
Elastic Block Store -> Volumns -> Modify volume
Network & Security -> Security Groups -> launch-wizard-1 -> inbound rules -> edit inboud rules -> Custom TCP

<h2> Log into SQL </h2>
mysql -u si699 -p
//then input password

sudo mysql
CREATE USER 'si699_remote'@'%' IDENTIFIED BY 'SI699_password';
GRANT ALL PRIVILEGES ON *.* TO 'si699_remote'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES
