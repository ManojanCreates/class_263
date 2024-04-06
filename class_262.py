from flask import flask, render_template, request
import requests

app = flask(__name__)

@app.route("/")
def visitors():

	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file.close()

	visitors_count = visitors_count + 1

	counter_write_file = open("count.txt", "w")
	counter_write_file.write(str(visitors_count))
	counter_write_file.close()

	return render_template("index.html", count = visitors_count)

def weather_stats():
	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file.close()

	latitude = request.form['latitude']
	longitude = request.form['longitude']

	api_url = 'https://weather-l6tl.onrender.com/api/getCurrentWeather/31/76'

	response = requests.get(api_url)
	weather_data = response.json()
	print(weather_data)
	return render_template("index.html", weather = weather_data, count = visitors_count

if __name__ == "__main__":
	app.run()

def covid_stats():
	# Load current count
	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file.close()

	#complete the code

#add code for executing flask