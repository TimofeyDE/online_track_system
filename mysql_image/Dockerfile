# MySQL image
FROM mysql:5.7

COPY ./init-db.sql /docker-entrypoint-initdb.d/

# Set environment variables to configure MySQL
ENV MYSQL_ROOT_PASSWORD=rootpassword
ENV MYSQL_DATABASE=mysql
ENV MYSQL_USER=dartchain
ENV MYSQL_PASSWORD=bitcoin2008

# Expose port 3306 to allow communication to/from the server
EXPOSE 3306


