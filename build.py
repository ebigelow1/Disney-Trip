"""Build index.html from content.md and template.html.

Run:  python3 build.py
Daily weather and flight gates live in data.json, which the page loads on its own,
so a daily update only needs to edit data.json. Rebuild only when content.md changes.
"""
import re
import markdown

content = open("content.md", encoding="utf-8").read()
html = markdown.markdown(content, extensions=["tables", "attr_list", "sane_lists", "md_in_html"])

# checklists: "[ ]" and "[x]" at the start of a list item
html = re.sub(r"<li>\s*(<p>)?\[ \]\s*", lambda m: '<li class="task">' + (m.group(1) or ""), html)
html = re.sub(r"<li>\s*(<p>)?\[x\]\s*", lambda m: '<li class="task done">' + (m.group(1) or ""), html)
# let wide tables scroll on their own instead of the page
html = html.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")

page = open("template.html", encoding="utf-8").read().replace("<!--CONTENT-->", html)
open("index.html", "w", encoding="utf-8").write(page)
print("index.html written,", len(page), "bytes")
