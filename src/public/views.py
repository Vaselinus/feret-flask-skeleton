"""
Logic for dashboard related routes
"""
from flask import Blueprint, render_template,url_for,request,redirect
from .forms import LogUserForm, CukrovinkyForm
from ..data.database import db
from ..data.models import LogUser, CukrovinkyDB
blueprint = Blueprint('public', __name__)

@blueprint.route('/', methods=['GET'])
def index():
    return render_template('public/index.tmpl')

@blueprint.route('/loguserinput',methods=['GET', 'POST'])
def InsertLogUser():
    form = LogUserForm()
    if form.validate_on_submit():
        LogUser.create(**form.data)
    return render_template("public/LogUser.tmpl", form=form)

@blueprint.route('/loguserlist',methods=['GET'])
def ListuserLog():
    pole = db.session.query(LogUser).all()
    return render_template("public/listuser.tmpl",data = pole)

@blueprint.route('/cukrovinky', methods=['GET', 'POST'])
def cukrovinky():
    form = CukrovinkyForm()
    if form.validate_on_submit():
        CukrovinkyDB.create(**form.data)
    return render_template("public/cukrovinky.tmpl", form=form)

@blueprint.route('/vypis_cukrovinky', methods=['GET'])
def vypis_cukrovinky():
    pole = db.session.query(CukrovinkyDB).all()
    return render_template("public/vypisCukrovinky.tmpl", data=pole)

@blueprint.route('/smazat_cukrovinky/<int:id>', methods=['GET'])
def smazat_cukrovinky(id):
    pole = db.session.query(CukrovinkyDB).filter_by(id = id).first()
    db.session.delete(pole)
    db.session.commit()
    return redirect(request.args.get("next")or url_for("public.vypis_cukrovinky"))