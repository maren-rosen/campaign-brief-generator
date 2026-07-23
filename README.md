# Campaign Brief Generator

A Python tool that uses the Claude API to generate complete, structured campaign briefs from five strategic inputs: product, audience, objective, budget, and brand voice.

Built by [Maren Rosen](https://www.linkedin.com/in/marenrosen) — marketing and commercial growth executive who has routed hundreds of briefs through creative teams at Tides Medical, Stuller, and agency engagements.

## Why I built this

The brief is where campaigns are won or lost, and writing a good one takes hours. I wanted to test whether AI could produce a routable first draft in minutes, and where executive judgment still has to intervene.

## What it does

Takes five inputs and returns a complete brief: campaign objective, audience insight, key message hierarchy, channel plan with budget allocation, three creative concept directions with working headlines, success metrics, and a phased timeline.

## The design decision that matters

Early runs confidently invented performance benchmarks (impression counts, ROI figures) that had no basis in reality. So the prompt now explicitly forbids fabricated metrics: the tool defines what to measure and marks every benchmark as [TO VALIDATE] for the strategist to fill in with real data. AI drafts the structure; the operator owns the numbers. Knowing where these tools fail is as important as knowing what they can do.

## How to run it

1. Get an Anthropic API key at console.anthropic.com
2. Open the script in Google Colab and add your API key where marked
3. Edit the five campaign input lines for your use case
4. Run. A complete brief prints in under a minute.

## Tools used

- Python
- Anthropic Claude API (claude-sonnet-4-6)
- Google Colab

## Related

- [voice-of-customer-ai-analyzer](https://github.com/maren-rosen/voice-of-customer-ai-analyzer): turns customer review data into sentiment findings and marketing recommendations
