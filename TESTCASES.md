<div align="center">

# 🧪 Test Case Documentation

### Ayurvedic Classification as a Rule-Based Expert System 🌿

![Total](https://img.shields.io/badge/Total%20Tests-11-blue)
![Passed](https://img.shields.io/badge/Passed-11-brightgreen)
![Failed](https://img.shields.io/badge/Failed-0-red)
![Coverage](https://img.shields.io/badge/Rules%20Covered-C1%20%7C%20C2%20%7C%20C3-orange)

**🎓 T.Y.B.Sc. Computer Science | Sem V | IKS Project | 2026-27**

</div>

---

## 📌 1. Objective

To verify that the expert system:

- ✅ gives the **correct Prakriti** for single-dosha, dual-dosha and balanced inputs
- ✅ handles **extreme scores** (8 / 0 / 0) correctly
- ✅ applies the classification rules **C1, C2, C3** correctly at their **boundaries**
- ✅ **rejects invalid input** and asks again

## ⚙️ 2. Test Environment

| | |
|---|---|
| 🐍 **Language** | Python 3 |
| 📄 **File tested** | `expert_system.py` |
| 💻 **Interface** | Command line |
| 📦 **Libraries** | None (standard Python only) |

## 🧠 3. How Expected Results Are Decided

Each of the 8 answers fires one scoring rule (R01-R24) and adds **+1** to one dosha, so the total is always **8**. Then the doshas are sorted into **top, mid, low** and the first true rule fires:

| Rule | 🔎 Condition | ✅ Result |
|:---:|---|---|
| **C1** | top - mid >= 2 | Single dosha (Ekadoshaja) |
| **C2** | top - mid < 2 **AND** top - low >= 2 | Dual dosha (Dvandvaja) |
| **C3** | top - low <= 1 | Sama / balanced (Sannipataja) |

**Input order:** frame, skin, appetite, sleep, climate, temperament, activity, stress

---

## 📊 4. Summary of Results

| ID | 🧾 Category | Scores (V / P / K) | 🎯 Expected Result | 🔥 Rule | Status |
|:---:|---|:---:|---|:---:|:---:|
| **T1** | Single dosha | 7 / 1 / 0 | Vata Prakriti (Ekadoshaja) | C1 | ✅ Pass |
| **T2** | Single dosha | 1 / 7 / 0 | Pitta Prakriti (Ekadoshaja) | C1 | ✅ Pass |
| **T3** | Dual dosha | 0 / 4 / 4 | Pitta-Kapha Prakriti (Dvandvaja) | C2 | ✅ Pass |
| **T4** | Balanced | 3 / 3 / 2 | Sama Prakriti (Sannipataja) | C3 | ✅ Pass |
| **T5** | Extreme (all Vata) | 8 / 0 / 0 | Vata Prakriti (Ekadoshaja) | C1 | ✅ Pass |
| **T6** | Extreme (all Kapha) | 0 / 0 / 8 | Kapha Prakriti (Ekadoshaja) | C1 | ✅ Pass |
| **T7** | Boundary of C1 | 5 / 3 / 0 | Vata Prakriti (Ekadoshaja) | C1 | ✅ Pass |
| **T8** | Boundary of C2 | 4 / 3 / 1 | Vata-Pitta Prakriti (Dvandvaja) | C2 | ✅ Pass |
| **T9** | Tie at top | 4 / 4 / 0 | Vata-Pitta Prakriti (Dvandvaja) | C2 | ✅ Pass |
| **T10** | Boundary of C3 | 3 / 3 / 2 | Sama Prakriti (Sannipataja) | C3 | ✅ Pass |
| **T11** | Invalid input | N/A | Input rejected, asked again | - | ✅ Pass |

### 🏆 Final: **11 / 11 tests passed (100%)**

---

## 🔍 5. Detailed Test Cases

### 🟢 T1: Single dosha (Vata)
- **🎯 Purpose:** Strong Vata with a little Pitta; checks rule C1.
- **⌨️ Input:** `thin, dry, irregular, light, dislikes_cold, quick_anxious, restless, anger`
- **📈 Scores:** Vata **7**, Pitta **1**, Kapha **0**
- **🧮 Check:** top - mid = 7 - 1 = 6, which is >= 2, so **C1** fires
- **✅ Expected = Actual:** `Vata Prakriti (Ekadoshaja)` | **Pass**

### 🟢 T2: Single dosha (Pitta)
- **🎯 Purpose:** Strong Pitta with a little Vata; checks rule C1.
- **⌨️ Input:** `medium, warm, strong, moderate, dislikes_heat, sharp_irritable, purposeful, worry`
- **📈 Scores:** Vata **1**, Pitta **7**, Kapha **0**
- **🧮 Check:** top - mid = 7 - 1 = 6, which is >= 2, so **C1** fires
- **✅ Expected = Actual:** `Pitta Prakriti (Ekadoshaja)` | **Pass**

### 🟡 T3: Dual dosha (Pitta-Kapha)
- **🎯 Purpose:** Two doshas equal; checks rule C2.
- **⌨️ Input:** `large, oily, strong, moderate, dislikes_damp, sharp_irritable, slow_steady, anger`
- **📈 Scores:** Vata **0**, Pitta **4**, Kapha **4**
- **🧮 Check:** top - mid = 0 (< 2) and top - low = 4 (>= 2), so **C2** fires
- **✅ Expected = Actual:** `Pitta-Kapha Prakriti (Dvandvaja)` | **Pass**

### 🔵 T4: Balanced (Sama)
- **🎯 Purpose:** All three doshas almost equal; checks rule C3.
- **⌨️ Input:** `thin, warm, slow, light, dislikes_heat, calm_steady, restless, anger`
- **📈 Scores:** Vata **3**, Pitta **3**, Kapha **2**
- **🧮 Check:** top - low = 3 - 2 = 1 (<= 1), so **C3** fires
- **✅ Expected = Actual:** `Sama Prakriti (Sannipataja / Tridoshaja)` | **Pass**

### 🔴 T5: Extreme score (all Vata)
- **🎯 Purpose:** Maximum possible score for one dosha.
- **⌨️ Input:** `thin, dry, irregular, light, dislikes_cold, quick_anxious, restless, worry`
- **📈 Scores:** Vata **8**, Pitta **0**, Kapha **0**
- **🧮 Check:** top - mid = 8, so **C1** fires
- **✅ Expected = Actual:** `Vata Prakriti (Ekadoshaja)` | **Pass**

### 🔴 T6: Extreme score (all Kapha)
- **🎯 Purpose:** Maximum possible score for Kapha.
- **⌨️ Input:** `large, oily, slow, deep, dislikes_damp, calm_steady, slow_steady, withdrawal`
- **📈 Scores:** Vata **0**, Pitta **0**, Kapha **8**
- **🧮 Check:** top - mid = 8, so **C1** fires
- **✅ Expected = Actual:** `Kapha Prakriti (Ekadoshaja)` | **Pass**

### 🟣 T7: Boundary of C1 (gap exactly 2)
- **🎯 Purpose:** Smallest gap that still gives a single dosha.
- **⌨️ Input:** `thin, dry, irregular, light, dislikes_cold, sharp_irritable, purposeful, anger`
- **📈 Scores:** Vata **5**, Pitta **3**, Kapha **0**
- **🧮 Check:** top - mid = 5 - 3 = **2** (>= 2), so **C1** fires
- **✅ Expected = Actual:** `Vata Prakriti (Ekadoshaja)` | **Pass**

### 🟣 T8: Boundary of C2 (gap 1)
- **🎯 Purpose:** Gap of 1 between top and mid must give a dual dosha, not a single one.
- **⌨️ Input:** `thin, dry, irregular, light, dislikes_heat, sharp_irritable, purposeful, withdrawal`
- **📈 Scores:** Vata **4**, Pitta **3**, Kapha **1**
- **🧮 Check:** top - mid = 1 (< 2) and top - low = 3 (>= 2), so **C2** fires
- **✅ Expected = Actual:** `Vata-Pitta Prakriti (Dvandvaja)` | **Pass**

### 🟣 T9: Tie at the top
- **🎯 Purpose:** Two doshas tied for the highest score.
- **⌨️ Input:** `thin, dry, irregular, light, dislikes_heat, sharp_irritable, purposeful, anger`
- **📈 Scores:** Vata **4**, Pitta **4**, Kapha **0**
- **🧮 Check:** top - mid = 0 and top - low = 4, so **C2** fires
- **✅ Expected = Actual:** `Vata-Pitta Prakriti (Dvandvaja)` | **Pass**

### 🟣 T10: Boundary of C3 (top - low = 1)
- **🎯 Purpose:** Largest gap that still counts as balanced.
- **⌨️ Input:** `thin, dry, irregular, moderate, dislikes_heat, sharp_irritable, slow_steady, withdrawal`
- **📈 Scores:** Vata **3**, Pitta **3**, Kapha **2**
- **🧮 Check:** top - low = 3 - 2 = **1** (<= 1), so **C3** fires
- **✅ Expected = Actual:** `Sama Prakriti (Sannipataja / Tridoshaja)` | **Pass**

### ⛔ T11: Invalid input handling
- **🎯 Purpose:** The program must not crash or accept wrong answers.
- **⌨️ Input:** `0`, `4`, `abc`, or a blank entry at any question
- **🧮 Check:** only `1`, `2` or `3` are accepted in `ask_user()`
- **✅ Expected = Actual:** prints `Invalid input, try again.` and asks the same question again | **Pass**

---

## 🖥️ 6. Sample Output (T3)

```
----- RESULT -----
Vata   score: 0
Pitta  score: 4
Kapha  score: 4
Prakriti : Pitta-Kapha Prakriti (Dvandvaja)

----- EXPLANATION (rules fired) -----
R03: IF frame = large THEN Kapha +1
R06: IF skin = oily THEN Kapha +1
R08: IF appetite = strong THEN Pitta +1
R11: IF sleep = moderate THEN Pitta +1
R15: IF climate = dislikes_damp THEN Kapha +1
R17: IF temperament = sharp_irritable THEN Pitta +1
R21: IF activity = slow_steady THEN Kapha +1
R23: IF stress = anger THEN Pitta +1
C2: classification rule fired -> Pitta-Kapha Prakriti (Dvandvaja)
```

## ▶️ 7. How to Re-run the Tests

**Manual:** run `python expert_system.py` and enter the choices for any test input (1 = first option, 2 = second, 3 = third for each question).

**Automatic (T1-T10):** run the helper script:

```bash
python run_tests.py
```

## 🎯 8. Coverage

| Area | Covered by |
|---|---|
| Rule **C1** (single dosha) | T1, T2, T5, T6, T7 |
| Rule **C2** (dual dosha) | T3, T8, T9 |
| Rule **C3** (balanced) | T4, T10 |
| Extreme scores | T5, T6 |
| Boundary values | T7, T8, T10 |
| Tie handling | T9 |
| Input validation | T11 |

## 📝 9. Conclusion

All **11 test cases passed**. The expert system classifies single-dosha, dual-dosha and balanced Prakriti correctly, handles boundary values and ties, and rejects invalid input.

---

<div align="center">

*👩‍💻 Shani Yadav | T.Y.B.Sc. Computer Science, Sem V | Guide: Asst. Prof. Sini V.*

🙏 *Educational project, not medical advice.* 🇮🇳

</div>
