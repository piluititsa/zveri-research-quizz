# What data beast are you? 🦊

A mini-quiz on customer-experience & AI statistics. Answer 4 questions, trust your gut on the numbers — and get your archetype beast: ostrich, meerkat, beaver, fox or eagle.

🔗 **Live version:** https://piluititsa.github.io/zveri-research-quizz/

🌍 **Languages:** English, Russian, Spanish, French, German (in-page switcher).

## What's inside

- **A single self-contained HTML page** — no frameworks or bundlers, works offline.
- **A breakdown after every answer**, with the source (Goodman/TARP, BCG, PwC, Pendo).
- **An archetype beast** based on your share of correct answers.
- **Download your result as an image** and share it: LinkedIn, X, Facebook, copy link, and the native "Share" sheet on mobile.
- **A self-count block** — all correct answers and all archetypes for manual scoring, always available.
- **"How others answered"** — anonymous counters on Supabase: aggregates only, no personal data; writes go through a guarded function, direct table access is closed (RLS).
- **Accessibility:** WCAG AA contrast, large touch targets, mobile-first, `prefers-reduced-motion` support.

## Tech

- HTML + CSS + vanilla JavaScript (dependency-free core)
- Supabase (Postgres + RPC) — aggregated answer counters
- GitHub Pages — hosting
- Python logic tests (`test_logic.py`)

---

Built with care for the details ✨
