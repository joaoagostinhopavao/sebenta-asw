"""Versão inglesa das figuras sem duplicar os scripts.

Cada script chama ativar(__file__) antes de ler sys.argv. Opções:
  --en      troca cada texto da figura pela tradução em en/<script>.json (um texto sem tradução fica igual)
  --listar  grava em en/<script>.json todos os textos da figura que ainda não estão lá (tradução vazia)

As traduções ficam em assets/scripts/en/, um JSON por script: {"texto em português": "English text"}.
"""
import json
import os
import sys

import matplotlib.text


def _caminho(script):
    pasta = os.path.join(os.path.dirname(os.path.abspath(script)), "en")
    return os.path.join(pasta, os.path.splitext(os.path.basename(script))[0] + ".json")


def ativar(script):
    caminho = _caminho(script)
    original = matplotlib.text.Text.set_text

    if "--en" in sys.argv:
        sys.argv.remove("--en")
        with open(caminho, encoding="utf-8") as f:
            tabela = json.load(f)

        def set_text(self, s):
            if isinstance(s, str) and tabela.get(s):
                s = tabela[s]
            return original(self, s)

        matplotlib.text.Text.set_text = set_text

    elif "--listar" in sys.argv:
        sys.argv.remove("--listar")
        tabela = {}
        if os.path.exists(caminho):
            with open(caminho, encoding="utf-8") as f:
                tabela = json.load(f)

        def set_text(self, s):
            if isinstance(s, str) and s.strip() and s not in tabela:
                tabela[s] = ""
            return original(self, s)

        matplotlib.text.Text.set_text = set_text

        def gravar():
            os.makedirs(os.path.dirname(caminho), exist_ok=True)
            with open(caminho, "w", encoding="utf-8") as f:
                json.dump(tabela, f, ensure_ascii=False, indent=1)

        import atexit
        atexit.register(gravar)
