from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    model_id = 'en-fr'
    textToTranslate = language_translator.translate(text = textToTranslate,
    model_id=model_id).get_result()
    return textToTranslate.get("translations")[0].get("translation")

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    model_id = 'fr-en'
    textToTranslate = language_translator.translate(text = textToTranslate,
    model_id=model_id).get_result()
    return textToTranslate.get("translations")[0].get("translation")

@app.route("/")
def renderIndexPage():
    return render_template("index.html")
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
