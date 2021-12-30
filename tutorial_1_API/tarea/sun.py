
import pymongo 

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://my-api:my-api-password@127.0.0.1:3306/tutorial1"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


dbUrl = pymongo.MongoClient("mongodb://localhost:27017/")

db = dbUrl['Sun']

news = db['News']
category = db['has_category']

new_news = [
    {
    "id" : 1,
    "title" : "Clases presenciales serán obligatorias desde marzo de 2022",
    "date" : "jueves 11, noviembre 2021 ",
    "url" : "https://www.t13.cl/noticia/nacional/clases-presenciales-obligatorias-marzo-2022-11-11-2021",
    "media_outlet": "T13"
    }, 
    {
    "id" : 2,
    "title" : "Clases presenciales serán obligatorias desde marzo de 2022",
    "date" : "jueves 11, noviembre 2021 ",
    "url" : "https://www.t13.cl/noticia/nacional/clases-presenciales-obligatorias-marzo-2022-11-11-2021",
    "media_outlet": "T13"
    }
]

categorys = [
    {"value":"clases presenciales", "id" :1},
    {"value": "mineduc", "id" :2},
    {"value": "clases", "id" :3},
    {"value":"ministerio de educación", "id" :4},
    {"value": "coronavirus en chile", "id" :5},
    {"value": "marzo 2022","id" :6 }
]
x = news.insert_many(new_news)
y = category.insert_many(categorys)






#lista de las bases de datos
dblist = dbUrl.list_database_names()

print(dblist)

if "Sun" in dblist:
  print("La base de datos existe.")

print(db.list_collection_names())