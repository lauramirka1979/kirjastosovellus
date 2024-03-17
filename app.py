from flask import Flask
from flask import render_template, request
from math import sqrt
	
app = Flask(__name__)

# # Distances of libraries from homes # #									
distncs_1 = {'Kirjastokukkula 1': 1.1, 'Lainalaakso 2': 2.5, 'Niteenneva 3':3.3} 
distncs_2 = {'Kirjastokukkula 1':9.4, 'Lainalaakso 2':7.4, 'Niteenneva 3':8.0} 
distncs_3 = {'Kirjastokukkula 1':5.0, 'Lainalaakso 2':0.5, 'Niteenneva 3':5.2}			
					
distances_by_address = {'Pulkkamäki 7':distncs_1, 'Kahvilanrotko 8':distncs_2, 'Syöksykierre 9':distncs_3}
										
# # Library addresses where the searched material is found # #
lib_addresses = ['Kirjastokukkula 1', 'Lainalaakso 2', 'Niteenneva 3']						

@app.route("/search")
def search():			
	return render_template("search.html")

@app.route("/result", methods=["POST"])
def result():
	genre = request.form["genre"]
	formaatti = request.form.getlist("formaatti")
	message1 = request.form["message1"]
	message2 = request.form["message2"]		
	return render_template("result.html", genre=genre, formaatti=formaatti, 
				message1=message1, message2=message2,
				distances_by_address=distances_by_address, lib_addresses=lib_addresses)
												
				
