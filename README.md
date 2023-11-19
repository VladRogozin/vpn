## A brief comment about the project
The project is divided into 2 applications that interact with each other:

1. account - an application with registration, authorization and profile management.

2. proxy - an application that contains the logic for creating "sites" and the logic for proxying sites. Some of the logic was moved to the utils file.

I connected the postgres container postgres:12.0-alpine to the project.
I connected nginx to the project


## System startup

### Local startup

1. Install the required libraries using the command:

   ```shell
   pip install -r requirements.txt
   
2. Go to the main project directory.

3. Conduct migrations
    ```shell
    python manage.py makemigrations
    python manage.py migrate

4. Start the development server with the command:
   (You can also choose any other port to start the server.)

   ```shell
   python manage.py runserver 14321

##Starting in Docker containers
1. Make sure you have Docker installed and running on your computer.

2. Navigate to the directory containing the docker-compose.yml file.
3. Also, don't forget to perform migrations
   ```shell
   docker compose exec web python manage.py migrate

3. If you have the plugin version of DComps, use the command:
   ```shell
   docker compose up --build

   
4. Else run the system in Docker containers using the command:

    ```shell
   docker-compose up-build.
