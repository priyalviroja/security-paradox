---
title: "The Paradox of Security Metrics: Measuring What Matters vs. What's Measurable"
category: "reflection"
readTime: "7 min"
---

## The Dashboard Delusion

A CISO proudly shows me their security dashboard. It's beautiful—real-time charts, color-coded indicators, trend lines going in the right direction:

- ✅ 99.2% of systems patched within SLA
- ✅ 10,000 vulnerabilities remediated this quarter
- ✅ 100% of employees completed security training
- ✅ Zero critical findings in last audit
- ✅ Mean time to detect: 4.2 hours

"We're crushing it," they say. "All our metrics are green."

Three months later, they were breached. An attacker spent 6 weeks inside their network, exfiltrated 2TB of customer data, and left undetected.

How did this happen when all the metrics were green?

**Because they were measuring what was easy to measure, not what actually mattered.**

## The Measurement Trap

Security leaders face a fundamental paradox: **the things that matter most are the hardest to measure, and the things that are easiest to measure often matter least**.

### What's Easy to Measure (But Often Doesn't Matter)

- Number of vulnerabilities found
- Percentage of systems patched
- Number of security tools deployed
- Training completion rates
- Compliance audit scores
- Number of policies written
- Security budget as % of IT spend

### What Matters (But Is Hard to Measure)

- Actual security posture
- Resilience to unknown threats
- Cultural security awareness
- Ability to detect novel attacks
- Speed of effective response
- Trust and collaboration
- Strategic risk reduction

**The trap: we optimize for what we measure. And if we measure the wrong things, we optimize for the wrong outcomes.**

## The Vanity Metrics

Let me share some common security metrics that look impressive but tell you almost nothing about actual security:

### 1. "We Patched 10,000 Vulnerabilities This Quarter"

**What it measures:** Activity

**What it doesn't measure:** 
- Were they the *right* vulnerabilities?
- How many new vulnerabilities were introduced?
- How many critical vulnerabilities remain unpatched?
- What's the actual reduction in exploitable risk?

**The problem:** You can patch 10,000 low-risk vulnerabilities and still leave the 10 critical ones unpatched. The metric looks great, but you're no safer.

**Better metric:** "We reduced our exploitable attack surface by 60% by patching the 50 vulnerabilities most likely to be exploited."

### 2. "100% of Employees Completed Security Training"

**What it measures:** Compliance

**What it doesn't measure:**
- Did they actually learn anything?
- Did their behavior change?
- Are they making better security decisions?
- Are phishing click rates decreasing?

**The problem:** People can click through training without absorbing anything. 100% completion doesn't mean 100% effectiveness.

**Better metric:** "Phishing simulation click rates decreased from 18% to 4% after training, and employees reported 47 suspicious emails this month."

### 3. "We Have 47 Security Tools Deployed"

**What it measures:** Investment

**What it doesn't measure:**
- Are they configured correctly?
- Are they actually being used?
- Are they generating actionable insights?
- Are they reducing risk?

**The problem:** More tools ≠ more security. Often, more tools = more complexity, more alert fatigue, more gaps.

**Better metric:** "Our security tools detected and blocked 12 real attacks this month, with zero false positives requiring investigation."

### 4. "Mean Time to Detect: 4.2 Hours"

**What it measures:** Detection speed (for known threats)

**What it doesn't measure:**
- What about unknown threats?
- What percentage of attacks are you actually detecting?
- How long do sophisticated attackers go undetected?

**The problem:** You can have a great MTTD for known threats while completely missing novel attacks. The Equifax breach went undetected for 76 days despite "good" detection metrics.

**Better metric:** "In our last red team exercise, we detected 8 out of 10 attack techniques, with a median detection time of 6 hours."

### 5. "Zero Critical Findings in Our SOC 2 Audit"

**What it measures:** Compliance at a point in time

**What it doesn't measure:**
- Actual security posture
- Resilience to real attacks
- Effectiveness of controls
- Security between audits

**The problem:** Compliance ≠ security. You can pass every audit and still be trivially breachable.

**Better metric:** "We maintain continuous compliance monitoring and can demonstrate control effectiveness in real-time, not just during audits."

## The Goodhart's Law Problem

Goodhart's Law states: **"When a measure becomes a target, it ceases to be a good measure."**

In security, this manifests as:

### Example 1: The Patch Metric

**Metric:** "95% of systems patched within 30 days"

**What happens:**
- Teams focus on hitting 95%, not on patching critical systems
- They patch low-risk systems first (easier)
- Critical systems that are "hard to patch" get delayed
- The metric looks great, but critical vulnerabilities remain

**The gaming:** Exclude critical systems from the metric ("they're special"), or patch non-critical systems to hit the target.

### Example 2: The Vulnerability Metric

**Metric:** "Reduce vulnerability count by 50%"

**What happens:**
- Teams focus on closing vulnerabilities in the scanner
- They mark vulnerabilities as "false positive" or "accepted risk"
- They disable scans on problematic systems
- The metric improves, but actual risk doesn't

**The gaming:** Change the definition, exclude systems, or dispute findings.

### Example 3: The Training Metric

**Metric:** "100% training completion"

**What happens:**
- Training becomes a checkbox exercise
- Content is dumbed down to ensure completion
- People click through without learning
- The metric is perfect, but behavior doesn't change

**The gaming:** Make training easier, shorter, less rigorous.

**The lesson: Any metric that becomes a target will be gamed. The question is whether the gaming improves security or just improves the metric.**

## What Should We Measure?

So if traditional metrics are flawed, what should we measure?

### 1. Outcome Metrics (Not Activity Metrics)

**Don't measure:** Number of vulnerabilities patched

**Do measure:** Reduction in exploitable attack surface

**Don't measure:** Number of security tools deployed

**Do measure:** Percentage of real attacks detected and blocked

**Don't measure:** Training completion rates

**Do measure:** Change in security behavior (phishing click rates, password hygiene, incident reporting)

**Don't measure:** Number of policies written

**Do measure:** Compliance with policies in practice

### 2. Leading Indicators (Not Lagging Indicators)

**Lagging indicators** tell you what already happened (breaches, incidents, audit findings)

**Leading indicators** tell you what's likely to happen (vulnerability trends, threat intelligence, security culture)

**Examples of leading indicators:**
- Time to patch critical vulnerabilities (trending down = good)
- Percentage of systems with EDR deployed (trending up = good)
- Employee security awareness (measured by simulations)
- Security debt accumulation rate
- Attack surface growth rate

### 3. Resilience Metrics (Not Prevention Metrics)

You can't prevent every attack. But you can measure how well you respond:

**Resilience metrics:**
- Time to detect (for various attack types)
- Time to contain (limit blast radius)
- Time to recover (restore operations)
- Percentage of attacks detected by internal controls (vs. external notification)
- Effectiveness of incident response (measured by tabletop exercises)

### 4. Comparative Metrics (Not Absolute Metrics)

Absolute metrics lack context. Comparative metrics provide it:

**Compare to:**
- **Your past self:** Are we getting better or worse?
- **Your peers:** How do we compare to similar organizations?
- **Industry benchmarks:** Are we above or below average?
- **Your goals:** Are we on track to meet our targets?

**Example:** "Our time to detect decreased from 200 days to 20 days (vs. industry average of 50 days)."

### 5. Risk-Based Metrics (Not Compliance-Based Metrics)

**Compliance metrics** tell you if you're following rules

**Risk metrics** tell you if you're actually reducing risk

**Examples:**
- **Compliance:** "We're 100% compliant with PCI DSS"
- **Risk:** "We've reduced the likelihood of payment card data breach from 30% to 5%"

- **Compliance:** "We have MFA deployed"
- **Risk:** "MFA protects 95% of our critical systems and has prevented 47 unauthorized access attempts this quarter"

## The Balanced Scorecard Approach

Instead of relying on a single metric, use a balanced scorecard that measures multiple dimensions:

### 1. Prevention
- Attack surface reduction
- Vulnerability remediation (risk-weighted)
- Security control coverage

### 2. Detection
- Time to detect (by attack type)
- Detection coverage (% of MITRE ATT&CK techniques)
- False positive rate

### 3. Response
- Time to contain
- Time to recover
- Incident response effectiveness

### 4. Culture
- Security awareness (measured by behavior)
- Incident reporting rate
- Security engagement (participation in training, bug bounties, etc.)

### 5. Business Alignment
- Security as a business enabler (not blocker)
- Customer trust metrics
- Competitive differentiation

**No single metric tells the whole story. But together, they provide a more complete picture.**

## The Leader's Role

As a security leader, your job is to **resist the temptation of easy metrics and embrace the complexity of meaningful measurement**.

This means:

### 1. Question Your Metrics

For every metric you track, ask:
- **What behavior does this incentivize?**
- **Can this be gamed? How?**
- **Does improving this metric actually improve security?**
- **What am I *not* measuring that matters more?**

### 2. Measure Outcomes, Not Outputs

**Outputs** are activities (patches deployed, tools purchased, training completed)

**Outcomes** are results (risk reduced, attacks prevented, resilience improved)

Focus on outcomes.

### 3. Embrace Qualitative Measures

Not everything can be quantified. Sometimes the best measure is qualitative:
- "Our security culture has improved—people are asking better questions"
- "Engineering teams are proactively engaging security earlier in the process"
- "We're having more strategic conversations about risk, not just compliance"

These are harder to measure, but they matter.

### 4. Use Metrics to Learn, Not to Judge

Metrics should drive learning and improvement, not punishment.

**Bad use:** "Your team only patched 80% of systems. You failed."

**Good use:** "We're at 80% patching. What's blocking the other 20%? How can we help?"

### 5. Evolve Your Metrics

What you measure should evolve as your security program matures:

**Early stage:** Activity metrics (are we doing the basics?)

**Mid stage:** Effectiveness metrics (are our controls working?)

**Mature stage:** Resilience metrics (how well do we respond to the inevitable?)

Don't get stuck measuring the same things forever.

## The Practice

Here's how to build better security metrics:

### 1. Start with Outcomes

Ask: "What outcome am I trying to achieve?"

Then: "What metric would tell me if I'm achieving it?"

**Example:**
- **Outcome:** Reduce risk of credential compromise
- **Metric:** Percentage of accounts with MFA + number of credential-based attacks prevented

### 2. Test for Gaming

Ask: "How could someone game this metric?"

Then: "Would gaming this metric actually improve security?"

If gaming the metric doesn't improve security, it's a bad metric.

### 3. Combine Leading and Lagging

**Lagging:** Did we get breached? (outcome)

**Leading:** Are we patching critical vulnerabilities quickly? (predictor)

Use both.

### 4. Make Metrics Actionable

Every metric should answer: "What should I do differently?"

If a metric doesn't drive action, it's just noise.

### 5. Review and Revise

Quarterly, ask:
- Are these metrics still relevant?
- Are they driving the right behavior?
- What should we add/remove/change?

Metrics should evolve with your program.

## The Uncomfortable Truth

Here's what most security leaders don't want to hear:

**Your metrics are probably lying to you.**

Not because they're wrong, but because they're measuring the wrong things.

You're measuring:
- What's easy (not what matters)
- What looks good (not what's true)
- What's quantifiable (not what's important)

And as a result, you're optimizing for metrics, not for security.

## The Path Forward

Building meaningful security metrics is hard. It requires:
- Intellectual honesty (admitting when metrics are flawed)
- Courage (measuring things that might look bad)
- Discipline (resisting the temptation of vanity metrics)
- Nuance (accepting that not everything can be quantified)

But it's worth it. Because **what you measure shapes what you optimize for**.

And if you measure the wrong things, you'll optimize for the wrong outcomes.

---

*The best security metrics aren't the ones that look good in dashboards—they're the ones that drive better decisions.*

