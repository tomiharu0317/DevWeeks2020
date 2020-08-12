from flask import (Blueprint, render_template, redirect, url_for, abort)
from flask_login import login_required, current_user

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from myproject import db, app
from myproject.models import User
# from myproject.task.forms import (FixedScheduleForm, OtherWorksForm,
#                                   ReportForm, TestForm, TestPrepareForm,
#                                   PresentationForm, OndemandClassForm)

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




@task_blueprint.route('/addtask')
@login_required
def addtask():

    return  redirect(url_for('auth.login')) if not current_user.is_authenticated \
            else render_template('add_task.html')




@task_blueprint.route('/addtask/fixedschedule')
@login_required
def fixedschedule():

    return  redirect(url_for('auth.login')) if not current_user.is_authenticated \
            else render_template('fixedschedule.html')



@task_blueprint.route('/addtask/otherworks')
@login_required
def otherworks():

    return  redirect(url_for('auth.login')) if not current_user.is_authenticated \
            else render_template('otherworks.html')



@task_blueprint.route('/addtask/report')
@login_required
def report():

    return  redirect(url_for('auth.login')) if not current_user.is_authenticated \
            else render_template('report.html')



@task_blueprint.route('/addtask/test')
@login_required
def test():

    return  redirect(url_for('auth.login')) if not current_user.is_authenticated \
            else render_template('test.html')



@task_blueprint.route('/addtask/testprepare')
@login_required
def testprepare():

    return  redirect(url_for('auth.login')) if not current_user.is_authenticated \
            else render_template('testprepare.html')



@task_blueprint.route('/addtask/presentation')
@login_required
def presentation():

    return  redirect(url_for('auth.login')) if not current_user.is_authenticated \
            else render_template('presentation.html')



@task_blueprint.route('/addtask/ondemandclass')
@login_required
def ondemandclass():

    return  redirect(url_for('auth.login')) if not current_user.is_authenticated \
            else render_template('ondemandclass.html')
