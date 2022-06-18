from flask import Flask, request, render_template, redirect, url_for, make_response, jsonify
from DovizKurlari import DovizKurlari
import json
import requests
from flask_sqlalchemy import SQLAlchemy
import http.client


app = Flask(__name__)


conn = http.client.HTTPSConnection("api.collectapi.com")

headers = {
    'content-type': "application/json",
    'authorization': "apikey 0rGgn5ryOkFCA5ZdBdPPi3:0bZMIiPE25gOCSIzeTkkUP"
    }

conn.request("GET", "/economy/hisseSenedi", headers=headers)
res = conn.getresponse()




kurlar = DovizKurlari()
db = SQLAlchemy(app)



@app.route("/web")
def web():

    data = res.read()

 

    return data


@app.route("/getData")
def getData():
    data = jsonify(kurlar.DegerSor())
    data2 = jsonify.dumps(data)
    return render_template("index.html", data2=data2)


@app.route('/api/doviz', methods=['GET', 'POST'])
def api_doviz():
    if request.method == "GET":
        return make_response(jsonify(kurlar.DegerSor()), 200)
    elif request.method == 'POST':
        content = request.json
        tarih = content['tarih']
        if "tur" in content:
            tur = content['tur']
            # 201 = ARSIV
            return make_response(jsonify(kurlar.Arsiv_tarih(tarih).get(tur.upper())), 201)
        else:
            # 201 = ARSIV
            return make_response(jsonify(kurlar.Arsiv_tarih(tarih)), 201)


@app.route('/api/doviz/<tur>', methods=['GET', 'POST'])
def api_her_doviz(tur):
    if request.method == "GET":
        Doviz_Value = kurlar.DegerSor().get(tur.upper())
        if Doviz_Value:
            return make_response(jsonify(Doviz_Value), 200)
        else:
            return make_response(jsonify(Doviz_Value), 404)
    elif request.method == "POST":  # Arsiv
        content = request.json
        tarih = content['tarih']
        Doviz_Value = kurlar.Arsiv_tarih(tarih).get(tur.upper())
        if Doviz_Value:
            return make_response(jsonify(Doviz_Value), 201)
        else:
            return make_response(jsonify(Doviz_Value), 404)


@app.route('/api/doviz/<yil>/<ay>/<gun>', methods=['GET'])
def gun_ay_yil_api(yil, ay, gun):
    if request.method == "GET":
        Doviz_Value = kurlar.Arsiv(gun, ay, yil)
        if Doviz_Value:
            return make_response(jsonify(Doviz_Value), 200)
        else:
            return make_response(jsonify(Doviz_Value), 404)


@app.route('/api/doviz/<yil>/<ay>/<gun>/<tur>', methods=['GET'])
def gun_ay_yil_tur_api(yil, ay, gun, tur):
    if request.method == "GET":
        Doviz_Value = kurlar.Arsiv(gun, ay, yil).get(tur.upper())
        if Doviz_Value:
            return make_response(jsonify(Doviz_Value), 200)
        else:
            return make_response(jsonify(Doviz_Value), 404)


if __name__ == "__main__":
    app.run(debug=True)
