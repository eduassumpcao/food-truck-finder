# Food Truck App 🚛🌮

This Django project helps you discover the five nearest food trucks in the San Francisco area.

## Run with Docker

To run your Django project with Docker using the provided Docker and Docker Compose files, follow these steps:

1. Build the Docker Images:

    Open a terminal and navigate to the directory containing your Dockerfile and docker-compose.yml files.

    Run the following command to build the Docker images:
    ```bash
    docker-compose build
    ```
2. Run the Docker Containers:

    After the build is complete, run the following command to start the Docker containers:
    ```bash
    docker-compose up
    ```

3. Access the Django Application:

    Once the containers are running, you can access your Django application by opening a web browser and navigating to http://localhost:8000.

4. Stop the Docker Containers:

    To stop the Docker containers, open a new terminal window and run:
    ```bash
    docker-compose down
    ```
    This will stop and remove the containers.

## Run without Docker
1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/eduassumpcao/food-truck-finder.git
   cd food-truck-app
   ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. Apply migrations to set up the database:
    ```bash
    python manage.py migrate
    ```

## Populating Food Truck Data
To populate the app with food truck data, you can use the following management command:

```bash
python manage.py load_foodtruck_data food-truck-data.csv
```

## Running the Development Server
Start the development server to see the app in action:
```bash
python manage.py runserver
```
Visit http://127.0.0.1:8000/ in your browser to access the app.

## Testing
This project is using `pytest` with `pytest-django`.

To test the project run:
 ```bash
 pytest
 ```

 ## Screenshots:
 The Index page:

 <img src="screenshots/index.png"/>

 The Map Page:
  <img src="screenshots/map.png"/>
