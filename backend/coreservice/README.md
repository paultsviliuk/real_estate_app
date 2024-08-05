Core app contains the House model which have the following attributes:

    A name for identification of each house.

    An image data of each house for visual recognition.

    A description of each house. 


Running the app:

1. docker compose up --build

2. Open second terminal and do:

docker compose exec backend sh
python3 manager.py db init
python3 manager.py db migrate 
python3 manager.py db upgrade