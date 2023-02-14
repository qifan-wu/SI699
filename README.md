git clone https://github.com/Dong34/SI699.git
cd SI699
sudo apt install nodejs npm
cd frontend
npm install 
cd ..
cd ..
wget https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh
bash Anaconda3-2022.10-Linux-x86_64.sh
conda --version
conda create -n my_envs
conda activate my_envs
sudo apt install python3-pip
pip install Flask
cd SI699
cd backend
python app.py
<-- !a new console -->
cd frontend
npm start

