"""template.html + summary.html + cards.json -> index.html"""
import json, pathlib, sys
d = pathlib.Path(__file__).parent
cards = json.loads((d / "cards.json").read_text())
photos = json.loads((d / "photos.json").read_text())
html = (d / "template.html").read_text()
html = html.replace("<!--SUMMARY-->", (d / "summary.html").read_text())
html = html.replace("/*CARDS*/[]", json.dumps(cards, ensure_ascii=False).replace("</", "<\\/"))
html = html.replace("/*PHOTOS*/[]", json.dumps(photos, ensure_ascii=False))
(d / "index.html").write_text(html)
print("index.html", len(cards), "cards")
