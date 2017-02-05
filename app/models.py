from app import app, db
from random import randint

class QueryResult(db.Model):
	__tablename__ = 'QueryResult'
	id = db.Column(db.Integer, primary_key = True, autoincrement = True)
	query = db.Column(db.String(100), nullable = False)
	result = db.Column(db.String(100), nullable = False)

	def __init__(self, query, result):
		self.query = query
		self.result = result


class Query(db.Model):
	__tablename__ = 'Query'
	id = db.Column(db.Integer, primary_key = True, autoincrement = True)
	query = db.Column(db.String(100), nullable = False)

	def __init__(self, query):
		self.query = query


def get_random_query():
	random_num = randint(1,2)
	ran_query = db.session.query(Query).filter(Query.id == random_num).first()
	
	return ran_query








	
