#!/usr/bin/env python3
import os, markdown, re, shutil

BASE = os.path.dirname(__file__)
SRC = os.path.join(BASE, "src")
DIST = os.path.join(BASE, "dist")

if os.path.exists(DIST):
    shutil.rmtree(DIST)
os.makedirs(DIST, exist_ok=True)

# Copy assets
for fn in ["styles.css", "script.js"]:
    src = os.path.join(SRC, fn)
    if os.path.exists(src):
        shutil.copy(src, DIST)

# Render epiphanies
epip_dir = os.path.join(SRC, "epiphanies")
os.makedirs(os.path.join(DIST, "epiphanies"), exist_ok=True)
for mdfile in os.listdir(epip_dir):
    if not mdfile.endswith(".md"): continue
    text = open(os.path.join(epip_dir, mdfile)).read()
    title = re.search(r'^title:\s*"(.*?)"', text, re.M).group(1)
    body_md = re.sub(r'^---[\s\S]+?---', '', text)
    html = markdown.markdown(body_md)
    page = f"<html><head><title>{title}</title><link rel='stylesheet' href='../styles.css'></head><body><main class='container'><article class='article-wrap'><h1>{title}</h1>{html}</article></main></body></html>"
    open(os.path.join(DIST, "epiphanies", mdfile.replace('.md', '.html')), "w").write(page)

# Create simple index
index_html = "<html><head><title>The Security Paradox</title><link rel='stylesheet' href='styles.css'></head><body><main class='container'><h1>The Security Paradox</h1><p>Security leadership is not the science of control — it's the art of understanding chaos.</p><ul>"
for mdfile in os.listdir(epip_dir):
    if mdfile.endswith('.md'):
        title = re.search(r'^title:\s*"(.*?)"', open(os.path.join(epip_dir, mdfile)).read(), re.M).group(1)
        index_html += f"<li><a href='epiphanies/{mdfile.replace('.md','.html')}'>{title}</a></li>"
index_html += "</ul></main></body></html>"
open(os.path.join(DIST, "index.html"), "w").write(index_html)

print("Generated site in dist/")
