---
title: "Trust as a Control Surface"
category: "epiphany"
readTime: "3 min"
order: 8
prev: "security-as-storytelling"
next: "the-human-firewall-myth"
nextContext: "If trust is design, how do we redesign our view of humans?"
---

<div class="journey-marker" data-act="reframing">
<span class="journey-label">Act III: Reframing</span>
<span class="journey-position">Epiphany 8 of 11</span>
</div>

<div class="epiphany-section">
<span class="epiphany-label">The Story</span>

A company implemented zero-trust. They spent 18 months removing all implicit trust, verifying everything, segmenting every network, requiring MFA for every action.

Then they looked at their packet captures and access logs.

**67% of their traffic was going through unapproved VPNs and shadow IT tools.**

Engineers couldn't collaborate. Teams couldn't ship. Every action required three approvals. The secure system was so locked down, people started finding workarounds—shared credentials, personal Dropbox accounts, unapproved Slack workspaces.

The zero-trust architecture created a high-trust culture problem. They'd eliminated technical trust and replaced it with organizational distrust. And distrust is hydraulic—it finds the path of least resistance.

Productivity collapsed. Security posture degraded. The CISO was fired.

Another company took a different approach:

"We trust our engineers. But we verify. We give broad access, but we monitor. We enable autonomy, but we detect anomalies. We make the secure path the easy path, not the only path."

Their security posture improved. Their productivity increased. Their shadow IT dropped to 8%.

What was different?

**Trust wasn't eliminated—it was managed.**

They didn't ask "How do we remove all trust?" They asked "Where should we place trust boundaries, and how do we make them visible?"

**The pattern: Trust is not the opposite of security. Trust is a control surface.**
</div>

<div class="section-divider"></div>

<div class="epiphany-section">
<span class="epiphany-label">The Reflection</span>

Every system has trust boundaries—places where you decide to trust without verifying. The question isn't whether to trust, but *where* to place those boundaries and *how* to manage them.

Zero-trust architecture is a misnomer. It's not "zero trust"—it's "explicitly managed trust." You're not eliminating trust; you're making it visible, measurable, and revocable.

But here's the paradox that keeps me up at night: **The more you try to eliminate trust, the more trust you need.**

Let me explain:

When you implement zero-trust, you're saying: "We don't trust the network. We don't trust the device. We don't trust the user."

But you're implicitly saying: "We trust the identity provider. We trust the MFA system. We trust the policy engine. We trust the monitoring system. We trust the security team to configure all of this correctly."

You haven't eliminated trust. You've just moved it. And often, you've concentrated it in places that are harder to verify.

I've seen this pattern repeat:
1. **Eliminate trust in the network** → Trust the identity provider
2. **Eliminate trust in users** → Trust the policy engine
3. **Eliminate trust in devices** → Trust the MDM system
4. **Eliminate trust in applications** → Trust the service mesh

At each step, you're trading distributed trust (which is hard to manage) for concentrated trust (which is a single point of failure).

And here's what haunts me: **What if trust is hydraulic?**

What if trust is like water—you can't eliminate it, you can only redirect it? What if every attempt to remove trust from one part of the system just pushes it to another part?

The best security systems don't eliminate trust—they make trust hydraulic. They push trust to the edges where it's needed (empowering people) and pull it back from the center where it's risky (protecting critical systems).

This requires:
- **Clarity** about what you trust and why (make trust boundaries explicit)
- **Mechanisms** to verify that trust is warranted (continuous authentication, behavioral monitoring)
- **Ability** to revoke trust when it's violated (automated response, graceful degradation)
- **Culture** that sees trust as a tool, not a weakness (trust is a control, not a vulnerability)

But here's the uncomfortable question: **Can you build a security system that people actually want to use?**

Because if your security system requires people to fight it, they will. And they'll win. Shadow IT, shared credentials, workarounds—these aren't security failures, they're design failures.

The system that's too secure to use is not secure at all.

Trust is not a binary. It's a dial. And the best security leaders know how to tune it—high enough to enable productivity, low enough to detect anomalies, flexible enough to adapt to context.

What would it take to make trust your strongest control instead of your biggest vulnerability?
</div>

<div class="section-divider"></div>

<div class="epiphany-section">
<span class="epiphany-label">The Principle</span>

<div class="principle-takeaway">
"Trust is not the opposite of security—it's a control surface. Trust is hydraulic: you can't eliminate it, only redirect it. Make trust explicit, measurable, and revocable. The goal is not zero trust, but managed trust that enables productivity while detecting anomalies."
</div>
</div>


<div class="nav-next">
<span class="nav-label">Next in the journey</span>
<a href="the-human-firewall-myth.html" class="nav-link">
<span class="nav-title">The Human Firewall Myth</span>
<span class="nav-context">If trust is design, how do we redesign our view of humans?</span>
</a>
</div>
</div>

<div class="epiphany-navigation">
<div class="nav-prev">
<a href="security-as-storytelling.html" class="nav-link">
<span class="nav-direction">← Previous</span>
<span class="nav-title">Security as Storytelling</span>
</a>
</div>
<div class="nav-next">
<span class="nav-label">Next in the journey</span>
<a href="the-human-firewall-myth.html" class="nav-link">
<span class="nav-title">The Human Firewall Myth</span>
<span class="nav-context">If trust is design, how do we redesign our view of humans?</span>
</a>
</div>
</div>
