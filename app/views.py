from flask import request, render_template
from app import app, models

@app.route('/', methods=['GET'])
def home():
	if request.method == 'GET':

		ran_query = models.get_random_query()
		search_query=ran_query.query

		return render_template("index.html", google_query = search_query)
