#!/usr/bin/env python3
"""Add journey navigation to all epiphanies"""

# Journey structure with deep connections
journey = [
    {
        "file": "the-mirage-of-control",
        "title": "The Mirage of Control",
        "order": 1,
        "act": "Act I: Awakening",
        "next_context": "But why do we chase this illusion of control so desperately?"
    },
    {
        "file": "the-cost-of-certainty",
        "title": "The Cost of Certainty",
        "order": 2,
        "act": "Act I: Awakening",
        "next_context": "So if certainty is expensive, why do we perform it so loudly?"
    },
    {
        "file": "the-noise-of-compliance",
        "title": "The Noise of Compliance",
        "order": 3,
        "act": "Act I: Awakening",
        "next_context": "If compliance is theater, what should we actually be measuring?"
    },
    {
        "file": "the-paradox-of-visibility",
        "title": "The Paradox of Visibility",
        "order": 4,
        "act": "Act II: Seeing Clearly",
        "next_context": "If metrics shape reality, does speed of action matter more than direction?"
    },
    {
        "file": "speed-is-not-velocity",
        "title": "Speed Is Not Velocity",
        "order": 5,
        "act": "Act II: Seeing Clearly",
        "next_context": "If direction matters, what invisible forces are steering us wrong?"
    },
    {
        "file": "the-invisible-attacker",
        "title": "The Invisible Attacker in the Org Chart",
        "order": 6,
        "act": "Act II: Seeing Clearly",
        "next_context": "If dysfunction is the real threat, how do we communicate this truth?"
    },
    {
        "file": "security-as-storytelling",
        "title": "Security as Storytelling",
        "order": 7,
        "act": "Act III: Reframing",
        "next_context": "If security is narrative, what role does trust play in our story?"
    },
    {
        "file": "trust-as-a-control-surface",
        "title": "Trust as a Control Surface",
        "order": 8,
        "act": "Act III: Reframing",
        "next_context": "If trust is design, how do we redesign our view of humans?"
    },
    {
        "file": "the-human-firewall-myth",
        "title": "The Human Firewall Myth",
        "order": 9,
        "act": "Act III: Reframing",
        "next_context": "If humans are sensors, how do we distinguish signal from noise?"
    },
    {
        "file": "the-security-theater",
        "title": "The Security Theater",
        "order": 10,
        "act": "Act IV: Integration",
        "next_context": "If we reject theater, what do we embrace instead?"
    },
    {
        "file": "resilience-over-perfection",
        "title": "Resilience Over Perfection",
        "order": 11,
        "act": "Act IV: Integration",
        "next_context": None  # Last one
    }
]

import os
import re

src_dir = "src/epiphanies"

# Map act to slug for data attributes
act_slug_map = {
    "Act I: Awakening": "awakening",
    "Act II: Seeing Clearly": "seeing",
    "Act III: Reframing": "reframing",
    "Act IV: Integration": "integration"
}

for i, epiphany in enumerate(journey):
    filepath = os.path.join(src_dir, f"{epiphany['file']}.md")

    if not os.path.exists(filepath):
        print(f"⚠️  File not found: {filepath}")
        continue

    with open(filepath, 'r') as f:
        content = f.read()

    act_slug = act_slug_map.get(epiphany['act'], 'default')

    # Update journey marker if it exists
    if '<div class="journey-marker"' in content:
        # Replace old journey marker with new one that has data attribute
        old_marker_pattern = r'<div class="journey-marker"[^>]*>.*?</div>'
        new_marker = f'<div class="journey-marker" data-act="{act_slug}">\n<span class="journey-label">{epiphany["act"]}</span>\n<span class="journey-position">Epiphany {epiphany["order"]} of 11</span>\n</div>'
        content = re.sub(old_marker_pattern, new_marker, content, flags=re.DOTALL, count=1)

    # Find where the last </div> is (end of principle section)
    last_div_pos = content.rfind('</div>\n</div>')

    if last_div_pos == -1:
        print(f"⚠️  Could not find end marker in {epiphany['file']}")
        continue
    
    # Build navigation HTML
    nav_html = '\n\n<div class="epiphany-navigation">\n'
    
    # Previous link
    if i > 0:
        prev = journey[i-1]
        nav_html += f'''<div class="nav-prev">
<a href="{prev['file']}.html" class="nav-link">
<span class="nav-direction">← Previous</span>
<span class="nav-title">{prev['title']}</span>
</a>
</div>\n'''
    
    # Next link
    if i < len(journey) - 1:
        next_ep = journey[i+1]
        nav_html += f'''<div class="nav-next">
<span class="nav-label">Next in the journey</span>
<a href="{next_ep['file']}.html" class="nav-link">
<span class="nav-title">{next_ep['title']}</span>
<span class="nav-context">{epiphany['next_context']}</span>
</a>
</div>\n'''
    else:
        # Last epiphany - link back to home
        nav_html += f'''<div class="nav-complete">
<span class="nav-label">Journey Complete</span>
<a href="../index.html" class="nav-link-home">
<span class="nav-title">Return to The Security Paradox</span>
<span class="nav-context">Explore reflections and mental models</span>
</a>
</div>\n'''
    
    nav_html += '</div>\n'
    
    # Check if navigation already exists
    if '<div class="epiphany-navigation">' in content:
        # Remove old navigation
        nav_start = content.find('<div class="epiphany-navigation">')
        nav_end = content.find('</div>\n', nav_start) + 6
        content = content[:nav_start] + content[nav_end:]
    
    # Insert new navigation before final newlines
    content = content.rstrip() + nav_html
    
    # Write back
    with open(filepath, 'w') as f:
        f.write(content)
    
    print(f"✅ Updated {epiphany['file']}.md")

print("\n🎉 All epiphanies updated with journey navigation!")

