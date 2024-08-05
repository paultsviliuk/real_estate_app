Before running the app:

update "Your_AMQP_URL" with relevant data.

Running the app:

1. docker compose up --build

2. Open second terminal and do:

docker compose exec backend sh
python3 manager.py db init
python3 manager.py db migrate 
python3 manager.py db upgrade