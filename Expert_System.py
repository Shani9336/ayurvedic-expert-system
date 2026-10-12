"""
Ayurvedic Classification as a Rule-Based Expert System
Prakriti (body constitution) classification using forward chaining.
Educational project - not a medical diagnosis tool.
"""

DOSHAS = ["Vata", "Pitta", "Kapha"]

# ---------------- KNOWLEDGE BASE: attributes ----------------
# attribute -> (question, [(value, description), ...])
# option order = Vata, Pitta, Kapha
ATTRIBUTES = {
    "frame": ("Body frame",
              [("thin", "Thin and light"),
               ("medium", "Medium and muscular"),
               ("large", "Large and heavy")]),
    "skin": ("Skin type",
             [("dry", "Dry and rough"),
              ("warm", "Warm, sensitive, prone to redness"),
              ("oily", "Oily, smooth and soft")]),
    "appetite": ("Appetite and digestion",
                 [("irregular", "Irregular appetite"),
                  ("strong", "Strong appetite, quick digestion"),
                  ("slow", "Low appetite, slow digestion")]),
    "sleep": ("Sleep pattern",
              [("light", "Light, easily disturbed"),
               ("moderate", "Moderate and sound"),
               ("deep", "Deep and long")]),
    "climate": ("Climate dislike",
                [("dislikes_cold", "Dislikes cold and wind"),
                 ("dislikes_heat", "Dislikes heat and sun"),
                 ("dislikes_damp", "Dislikes damp, cool weather")]),
    "temperament": ("Temperament",
                    [("quick_anxious", "Quick, enthusiastic, anxious"),
                     ("sharp_irritable", "Sharp, focused, irritable"),
                     ("calm_steady", "Calm, steady, forgiving")]),
    "activity": ("Activity level",
                 [("restless", "Restless, always moving"),
                  ("purposeful", "Purposeful and goal oriented"),
                  ("slow_steady", "Slow, steady, enduring")]),
    "stress": ("Reaction to stress",
               [("worry", "Worry and fear"),
                ("anger", "Anger and frustration"),
                ("withdrawal", "Withdrawal and silence")]),
}

ADVICE = {
    "Vata": "Prefer warm, cooked, moist foods; keep a regular routine; "
            "get enough rest; avoid cold, dry and very irregular habits.",
    "Pitta": "Prefer cooling, mildly sweet and bitter foods; avoid excess "
             "spicy, fried and sour food; avoid overheating and overwork.",
    "Kapha": "Prefer light, warm, spiced food; take regular vigorous "
             "exercise; avoid heavy, oily, sweet food and daytime sleep.",
}


def build_rules():
    """Scoring rules R01..R24: IF attribute = value THEN dosha +1"""
    rules, n = [], 1
    for attr, (_, options) in ATTRIBUTES.items():
        for i, (value, _) in enumerate(options):
            rules.append({"id": "R%02d" % n, "attr": attr,
                          "val": value, "dosha": DOSHAS[i]})
            n += 1
    return rules


RULES = build_rules()


# ---------------- INFERENCE ENGINE (forward chaining) ----------------
def infer(facts):
    score = {d: 0 for d in DOSHAS}
    trace = []
    # Phase 1: fire every scoring rule whose condition matches the facts
    for r in RULES:
        if facts.get(r["attr"]) == r["val"]:
            score[r["dosha"]] += 1
            trace.append("%s: IF %s = %s THEN %s +1"
                         % (r["id"], r["attr"], r["val"], r["dosha"]))
    # Phase 2: classification rules on the accumulated scores
    ranked = sorted(DOSHAS, key=lambda d: -score[d])
    top, mid, low = (score[d] for d in ranked)
    if top - mid >= 2:
        rule, result = "C1", "%s Prakriti (Ekadoshaja)" % ranked[0]
        advice = ADVICE[ranked[0]]
    elif top - low <= 1:
        rule, result = "C3", "Sama Prakriti (Sannipataja / Tridoshaja)"
        advice = "Maintain balance of all three doshas with a varied diet."
    else:
        rule = "C2"
        result = "%s-%s Prakriti (Dvandvaja)" % (ranked[0], ranked[1])
        advice = ADVICE[ranked[0]] + " Also: " + ADVICE[ranked[1]]
    trace.append("%s: classification rule fired -> %s" % (rule, result))
    return {"score": score, "result": result,
            "advice": advice, "trace": trace}


def ask_user():
    facts = {}
    for attr, (title, options) in ATTRIBUTES.items():
        print("\n%s?" % title)
        for i, (_, desc) in enumerate(options, 1):
            print("  %d. %s" % (i, desc))
        while True:
            ch = input("Enter choice (1-3): ").strip()
            if ch in ("1", "2", "3"):
                facts[attr] = options[int(ch) - 1][0]
                break
            print("Invalid input, try again.")
    return facts


def show(out):
    print("\n----- RESULT -----")
    for d in DOSHAS:
        print("%-6s score: %d" % (d, out["score"][d]))
    print("Prakriti :", out["result"])
    print("Advice   :", out["advice"])
    print("\n----- EXPLANATION (rules fired) -----")
    for line in out["trace"]:
        print(line)


if __name__ == "__main__":
    print("AYURVEDIC PRAKRITI EXPERT SYSTEM")
    show(infer(ask_user()))
    print("\nNote: educational use only; consult a qualified Vaidya.")
