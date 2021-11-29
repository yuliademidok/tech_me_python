from habr_parse.database.database import Database
from habr_parse.settings import DATABASES
from habr_parse.database import models


database = Database(DATABASES['URL'])
