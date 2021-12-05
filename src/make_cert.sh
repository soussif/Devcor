#script to generate self signed cert in the folder ssl

mkdir -p ssl
openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 \
     -subj "/C=NL/ST=Noord-Holland/L=Hoofddorp/O=SoussifCorp/CN=sqlalchemy.localhost" \
     -keyout ssl/key.pem -out ssl/cert.pem

# you may have to run chmod +x make_cert.sh on the file to run the script