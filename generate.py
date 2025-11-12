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
    <style>
    .about-content {{
        max-width: 800px;
        margin: 0 auto;
        padding: var(--space-xl) var(--space-md);
    }}

    .about-content h2 {{
        font-size: 2rem;
        margin-top: var(--space-xl);
        margin-bottom: var(--space-md);
        color: var(--text-primary);
        font-weight: 600;
    }}

    .about-content h3 {{
        font-size: 1.3rem;
        margin-top: var(--space-lg);
        margin-bottom: var(--space-sm);
        color: var(--accent-primary);
        font-family: var(--font-sans);
        font-weight: 600;
    }}

    .about-content h4 {{
        font-size: 1.1rem;
        margin-bottom: var(--space-xs);
        color: var(--accent-primary);
    }}

    .about-content p {{
        margin-bottom: var(--space-md);
        line-height: 1.8;
        font-size: 1.05rem;
    }}

    .about-content strong {{
        color: var(--text-primary);
        font-weight: 600;
    }}

    .about-content ul {{
        list-style: none;
        padding-left: 0;
        margin-bottom: var(--space-md);
    }}

    .about-content li {{
        padding-left: 1.5rem;
        margin-bottom: var(--space-xs);
        position: relative;
        line-height: 1.7;
    }}

    .about-content li::before {{
        content: '—';
        position: absolute;
        left: 0;
        color: var(--accent-primary);
        font-weight: bold;
    }}
    </style>
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
        <div class="about-content">
            {html}
        </div>
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
                    <p class="journey-intro">A continuous cycle of awakening, seeing, reframing, and integration. Click any epiphany to begin.</p>

                    <div class="journey-circle-container">
                        <svg class="journey-circle" viewBox="0 0 500 500" xmlns="http://www.w3.org/2000/svg">
                            <!-- Center circle background -->
                            <circle cx="250" cy="250" r="80" fill="rgba(26, 29, 36, 0.8)" stroke="rgba(124, 156, 191, 0.3)" stroke-width="2"/>

                            <!-- Center text -->
                            <text x="250" y="240" text-anchor="middle" class="circle-center-title">The Journey</text>
                            <text x="250" y="260" text-anchor="middle" class="circle-center-subtitle">Never Ends</text>

                            <!-- Connecting circle path -->
                            <circle cx="250" cy="250" r="180" fill="none" stroke="rgba(124, 156, 191, 0.2)" stroke-width="2" stroke-dasharray="5,5"/>
"""

# Calculate positions for 11 epiphanies in a circle
import math

# Act colors
act_colors = {
    'awakening': '#d4a574',      # amber
    'seeing': '#7c9cbf',          # blue
    'reframing': '#8fbc8f',       # green
    'integration': '#b8a0c7'      # purple
}

# Act assignments
act_assignments = [
    'awakening', 'awakening', 'awakening',  # 1-3
    'seeing', 'seeing', 'seeing',            # 4-6
    'reframing', 'reframing', 'reframing',  # 7-9
    'integration', 'integration'             # 10-11
]

radius = 180
center_x = 250
center_y = 250

# Start from top (270 degrees = -90 in standard coords)
start_angle = -90

for i, epi in enumerate(epiphanies):
    angle_deg = start_angle + (i * 360 / 11)
    angle_rad = math.radians(angle_deg)

    x = center_x + radius * math.cos(angle_rad)
    y = center_y + radius * math.sin(angle_rad)

    act = act_assignments[i]
    color = act_colors[act]

    # Create clickable group with tooltip
    start_here = ' data-start="true"' if i == 0 else ''
    index_html += f"""
                            <!-- Epiphany {i+1}: {epi['title']} -->
                            <g class="journey-node" data-act="{act}" data-href="epiphanies/{epi['file']}" data-title="{epi['title']}"{start_here}>
                                <title>{epi['title']}</title>
                                <!-- Connecting line to next node -->
"""

    # Calculate next node position for connecting line
    next_i = (i + 1) % 11
    next_angle_deg = start_angle + (next_i * 360 / 11)
    next_angle_rad = math.radians(next_angle_deg)
    next_x = center_x + radius * math.cos(next_angle_rad)
    next_y = center_y + radius * math.sin(next_angle_rad)

    index_html += f"""                                <line x1="{x}" y1="{y}" x2="{next_x}" y2="{next_y}"
                                      stroke="{color}" stroke-width="2" opacity="0.3" class="node-connector"/>

                                <!-- Node circle -->
                                <circle cx="{x}" cy="{y}" r="20" fill="rgba(26, 29, 36, 0.9)"
                                        stroke="{color}" stroke-width="3" class="node-circle"/>

                                <!-- Node number -->
                                <text x="{x}" y="{y + 5}" text-anchor="middle" class="node-number">{i+1}</text>

                                <!-- Node label (positioned outside) -->
"""

    # Position label outside the circle
    label_radius = 220
    label_x = center_x + label_radius * math.cos(angle_rad)
    label_y = center_y + label_radius * math.sin(angle_rad)

    # Determine text anchor based on position
    if x < center_x - 50:
        anchor = "end"
    elif x > center_x + 50:
        anchor = "start"
    else:
        anchor = "middle"

    # Shorten title if too long
    title = epi['title']
    if len(title) > 25:
        title = title[:22] + "..."

    index_html += f"""                                <text x="{label_x}" y="{label_y}" text-anchor="{anchor}" class="node-label">{title}</text>
                            </g>
"""

index_html += """                        </svg>
                    </div>

                    <div class="journey-legend">
                        <div class="legend-item" data-act="awakening">
                            <span class="legend-dot"></span>
                            <span class="legend-text">Act I: Awakening</span>
                        </div>
                        <div class="legend-item" data-act="seeing">
                            <span class="legend-dot"></span>
                            <span class="legend-text">Act II: Seeing Clearly</span>
                        </div>
                        <div class="legend-item" data-act="reframing">
                            <span class="legend-dot"></span>
                            <span class="legend-text">Act III: Reframing</span>
                        </div>
                        <div class="legend-item" data-act="integration">
                            <span class="legend-dot"></span>
                            <span class="legend-text">Act IV: Integration</span>
                        </div>
                    </div>

                    <!-- Toggle for list view -->
                    <div class="view-toggle-container">
                        <button class="view-toggle-btn" id="toggleListView">
                            <span class="toggle-icon">📋</span>
                            <span class="toggle-text">Show List View</span>
                        </button>
                    </div>

                    <!-- Collapsible list view -->
                    <div class="journey-list-view" id="journeyListView" style="display: none;">
"""

# Add the list view with all epiphanies grouped by act
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

# Add ALL reflections (not just 3)
for item in reflections:
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
                        <a href="mental-models/trust-boundaries.html" class="content-item model-item">
                            <div class="model-icon-small">🔐</div>
                            <div class="model-content">
                                <h4 class="content-item-title">Trust Boundaries</h4>
                                <p class="model-description">Explore zero-trust architecture and verification zones</p>
                            </div>
                        </a>
                        <a href="mental-models/incident-response-timeline.html" class="content-item model-item">
                            <div class="model-icon-small">⏱️</div>
                            <div class="model-content">
                                <h4 class="content-item-title">Incident Response Timeline</h4>
                                <p class="model-description">See how time compounds the cost of breaches</p>
                            </div>
                        </a>
                        <a href="mental-models/security-debt-compound.html" class="content-item model-item">
                            <div class="model-icon-small">📈</div>
                            <div class="model-content">
                                <h4 class="content-item-title">Security Debt Compounding</h4>
                                <p class="model-description">Watch security debt grow exponentially over time</p>
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
