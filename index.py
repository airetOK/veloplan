import os
from datetime import timedelta
from functools import wraps

from flask import Flask, render_template, request, redirect, url_for, session
import ast
from flask_session import Session

from entity.veloplan import Veloplan
from repository.plancompleterepository import PlanCompleteRepository
from repository.veloplanrepository import VeloplanRepository
from service.activityservice import ActivityService
from service.veloplanservice import VeloplanService

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(hours=23)
Session(app)

plan_complete_repository = PlanCompleteRepository('data/plan_complete.csv')
veloplan_repository = VeloplanRepository('data/veloplan.csv')
veloplan_service = VeloplanService()
activity_service = ActivityService()


def login_required(f):
    @wraps(f)
    def check_password():
        if session.get('password') is None:
            return redirect(url_for('login'))
        return f()

    return check_password


@app.route('/', endpoint='get_plan')
@login_required
def get_plan():
    week = plan_complete_repository.get_week_where_not_week_complete()
    plan_list = veloplan_repository.get_plan_list_by_week(week)
    is_week_complete = veloplan_service.is_all_activities_complete_in_week(plan_list)
    plan_complete = plan_complete_repository.get_plan_complete_for_week(week)
    goal = f'The goal for the week "{plan_complete[1]}" is to ride more than {plan_complete[2]} km in less than 7 days.'
    return render_template('home.html',
                           plan_list=plan_list,
                           is_week_complete=is_week_complete,
                           goal=goal)


@app.route('/save', endpoint='save_date_and_km', methods=['POST'])
@login_required
def save_date_and_km():
    date = request.form['date']
    km = request.form['km']
    week = plan_complete_repository.get_week_where_not_week_complete()
    veloplan_repository.update_training_in_week(week, date, km)
    return redirect(url_for('get_plan'))


@app.route('/verify', endpoint='verify_week_plan', methods=['POST'])
@login_required
def verify_week_plan():
    plan_list = ast.literal_eval(request.form['plan_list'])
    week = plan_list[0][0]
    week_km = plan_complete_repository.get_week_km_by_week(week)

    if not activity_service.is_week_complete(Veloplan(plan_list), week_km):
        veloplan_repository.delete_records_for_week(week)
        plan_complete = plan_complete_repository.get_plan_complete_for_week(week)
        goal = f'The goal for the week "{plan_complete[1]}" is to ride more than {plan_complete[2]} km ' \
               f'in less than 7 days. You should try again this week. Good luck!'
        return render_template('failed-plan.html',
                               goal=goal)

    plan_complete_repository.update_plan_complete_for_week(week)
    return redirect(url_for('get_plan'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    print(request.method)
    if request.method == 'GET':
        return render_template('login.html')
    else:
        password = request.form.get('password')
        print(os.getenv('PASSWORD'))
        print(password)
        print(os.getenv('PASSWORD') == password)
        if password != os.getenv('PASSWORD'):
            return redirect(url_for('login'))
        session['password'] = password
    return redirect(url_for('get_plan'))
