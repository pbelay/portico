# -*- coding: utf-8 -*-
############################
# portico.py
# Metodo para empregar o login de Chuza.gl
# en aplicacións de terceiras partes
#
# Calquera aplicacion requerira consentimento
# por parte da asociacion (chuza.gl@gmail.com)
############################

import requests

# dicionario coa lista de parametros que enviaremos ao servidor
# requests codifica atomaticamente a JSON os parametros
payload = {
    "username": "chuci",  # en desenvolvimento, mellor empregar um usuario de proba
    "password":"Chuza2020",
    "segredo": "marcialdorado"  # isto seria propio para cada aplicacion
}

# facemos login usando o metodo GET, para axilizar
r = requests.get('http://test.chuza.gl/backend/portico.php',
                    params=payload)

# a resposta debe conter a cadea "OK"
# esa cadea pode ser mudada, mais éunha convenci�n de Meneame
assert 'OK' in r.content
