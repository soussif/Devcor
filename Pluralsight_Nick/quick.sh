src/./make_cert.sh
pylint src/*.py
pytest src/test_unit.py
sudo docker-compose down --volumes
sudo docker-compose up --build --detach
./wait_for_https.sh 60
pytest src/test_system.py
