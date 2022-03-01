# induction-measuring-gui

### Install requirement library
    pip install requirement.txt or
    pip install mysql-connector-python

### Install mysql server e.g with docker
    docker run --init -d --name mysql-server --env="MYSQL_ROOT_HOST=%" --env="MYSQL_ROOT_PASSWORD=root" -p 3306:3306 --restart=unless-stopped mysql/mysql-server:5.7
    docker ps -> take id of docker container
    docker exec -it mysql-server bash -> connect to mysql inside the container
        mysql -u root -p
        Enter password:
        CREATE USER 'appuser'@'172.17.0.1' IDENTIFIED BY 'hund1234';
        GRANT ALL PRIVILEGES ON *.* TO 'appuser'@'172.17.0.1' WITH GRANT OPTION;
        flush privileges;
        

### To compile this program, you need:
- MySQL is installed
- The project database must be uploaded to the local DBMS

### When all this is done, launch or compile the file 
    python Interface.py or
    python3 Interface.py