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

    data =  Task.query.filter_by(classification=1).first()

    return  redirect(url_for('auth.login')) if not current_user.is_authenticated else render_template('all_tasks.html', data=data)



@task_blueprint.route('/addtask')
@login_required
def addtask():

    return  redirect(url_for('auth.login')) if not current_user.is_authenticated \
            else render_template('add_task.html')



@task_blueprint.route('/addtask/fixedschedule', methods=['GET', 'POST'])
@login_required
def fixedschedule():

    form = FixedScheduleForm()

    if form.validate_on_submit():

        task = Task(classification=1,
                    taskname=form.taskname.data,
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

    if form.validate_on_submit():

        task = Task(classification=2,
                    taskname=form.taskname.data,
                    date=str(form.date.data),
                    due=str(form.due.data),
                    taskweight=int(form.taskweight.data))

        db.session.add(task)
        db.session.commit()

        # 送ったらタスク一覧へリダイレクト
        return redirect(url_for('task.alltasks'))


    return  redirect(url_for('auth.login')) if not current_user.is_authenticated \
            else render_template('otherworks.html', form=form)



@task_blueprint.route('/addtask/report', methods=['GET', 'POST'])
@login_required
def report():

    form = ReportForm()

    if form.validate_on_submit():

        task = Task(classification=3,
                    taskname=form.taskname.data,
                    date=str(form.date.data),
                    due=str(form.due.data),
                    taskweight=int(form.taskweight.data),
                    lang=form.lang.data,
                    words=form.words.data)

        db.session.add(task)
        db.session.commit()

        # 送ったらタスク一覧へリダイレクト
        return redirect(url_for('task.alltasks'))

    return  redirect(url_for('auth.login')) if not current_user.is_authenticated \
            else render_template('report.html', form=form)



@task_blueprint.route('/addtask/test', methods=['GET', 'POST'])
@login_required
def test():

    form = TestForm()

    if form.validate_on_submit():

        task = Task(classification=4,
                    taskname=form.taskname.data,
                    date=str(form.date.data),
                    due=str(form.due.data),
                    taskweight=int(form.test_weight.data),
                    anylength=form.test_time.data)

        db.session.add(task)
        db.session.commit()

        # 送ったらタスク一覧へリダイレクト
        return redirect(url_for('task.alltasks'))

    return  redirect(url_for('auth.login')) if not current_user.is_authenticated \
            else render_template('test.html', form=form)



@task_blueprint.route('/addtask/testprepare', methods=['GET', 'POST'])
@login_required
def testprepare():

    form = TestPrepareForm()

    form = TestForm()

    if form.validate_on_submit():

        task = Task(classification=5,
                    taskname=form.taskname.data,
                    date=str(form.date.data),
                    due=str(form.due.data),
                    taskweight=int(form.test_weight.data))

        db.session.add(task)
        db.session.commit()

        # 送ったらタスク一覧へリダイレクト
        return redirect(url_for('task.alltasks'))

    return  redirect(url_for('auth.login')) if not current_user.is_authenticated \
            else render_template('testprepare.html', form=form)



@task_blueprint.route('/addtask/presentation', methods=['GET', 'POST'])
@login_required
def presentation():

    form = PresentationForm()

    if form.validate_on_submit():

        # classification

        task = Task(classification=6,
                    taskname=form.taskname.data,
                    date=str(form.date.data),
                    due=str(form.due.data),
                    anylength=form.presentation_time.data,
                    page_num=form.page_num.data)

        db.session.add(task)
        db.session.commit()

        # 送ったらタスク一覧へリダイレクト
        return redirect(url_for('task.alltasks'))


    return  redirect(url_for('auth.login')) if not current_user.is_authenticated \
            else render_template('presentation.html', form=form)



@task_blueprint.route('/addtask/ondemandclass', methods=['GET', 'POST'])
@login_required
def ondemandclass():

    form = OndemandClassForm()

    if form.validate_on_submit():

        task = Task(classification=7,
                    taskname=form.taskname.data,
                    date=str(form.date.data),
                    due=str(form.due.data),
                    anylength=form.class_length.data)

        db.session.add(task)
        db.session.commit()

        # 送ったらタスク一覧へリダイレクト
        return redirect(url_for('task.alltasks'))

    return  redirect(url_for('auth.login')) if not current_user.is_authenticated \
            else render_template('ondemandclass.html', form=form)
