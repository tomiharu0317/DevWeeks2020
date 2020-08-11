from flask import (Blueprint, render_template, redirect, url_for, abort)
from flask_login import login_required, current_user

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from myproject import db, app
from myproject.models import User

task_blueprint = Blueprint('task',
                           __name__,
                           template_folder='templates/task')

@task_blueprint.route('/scheduletoday')
@login_required
def scheduletoday():

    return  redirect(url_for('auth.login')) if not current_user.is_authenticated else render_template('schedule_today.html')

@task_blueprint.route('/alltasks')
@login_required
def alltasks():

    return  redirect(url_for('auth.login')) if not current_user.is_authenticated else render_template('all_tasks.html')
