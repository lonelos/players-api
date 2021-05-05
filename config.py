host = 'localhost'
port = 54322
user = 'postgres'
password = 'mysecretpassword'
database = 'ci_players'

DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
