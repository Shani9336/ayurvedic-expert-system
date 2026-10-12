# ayurvedic-expert-system
Ayurvedic Classification as a Rule-Based Expert System: a Python program that classifies Prakriti (Vata, Pitta, Kapha) using IF-THEN rules and forward chaining. IKS project, TYBSc CS Sem 5.

<div align="center">

# 🌿 Ayurvedic Classification as a Rule-Based Expert System 🧘‍♂️

### *Where ancient Indian wisdom meets Artificial Intelligence* 🇮🇳🤖

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)
![Technique](https://img.shields.io/badge/Technique-Forward%20Chaining-green)
![Rules](https://img.shields.io/badge/Rules-24%20%2B%203-orange)
![Tests](https://img.shields.io/badge/Tests-11%2F11%20Passed-brightgreen)
![Project](https://img.shields.io/badge/Subject-IKS-purple)

**🎓 T.Y.B.Sc. Computer Science | Semester V | 2026-27**

</div>

---

## 📖 About the Project

🕉️ **Ayurveda** is a 3,000+ year old science of life. It does not treat everyone the same way. It first understands a person's natural constitution, called **Prakriti**, and then suggests diet and lifestyle to suit it.

👨‍⚕️ Normally this needs the experience of a **Vaidya**, and the classical rules are scattered across many texts. So this project turns that knowledge into a small **expert system** that acts like a simple Vaidya assistant.

✨ It makes the classification:

- ✅ **Consistent**: same input, same answer, every time
- 🔍 **Transparent**: it shows exactly *why* it gave a result
- 🔧 **Flexible**: rules can be added or edited without touching the engine

---

## 🌟 Features

| | Feature |
|---|---|
| ❓ | 8 simple questions, answered with 1, 2 or 3 |
| 📏 | 24 scoring rules (R01-R24) + 3 classification rules (C1-C3) |
| ⚙️ | Forward-chaining inference engine |
| 🧬 | Classifies into all **7 Prakriti types** |
| 💡 | Explanation facility showing every rule that fired |
| 🛡️ | Input validation for wrong entries |
| 🐍 | Pure Python 3, **no external libraries** |

---

## 🔱 The Three Doshas

| 🌬️ **Vata** | 🔥 **Pitta** | 🌊 **Kapha** |
|:---:|:---:|:---:|
| Air + Space | Fire + Water | Water + Earth |
| Movement | Transformation and digestion | Structure and lubrication |
| Dry, light, cold, mobile | Hot, sharp, oily, liquid | Heavy, slow, cool, steady |

### 🧿 Seven Types of Prakriti

| Group | Types |
|---|---|
| 1️⃣ **Ekadoshaja** (single dosha) | Vata, Pitta, Kapha |
| 2️⃣ **Dvandvaja** (dual dosha) | Vata-Pitta, Pitta-Kapha, Vata-Kapha |
| 3️⃣ **Sannipataja / Sama** (all three) | Vata-Pitta-Kapha |

---

## 🧠 How It Works

```
 👤 User               🗂️ Working Memory         ⚙️ Inference Engine        🎯 Result
(Questionnaire)  --->      (Facts)        --->   (Forward Chaining)   --->  (Prakriti Type)
                                                    ▲           │
                                      📚 Knowledge Base         └--->  💡 Explanation
                                        (R01-R24, C1-C3)               Facility
```

**🪜 Step by step**

1. 📝 The user answers 8 questions, and each answer is stored as a **fact**.
2. 🔥 Every matching scoring rule **fires** and adds +1 to Vata, Pitta or Kapha. The total is always **8**.
3. 📊 The doshas are sorted into **top, mid and low** scores.
4. 🏁 Classification rules are checked in order, and the **first true rule** fires.
5. 💬 Result, advice and the list of fired rules are displayed.

**🧩 The 8 attributes:** Body frame, Skin type, Appetite and digestion, Sleep pattern, Climate dislike, Temperament, Activity level, Reaction to stress.

**📌 Scoring rule example**

```
IF skin = dry THEN Vata score + 1
```

**🏆 Classification rules**

| Rule | 🔎 Condition | ✅ Result |
|:---:|---|---|
| **C1** | top - mid >= 2 | Single dosha Prakriti (Ekadoshaja) |
| **C2** | top - mid < 2 **AND** top - low >= 2 | Dual dosha Prakriti (Dvandvaja) |
| **C3** | top - low <= 1 | Sama Prakriti, all balanced (Sannipataja) |

---

## 🚀 How to Run

```bash
# 1️⃣ Make sure Python 3 is installed
python --version

# 2️⃣ Run the program
python expert_system.py
```

3️⃣ Answer the 8 questions by entering **1, 2 or 3** 🎉

---

## 🖥️ Sample Output (Test Case T3)

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

---

## 🧪 Testing

✅ **11 / 11 test cases passed**

| 🧾 Test cases | 🎯 What they check |
|:---:|---|
| **T1 - T4** | Typical single-dosha, dual-dosha and balanced results |
| **T5 - T6** | Extreme scores (8 / 0 / 0) |
| **T7 - T10** | Decision boundaries of C1, C2 and C3 |
| **T11** | Invalid input handling (0, 4, text, blank) |

---

## ⚠️ Limitations

- 🔸 Uses only 8 attributes. A real Vaidya also checks pulse (Nadi Pariksha), tongue and detailed history
- 🔸 All attributes have equal weight
- 🔸 Answers are self-reported
- 🔸 Classifies Prakriti only, no diagnosis or treatment
- 🔸 Basic text-based interface

## 🔮 Future Scope

- 🌱 More attributes and weighted rules, prepared with an Ayurvedic practitioner
- 🩺 Vikriti (current imbalance) assessment
- 🌫️ Fuzzy logic for in-between answers
- 📱 Web or mobile app with regional language support
- 🍎 Extend classification to foods (rasa and guna) and medicinal plants
- 🤖 Compare with a machine learning model trained on expert-labelled data

---

## 👩‍💻 Project Details

| | |
|---|---|
| 🧑‍🎓 **Student** | Shani Yadav |
| 📚 **Class** | T.Y.B.Sc. Computer Science, Sem V |
| 🧑‍🏫 **Guide** | Asst. Prof. Sini V. |
| 🏢 **Department** | Computer Science & Information Technology |
| 🏫 **College** | Smt. Devkiba Mohansinhji Chauhan College of Commerce and Science, Silvassa (Affiliated to University of Mumbai) |

---

## 📜 Disclaimer

> 🩺 This project is made **only for academic and educational purposes**. It is **not a medical device** and its output must not be treated as medical advice. Please consult a qualified Ayurvedic practitioner or doctor for any health concern.

<div align="center">

### 🙏 Thank you! 🇮🇳

*Made with ❤️ and Python*

</div>
