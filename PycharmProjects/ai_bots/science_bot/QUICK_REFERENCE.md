# 🔬 Science Bot - Quick Reference

Fast answers to common questions and quick formula lookup.

## 🚀 Quick Start (30 seconds)

1. Run: `.\START_CHATBOT.ps1` (Windows) or `streamlit run app.py`
2. Browser opens at `http://localhost:8501`
3. Select difficulty level and science subject
4. Ask your question!

## ❓ FAQ

### Q: How do I install this?
**A:** See [SETUP_GUIDE.md](SETUP_GUIDE.md) for complete instructions.

### Q: What if Ollama won't start?
**A:** 
- Download from https://ollama.ai
- Run the installer
- Look for Ollama icon in system tray
- Wait 30 seconds then refresh browser

### Q: Can I ask multiple questions?
**A:** Yes! The bot remembers your conversation history and context.

### Q: How do I clear chat history?
**A:** Refresh the browser page (F5) to start a new conversation.

### Q: Does it work offline?
**A:** No, Ollama service must be running in background.

### Q: Can I change the AI model?
**A:** Yes, in `app.py` change `model="qwen2:1.5b"` to another Ollama model.

### Q: What are the system requirements?
**A:** Minimum: 4GB RAM, Python 3.8+, Windows/Mac/Linux

---

## 📚 Quick Formula Reference

### Physics
| Concept | Formula | Variables |
|---------|---------|-----------|
| Force | F = ma | F (N), m (kg), a (m/s²) |
| Work | W = Fd | W (J), F (N), d (m) |
| Kinetic Energy | KE = ½mv² | KE (J), m (kg), v (m/s) |
| Potential Energy | PE = mgh | PE (J), m (kg), g (9.8 m/s²), h (m) |
| Power | P = W/t | P (W), W (J), t (s) |
| Momentum | p = mv | p (kg·m/s), m (kg), v (m/s) |
| Velocity | v = d/t | v (m/s), d (m), t (s) |
| Acceleration | a = Δv/Δt | a (m/s²), Δv (m/s), Δt (s) |
| Pressure | P = F/A | P (Pa), F (N), A (m²) |
| Density | ρ = m/V | ρ (kg/m³), m (kg), V (m³) |
| Energy | E = mc² | E (J), m (kg), c (3×10⁸ m/s) |
| Ohm's Law | V = IR | V (V), I (A), R (Ω) |
| Frequency & Wavelength | c = fλ | c (m/s), f (Hz), λ (m) |

### Chemistry
| Concept | Formula | Variables |
|---------|---------|-----------|
| Molarity | M = n/V | M (mol/L), n (mol), V (L) |
| pH | pH = -log[H⁺] | pH (scale), [H⁺] (mol/L) |
| Ideal Gas Law | PV = nRT | P (Pa), V (m³), n (mol), R, T (K) |
| Molar Mass | M = m/n | M (g/mol), m (g), n (mol) |
| Mass Percent | % = (mass solute/mass solution)×100 | Mass (g) |
| Percent Yield | %Y = (actual/theoretical)×100 | Yield (%) |
| Molality | m = n/kg solvent | m (mol/kg), n (mol) |

### Biology
| Concept | Formula | Description |
|---------|---------|-------------|
| Hardy-Weinberg | p² + 2pq + q² = 1 | Genetic equilibrium |
| Population Growth | N(t) = N₀·e^(rt) | N (population), r (growth rate), t (time) |
| ATP Energy | ~30.5 kJ/mol | Molar energy from ATP hydrolysis |
| Cell Division | 2ⁿ = cells | n (number of divisions) |

---

## ⚙️ Keyboard Shortcuts

| Action | Windows | Mac |
|--------|---------|-----|
| Clear Cache | Ctrl + Shift + R | Cmd + Shift + R |
| Open Settings | Click ⚙️ (top right) | Click ⚙️ (top right) |
| Refresh Page | F5 | Cmd + R |
| Full Screen | F11 | Cmd + Ctrl + F |

---

## 🎯 Example Questions to Try

### Physics
- "What is Newton's Second Law (F=ma)?"
- "Explain kinetic energy formula"
- "How does E=mc² work?"
- "What is momentum?"
- "Explain Ohm's Law"

### Chemistry
- "What is the pH formula?"
- "Explain the ideal gas law"
- "How to calculate molarity?"
- "What is stoichiometry?"
- "Explain chemical bonding"

### Biology
- "How does photosynthesis work?"
- "Explain DNA structure"
- "What is Hardy-Weinberg?"
- "How do cells divide?"
- "Explain natural selection"

### Earth Science
- "What causes earthquakes?"
- "Explain plate tectonics"
- "How does the water cycle work?"
- "What is the carbon cycle?"
- "How are rocks formed?"

---

## 🔧 Common Fixes

### Bot not responding
1. Check Ollama is running (system tray)
2. Refresh browser (F5)
3. Wait 10 seconds
4. Try again

### Slow responses
1. Close other applications
2. Restart Ollama
3. Check internet speed
4. Restart computer if needed

### Error messages
1. Read the error carefully
2. Check [SETUP_GUIDE.md](SETUP_GUIDE.md) troubleshooting
3. Verify Ollama is running
4. Reinstall: `pip install -r requirements.txt --force-reinstall`

---

## 📊 Difficulty Levels Explained

| Level | Best For | Complexity |
|-------|----------|-----------|
| Elementary (K-5) | Young students, basic concepts | Simple explanations, no advanced math |
| Middle School (6-8) | Middle schoolers | Basic formulas, simple derivations |
| High School (9-12) | High schoolers | Complex formulas, full derivations |
| College Level | University students | Advanced math, research-level theory |
| Advanced Research | Researchers | Cutting-edge concepts, specialized topics |

---

## 📚 Learning Styles Explained

| Style | What You Get | Best For |
|-------|-------------|---------|
| Quick Formula | Just the formula | Quick reference, exams |
| Formula Explained | Formula + variable meanings | Understanding notation |
| Detailed Theory | Full theory + derivation | Deep understanding |
| Lab Simulation | Experimental approach | Hands-on learning |

---

## 🌟 Tips & Tricks

1. **Ask for specific help**: "explain the variables in F=ma" works better than "what is force?"

2. **Use follow-up questions**: After a response, ask "can you show me an example?" or "how is this used?"

3. **Try different learning styles**: If one doesn't work, switch to another

4. **Save responses**: Copy important formulas and explanations to your notes

5. **Check multiple sources**: Use this bot alongside textbooks and Khan Academy

6. **Regular breaks**: Learning science is a marathon, not a sprint!

---

## 📞 Support Resources

- **Ollama**: https://ollama.ai
- **Streamlit**: https://streamlit.io
- **Python**: https://python.org
- **Science Education**: Khan Academy, OpenStax

---

## ✨ Fun Facts

- This bot uses Qwen2, an advanced AI model by Alibaba
- Ollama allows running AI models locally (privacy-friendly!)
- Streamlit makes interactive web apps with pure Python
- Science formulas are the language of the universe! 🌌

---

**Need more help?** See [SETUP_GUIDE.md](SETUP_GUIDE.md) or [README.md](README.md)

Happy learning! 🔬✨

