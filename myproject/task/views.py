from flask import (Blueprint, render_template, redirect, url_for, abort)
from flask_login import login_required, current_user

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from myproject import db, app
from myproject.models import User, Task
from myproject.task.forms import (FixedScheduleForm, OtherWorksForm,
                                  ReportForm, TestForm, TestPrepareForm,
                                  PresentationForm, OndemandClassForm)

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



@task_blueprint.route('/addtask/fixedschedule', methods=['GET', 'POST'])
@login_required
def fixedschedule():

    form = FixedScheduleForm()

    if form.validate():

        task = Task(taskname=form.taskname.data,
                    date=str(form.date.data),
                    startat=str(form.startat.data),
                    endat=str(form.endat.data))

        db.session.add(task)
        db.session.commit()

        # 送ったらタスク一覧へリダイレクト
        return redirect(url_for('task.alltasks'))


    return  redirect(url_for('auth.login')) if not current_user.is_authenticated \
            else render_template('fixedschedule.html', form=form)



@task_blueprint.route('/addtask/otherworks', methods=['GET', 'POST'])
@login_required
def otherworks():

    form = OtherWorksForm()

    return  redirect(url_for('auth.login')) if not current_user.is_authenticated \
            else render_template('otherworks.html', form=form)



@task_blueprint.route('/addtask/report', methods=['GET', 'POST'])
@login_required
def report():

    form = ReportForm()

    return  redirect(url_for('auth.login')) if not current_user.is_authenticated \
            else render_template('report.html', form=form)



@task_blueprint.route('/addtask/test', methods=['GET', 'POST'])
@login_required
def test():

    form = TestForm()

    return  redirect(url_for('auth.login')) if not current_user.is_authenticated \
            else render_template('test.html', form=form)



@task_blueprint.route('/addtask/testprepare', methods=['GET', 'POST'])
@login_required
def testprepare():

    form = TestPrepareForm()

    return  redirect(url_for('auth.login')) if not current_user.is_authenticated \
            else render_template('testprepare.html', form=form)



@task_blueprint.route('/addtask/presentation', methods=['GET', 'POST'])
@login_required
def presentation():

    form = PresentationForm()

    return  redirect(url_for('auth.login')) if not current_user.is_authenticated \
            else render_template('presentation.html', form=form)



@task_blueprint.route('/addtask/ondemandclass', methods=['GET', 'POST'])
@login_required
def ondemandclass():

    form = OndemandClassForm()

    return  redirect(url_for('auth.login')) if not current_user.is_authenticated \
            else render_template('ondemandclass.html', form=form)
