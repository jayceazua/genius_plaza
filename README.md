# genius_plaza
### Run Django Commands
 - docker-compose run web python3 /code/manage.py [options]

### Startup Docker Instructions:
1. docker build .
2. docker-compose build --no-cache 
3. docker-compose up

## Best-to-use:
Postman:
Base_url: `http://localhost:8000`

Get-Recipe-from-specific-user:
 - _INDEX: `admin/<user>`_



### Recipe-Endpoints:
 - INDEX: `recipes`
 - CREATE: `recipes/`
 - READ: `recipes/<int:id>`
 - UPDATE: `recipes/<int:id>`
 - DELETE: `recipes/<int:id>`

 ### Step-Endpoints: 
 - CREATE: `steps/`
 - READ: `steps/<int:id>`
 - UPDATE: `steps/<int:id>`
 - DELETE: `steps/<int:id>`

### Ingredient-Endpoints:
 - CREATE: `ingredients/`
 - READ: `ingredients/<int:id>`
 - UPDATE: `ingredients/<int:id>`
 - DELETE: `ingredients/<int:id>`

