mkvirtualenv slackbot-template
pip install --upgrade pip
pip install -r requirements.txt
nvm use stable # v9.2.0
npm install -g localtunnel
lt --port 5000 &
python run.py &