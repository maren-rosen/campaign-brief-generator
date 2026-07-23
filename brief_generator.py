import anthropic

# ---- SETTINGS ----
API_KEY = "PUT-KEY-HERE"

# ---- CAMPAIGN INPUTS: edit these for any campaign ----
PRODUCT = "A boutique short-term rental house in a mountain-adjacent city, design-forward renovation"
AUDIENCE = "Traveling families and small friend groups visiting for ski trips, concerts, and long weekends"
OBJECTIVE = "Drive first 20 bookings and 10+ five-star reviews within 90 days of listing launch"
BUDGET = "$1,500"
BRAND_VOICE = "Warm, design-forward, local-insider"

# ---- BUILD THE BRIEF ----
client = anthropic.Anthropic(api_key=API_KEY)

prompt = f"""You are a senior marketing strategist writing a creative brief.
Write a complete campaign brief using these inputs:

Product: {PRODUCT}
Target audience: {AUDIENCE}
Objective: {OBJECTIVE}
Budget: {BUDGET}
Brand voice: {BRAND_VOICE}

Structure the brief with these sections:
1. Campaign objective (one sharp sentence)
2. Audience insight (what this audience actually cares about)
3. Key message (one sentence) plus three supporting messages
4. Channel plan with budget allocation across channels
5. Three creative concept directions, each with a working headline
6. Success metrics tied to the objective
7. Timeline with 3 phases

Keep it tight and actionable, the way a brief routed to a real creative team would read.
For success metrics, do not invent specific impression, reach, or ROI numbers. Define what should be measured and how, and mark any benchmark as [TO VALIDATE] for the strategist to fill in."""

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=3000,
    messages=[{"role": "user", "content": prompt}],
)

print(response.content[0].text)
