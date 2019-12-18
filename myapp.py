# -*- coding: utf-8 -*-
from flask import Flask, request, url_for, redirect, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/WCF_Carbon_w")
def resultat_WCF_Carbon_w():
    return render_template("WCF_Carbon_w_EFConsTotGHA.html")

@app.route("/WCF_Carbon_TotGHA_fr")
def resultat_WCF_Carbon_EFConsTotGHA():
    return render_template("WCF_Carbon_EFConsTotGHA_fr.html")

@app.route("/WCF_Carbon_PerCap_fr")
def resultat_WCF_Carbon_EFConsPerCap():
    return render_template("WCF_Carbon_EFConsPerCap_fr.html")

@app.route("/WCF_BiocapTotGHA_frvsw")
def resultat_WCF_BiocapTotGHA_frvsw():
    return render_template("WCF_BiocapTotGHA_frvsw.html")

@app.route("/WCF_BiocapPerCap_frvsw")
def WCF_BiocapPerCap_frvsw():
    return render_template("WCF_BiocapPerCap_frvsw.html")

@app.route("/WCF_BiocapTotGHA_fr")
def resultat_WCF_BiocapTotGHA_fr():
    return render_template("WCF_BiocapTotGHA_fr.html")

@app.route("/WCF_EFConsTotGHA_1970_2014")
def WCF_EFConsTotGHA_1970_2014():
    return render_template("WCF_EFConsTotGHA_1970_2014.html")

@app.route("/Top10b")
def Top10b():
    return render_template("Top10_WCF_EFConsTotGHA.html")

@app.route("/Top10h")
def Top10h():
    return render_template("Bad10_WCF_EFConsTotGHA.html")

if __name__ == '__main__':
    app.run(debug=True)

#'/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6' 'myapp.py'    


#<div>
#<p class="resultat"><small><a href="{{url_for('static', filename='Répartition des voix par candidat au premier tour - h.png')}}"> - Nombres de voix par candidat au premier tour - histogramme</a></small></p>
#<p class="resultat"><small><a href="{{url_for('static', filename='Répartition des voix par candidat au deuxième tour - v.png')}}"> - Nombres de voix par candidat au deuxième tour - histogramme</a></small></p>
#<p class="resultat"><small><a href="{{url_for('static', filename='répartition des voix par candidat T1.png')}}"> - Nombres de voix par candidat au premier tour - diagramme circulaire</a></small></p>
#<p class="resultat"><small><a href="{{url_for('static', filename='répartition des voix par candidat T2.png')}}"> - Nombres de voix par candidat au deuxième tour - diagramme circulaire</a></small></p>
#<p class="resultat"><small><a href="{{ url_for('resultat_abstention_T1')}}"> - Résultat de l'abstention au 1er tour</a></small></p>
#<p class="resultat"><small><a href="{{ url_for('resultat_abstention_T2')}}"> - Résultat de l'abstention au 2ème tour</a></small></p>
#<p class="resultat"><small><a href="{{ url_for('resultat_candidat_T1_Sarkozy')}}"> - Répartition des voix pour Sarkozy au 1er tour</a></small></p>
#<p class="resultat"><small><a href="{{ url_for('resultat_candidat_T2_Sarkozy')}}"> - Répartition des voix pour Sarkozy au 2ème tour</a></small></p>
#<p class="resultat"><small><a href="{{ url_for('resultat_repartition_taux_de_pauvrete_fr')}}"> - Résultat de la répartition du taux de pauvreté en France</a></small></p>
#</div>