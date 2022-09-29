from Files.calorie_cal import CalorieCalculator
from Files.temperature import Temperature
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request

app = Flask(__name__)  # Flask Object


# Home Page
class HomePage(MethodView):

    def get(self):
        # Return HTML template to user
        return render_template("index.html")


class CaloriesFormPage(MethodView):
    # place Calories form into calories_form_page.html
    def get(self):
        calories_form = CaloriesForm()
        return render_template("calories_form_page.html", caloriesform=calories_form)
    # use retrieved data and return total calories, will post on same page.
    def post(self):
        calories_form = CaloriesForm(request.form)
        temperature = Temperature(state=calories_form.state.data, city=calories_form.city.data).Get()
        calorie = CalorieCalculator(weight_lbs=float(calories_form.weight.data),
                                    height_cm=float(calories_form.height.data),
                                    age=float(calories_form.age.data),
                                    temperature=temperature)
        total_calories = calorie.Calculate()
        return render_template("calories_form_page.html", caloriesform=calories_form, calories=total_calories,
                               result=True)


class Results(MethodView):
    # use retrieved data and return total calories and post onto results.html page
    def post(self):
        calories_form = CaloriesForm(request.form)
        temperature = Temperature(state=calories_form.state.data, city=calories_form.city.data).Get()
        calorie = CalorieCalculator(weight_lbs=float(calories_form.weight.data),
                                    height_cm=float(calories_form.height.data),
                                    age=float(calories_form.age.data),
                                    temperature=temperature)
        total_calories = calorie.Calculate()
        return render_template("results.html", caloriesform=calories_form, calories=total_calories,
                               result=True)


class CaloriesForm(Form):
    weight = StringField("Weight in Lbs:")
    height = StringField("Height in CM:")
    age = StringField("Age:")
    state = StringField("State:")
    city = StringField("City:")
    button = SubmitField("Calculate")


app.add_url_rule("/", view_func=HomePage.as_view("home_page"))
app.add_url_rule("/calories_form_page", view_func=CaloriesFormPage.as_view("calories_form_page"))
app.add_url_rule("/results", view_func=Results.as_view("results_page"))

app.run(debug=True)
