#!/bin/bash

mkdir tempdir
mkdir tempdir/templates
mkdir tempdir/static

cp main.py tempdir/.
cp -r templates/* tempdir/templates/.
cp -r static/* tempdir/static/.
cp userdb.sqlite tempdir/.

echo "FROM python" > tempdir/Dockerfile
echo "RUN pip install flask" >> tempdir/Dockerfile
echo "RUN pip install requests" >> tempdir/Dockerfile

echo "COPY  ./static /home/devasc/CPE41S2/MidProjectG11/group11/static/" >> tempdir/Dockerfile
echo "COPY  ./templates /home/devasc/CPE41S2/MidProjectG11/group11/templates/" >> tempdir/Dockerfile
echo "COPY  main.py /home/devasc/CPE41S2/MidProjectG11/group11/" >> tempdir/Dockerfile
echo "EXPOSE 8080" >> tempdir/Dockerfile

echo "CMD python3 /home/devasc/CPE41S2/MidProjectG11/group11/main.py" >> tempdir/Dockerfile

cd tempdir
docker build -t midtermgroup11 .

docker run -t -d -p 8080:8080 --name midgroup11 midtermgroup11

docker ps -a
