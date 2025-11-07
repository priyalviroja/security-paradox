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

# Copy mental models (HTML files)
mental_models_src = os.path.join(SRC, "mental-models")
mental_models_dist = os.path.join(DIST, "mental-models")
if os.path.exists(mental_models_src):
    shutil.copytree(mental_models_src, mental_models_dist)

def render_markdown_section(section_name, output_dir):
    """Render markdown files from a section directory"""
    section_dir = os.path.join(SRC, section_name)
    if not os.path.exists(section_dir):
        return []

    os.makedirs(output_dir, exist_ok=True)
    items = []

    for mdfile in os.listdir(section_dir):
        if not mdfile.endswith(".md"):
            continue

        text = open(os.path.join(section_dir, mdfile), encoding='utf-8').read()
        title_match = re.search(r'^title:\s*"(.*?)"', text, re.M)
        if not title_match:
            continue

        title = title_match.group(1)
        read_time_match = re.search(r'^readTime:\s*"(.*?)"', text, re.M)
        read_time = read_time_match.group(1) if read_time_match else ""

        # Extract order for epiphanies
        order_match = re.search(r'^order:\s*(\d+)', text, re.M)
        order = int(order_match.group(1)) if order_match else 999

        body_md = re.sub(r'^---[\s\S]+?---\n*', '', text)
        html = markdown.markdown(body_md)

        # Enhanced page template with navigation
        page = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - The Security Paradox</title>
    <link rel="stylesheet" href="../styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Crimson+Text:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
</head>
<body>
    <nav>
        <div class="nav-container">
            <a href="../index.html" class="nav-logo">The Security Paradox</a>
            <ul class="nav-links">
                <li><a href="../index.html#epiphanies">Epiphanies</a></li>
                <li><a href="../index.html#reflections">Reflections</a></li>
                <li><a href="../index.html#mental-models">Mental Models</a></li>
                <li><a href="../about.html">About</a></li>
            </ul>
        </div>
    </nav>
    <main class="container">
        <article class="article-wrap">
            <div class="article-header">
                <div class="article-meta">{section_name.upper()}{' • ' + read_time if read_time else ''}</div>
                <h1>{title}</h1>
            </div>
            {html}
        </article>
    </main>
    <script src="../script.js"></script>
</body>
</html>"""

        output_file = os.path.join(output_dir, mdfile.replace('.md', '.html'))
        open(output_file, "w", encoding='utf-8').write(page)
        items.append({'title': title, 'file': mdfile.replace('.md', '.html'), 'readTime': read_time, 'order': order})

    # Sort by order (for epiphanies journey)
    items.sort(key=lambda x: x['order'])

    return items

# Render all sections
epiphanies = render_markdown_section("epiphanies", os.path.join(DIST, "epiphanies"))
reflections = render_markdown_section("reflections", os.path.join(DIST, "reflections"))
audio = render_markdown_section("audio", os.path.join(DIST, "audio"))

# Render about page
about_src = os.path.join(SRC, "about.md")
if os.path.exists(about_src):
    text = open(about_src, encoding='utf-8').read()
    title_match = re.search(r'^title:\s*"(.*?)"', text, re.M)
    title = title_match.group(1) if title_match else "About"
    body_md = re.sub(r'^---[\s\S]+?---\n*', '', text)
    html = markdown.markdown(body_md)

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - The Security Paradox</title>
    <link rel="stylesheet" href="styles.css">
    <link href="https://fonts.googleapis.com/css2?family=Crimson+Text:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
</head>
<body>
    <nav>
        <div class="nav-container">
            <a href="index.html" class="nav-logo">The Security Paradox</a>
            <ul class="nav-links">
                <li><a href="index.html#epiphanies">Epiphanies</a></li>
                <li><a href="index.html#reflections">Reflections</a></li>
                <li><a href="index.html#mental-models">Mental Models</a></li>
                <li><a href="about.html">About</a></li>
            </ul>
        </div>
    </nav>
    <main class="container">
        {html}
    </main>
    <script src="script.js"></script>
</body>
</html>"""

    open(os.path.join(DIST, "about.html"), "w", encoding='utf-8').write(page)

# Create enhanced home page with doorways
index_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Security Paradox</title>
    <meta name="description" content="Security leadership is not the science of control — it's the art of understanding chaos.">
    <link rel="stylesheet" href="styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Crimson+Text:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
</head>
<body>
    <nav>
        <div class="nav-container">
            <a href="index.html" class="nav-logo">The Security Paradox</a>
            <ul class="nav-links">
                <li><a href="#epiphanies">Epiphanies</a></li>
                <li><a href="#reflections">Reflections</a></li>
                <li><a href="#mental-models">Mental Models</a></li>
                <li><a href="about.html">About</a></li>
            </ul>
        </div>
    </nav>

    <section class="hero">
        <div class="hero-content">
            <h1 class="hero-title">The Security Paradox</h1>
            <div class="hero-subtitle">
                <p class="hero-tagline">Security leadership is not the <strong>science of control</strong> — it's the <strong>art of understanding chaos</strong>.</p>
                <p class="hero-audience">For CISOs and security leaders who know that the hardest problems aren't <strong>technical</strong>—they're <strong>human, organizational, cultural</strong>.</p>
            </div>
        </div>
    </section>

    <section class="doorways-section">
        <div class="container">
            <h2 class="section-title">Three Doorways</h2>
            <div class="doorways-grid">

                <button class="doorway doorway-toggle active" data-target="epiphanies-column">
                    <div class="doorway-icon">💡</div>
                    <h3 class="doorway-title">Epiphanies</h3>
                    <p class="doorway-description">
                        Short, 3-minute ideas that challenge assumptions about security, control, and leadership.
                    </p>
                    <span class="doorway-count">11 insights</span>
                    <span class="doorway-indicator">−</span>
                </button>

                <button class="doorway doorway-toggle active" data-target="reflections-column">
                    <div class="doorway-icon">📖</div>
                    <h3 class="doorway-title">Reflections</h3>
                    <p class="doorway-description">
                        Longer essays exploring the paradoxes of security leadership and organizational resilience.
                    </p>
                    <span class="doorway-count">3 essays</span>
                    <span class="doorway-indicator">−</span>
                </button>

                <button class="doorway doorway-toggle active" data-target="models-column">
                    <div class="doorway-icon">🧠</div>
                    <h3 class="doorway-title">Mental Models</h3>
                    <p class="doorway-description">
                        Interactive visualizations of abstract security truths—complexity, defense, and trust.
                    </p>
                    <span class="doorway-count">Explore</span>
                    <span class="doorway-indicator">−</span>
                </button>

            </div>
        </div>
    </section>

    <section class="content-section">
        <div class="container">
            <div class="content-grid">

                <!-- Column 1: The Journey of Epiphanies -->
                <div class="content-column" id="epiphanies-column">
                    <h3 class="content-heading">The Journey of Epiphanies</h3>
                    <p class="journey-intro">11 insights that build upon each other, taking you from awakening to integration.</p>

                    <div class="journey-start">
                        <a href="epiphanies/{0}" class="journey-begin-btn">
                            <span class="btn-label">Begin the Journey</span>
                            <span class="btn-subtitle">{1}</span>
                        </a>
                    </div>

                    <div class="journey-preview">
""".format(epiphanies[0]['file'], epiphanies[0]['title'])

# Group epiphanies by act
acts = [
    ("Act I: Awakening", "awakening", epiphanies[0:3]),
    ("Act II: Seeing Clearly", "seeing", epiphanies[3:6]),
    ("Act III: Reframing", "reframing", epiphanies[6:9]),
    ("Act IV: Integration", "integration", epiphanies[9:11])
]

for act_name, act_slug, act_items in acts:
    index_html += f"""                        <div class="act-group" data-act="{act_slug}">
                            <h4 class="act-title">{act_name}</h4>
"""
    for item in act_items:
        index_html += f"""                            <a href="epiphanies/{item['file']}" class="journey-item">
                                <span class="journey-number">{item['order']}</span>
                                <span class="journey-title">{item['title']}</span>
                            </a>
"""
    index_html += """                        </div>
"""

index_html += """                    </div>
                </div>

                <!-- Column 2: Recent Reflections -->
                <div class="content-column" id="reflections-column">
                    <h3 class="content-heading">Recent Reflections</h3>
                    <p class="column-intro">Longer essays exploring security leadership, culture, and transformation.</p>
                    <div class="content-list">
"""

# Add reflections
for item in reflections[:3]:
    index_html += f"""                        <a href="reflections/{item['file']}" class="content-item">
                            <h4 class="content-item-title">{item['title']}</h4>
                            <span class="read-time">{item['readTime']}</span>
                        </a>
"""

index_html += """                    </div>
                </div>

                <!-- Column 3: Mental Models -->
                <div class="content-column" id="models-column">
                    <h3 class="content-heading">Mental Models</h3>
                    <p class="column-intro">Interactive visualizations of abstract security truths.</p>
                    <div class="content-list">
                        <a href="mental-models/attack-surface.html" class="content-item model-item">
                            <div class="model-icon-small">🎯</div>
                            <div class="model-content">
                                <h4 class="content-item-title">Attack Surface</h4>
                                <p class="model-description">Watch complexity compound with every feature</p>
                            </div>
                        </a>
                        <a href="mental-models/defense-in-depth.html" class="content-item model-item">
                            <div class="model-icon-small">🛡️</div>
                            <div class="model-content">
                                <h4 class="content-item-title">Defense in Depth</h4>
                                <p class="model-description">Visualize how layered security contains failure</p>
                            </div>
                        </a>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <section class="audio-section">
        <div class="container">
            <h3 class="content-heading">Audio Fireflies</h3>
            <p class="section-description">
                Micro reflections for leaders on the move—2-3 minute contemplative pieces for moments between meetings.
            </p>
            <a href="audio/index.html" class="cta-link">Explore Audio →</a>
        </div>
    </section>

    <footer class="footer">
        <div class="container">
            <p>Built with care for security leaders who think deeply.</p>
            <p><a href="about.html">About & Support</a></p>
        </div>
    </footer>

    <script src="script.js"></script>
</body>
</html>"""

open(os.path.join(DIST, "index.html"), "w", encoding='utf-8').write(index_html)

print(f"✨ Generated site in dist/")
print(f"   📝 {len(epiphanies)} epiphanies")
print(f"   📖 {len(reflections)} reflections")
print(f"   🧠 Mental models")
print(f"   🎧 Audio section")
print(f"   ℹ️  About page")
