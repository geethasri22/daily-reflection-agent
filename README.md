# daily-reflection-agent
# 🌱 Daily Reflection Tree (Deterministic System)

## Problem Statement

Design a deterministic decision tree for a structured daily reflection process.
The goal is to transform subjective reflection into a structured, actionable system.

---

## Approach

* Built a **rule-based deterministic decision tree**
* Focused on:

  * Task completion
  * Emotional reflection
  * Root cause analysis
  * Action planning
* Ensured **no randomness** and **fixed transitions**

---

## Decision Tree Overview

1. Start Reflection
2. Task Completion Check
3. Blocker Identification (if failed)
4. Satisfaction Rating (if completed)
5. Improvement / Reinforcement
6. Next-Day Planning

---

## Decision Tree Diagram

```mermaid```
graph TD
    A[Start Reflection] --> B{Completed Main Goal?}

    B -->|No| C[Identify Blocker]
    C --> D{Blocker Type}

    D -->|Time| E[Suggest Task Breakdown]
    D -->|Focus| F[Suggest Pomodoro]
    D -->|Distraction| G[Reduce Distractions]

    B -->|Yes| H[Rate Satisfaction 1-5]
    H -->|>=4| I[What Went Well]
    H -->|<=3| J[What Can Improve]

    I --> K[Reinforce Behavior]
    J --> L[Improvement Plan]

    E --> M[Plan Tomorrow]
    F --> M
    G --> M
    K --> M
    L --> M

    M --> N[End]

## Implementation

* Python CLI-based system
* Deterministic branching using `if-else`
* Input-driven navigation through tree

---

## Guardrails Against AI Hallucination

* Only predefined inputs allowed (yes/no, fixed categories)
* No probabilistic or random logic
* All decisions are rule-based
* Invalid inputs handled explicitly
* No free-form AI-generated branching

---

## Structural Insight (KEY LEARNING)

While building this system, the difference between structured and unstructured thinking became clear:

### Without Structure:

* Reflection is inconsistent
* No clear outcomes
* Hard to track improvement
* Depends on mood

### With Deterministic Structure:

* Every input leads to a defined output
* Patterns (like recurring blockers) become visible
* Reflection becomes actionable
* AI systems can reliably operate on structured input

### Key Realization:

**Structure converts subjective reflection into actionable, repeatable intelligence.**

---

## How to Run

```bash
python agent.py
```

## Future Improvements

* Store daily reflections (history tracking)
* Add scoring system
* Convert into web/mobile app
* Integrate with AI summarization

---

## 👤 Persona

Persona: College student preparing for placements

Context:
- Managing daily study, coding, and aptitude practice
- Struggles with consistency and distractions
- Goal is to improve productivity and track performance


Decision Tree logic:

Start
↓
Did you complete your main goal? (yes/no)

IF NO:
  ↓
  What blocked you? (time/focus/distraction)
  ↓
  Give suggestion based on blocker

IF YES:
  ↓
  Rate satisfaction (1–5)

  IF ≥4:
    → What went well → reinforce

  IF ≤3:
    → What to improve → improvement

↓
Plan tomorrow? (yes/no)
↓
End

## Guardrails Against AI Hallucination

- Only predefined inputs allowed
- No randomness or probabilistic outputs
- All decisions follow deterministic logic
- Invalid inputs handled explicitly
- No free-form AI-generated branching
  
