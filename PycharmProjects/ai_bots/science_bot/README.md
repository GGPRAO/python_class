# 🔬 Science Formula & Concept Bot

An intelligent, AI-powered chatbot application for exploring science formulas, concepts, and theories with detailed explanations. Master physics, chemistry, biology, and more across all educational levels.

## ✨ Features

### 📚 Comprehensive Science Subjects
- **🔋 Physics**: Motion, forces, energy, waves, electricity, magnetism, optics, relativity
- **⚗️ Chemistry**: Atomic structure, chemical bonds, reactions, states of matter
- **🧬 Biology**: Cells, genetics, evolution, ecosystems, human body systems
- **🌍 Earth & Environmental Science**: Geology, weather, climate, plate tectonics, oceanography
- **🔭 Astronomy & Space**: Celestial mechanics, stars, galaxies, cosmology
- **💡 Quantum Mechanics**: Uncertainty principle, superposition, wave-particle duality
- **🌊 Thermodynamics**: Heat, entropy, laws of thermodynamics, energy transfer
- **⚛️ Atomic & Nuclear Science**: Radioactivity, fission, fusion, atomic physics

### 🎓 Difficulty Levels
- **Elementary (K-5)**: Basic science concepts and simple phenomena
- **Middle School (6-8)**: Foundational science principles and introductory formulas
- **High School (9-12)**: Advanced concepts, complex formulas, mathematical applications
- **College Level**: University-level science, advanced mathematics, research-oriented
- **Advanced Research**: Cutting-edge research, specialized topics, theoretical science

### 💡 Learning Styles
- **Quick Formula**: Fast reference with just the essential formula
- **Formula Explained**: Formula with clear variable definitions
- **Detailed Theory**: In-depth theory, full derivations, and scientific reasoning
- **Lab Simulation**: Experimental approach and hands-on learning guidance

### 🎯 Smart Features
- ✅ **Formula Derivation**: Step-by-step mathematical derivations explained
- 🌍 **Real-World Applications**: Connect science to practical, real-world scenarios
- 🔍 **Common Misconceptions**: Address typical misunderstandings in science
- 📊 **Physical Constants**: Includes relevant SI units and scientific constants
- 🧪 **Lab Simulation**: Experimental methods and verification techniques
- 📖 **Concept Connections**: Links between related scientific topics
- 💬 **Interactive Dialogue**: Ask follow-up questions for deeper understanding
- 🎓 **Difficulty Scaling**: Content adapts to your educational level

## 📋 Quick Start

### Prerequisites
- Python 3.8 or higher
- Ollama (for AI responses)
- Internet connection
- 4GB RAM minimum

### Installation

1. **Clone or navigate to the project directory:**
```bash
cd C:\Users\USER\PycharmProjects\ai_bots\science_bot
```

2. **Install required Python packages:**
```bash
pip install -r requirements.txt
```

3. **Install Ollama:**
   - Download from: https://ollama.ai
   - Follow installation instructions for your operating system
   - After installation, pull the required model:
   ```bash
   ollama pull qwen2:1.5b
   ```

4. **Run Ollama service:**
   - Start the Ollama application (should run in background)
   - Verify it's running on `http://localhost:11434`

5. **Launch the Science Bot:**
   
   **Option A - Windows PowerShell:**
   ```powershell
   .\START_CHATBOT.ps1
   ```
   
   **Option B - Command Prompt:**
   ```cmd
   START_CHATBOT.bat
   ```
   
   **Option C - Direct Command:**
   ```bash
   streamlit run app.py
   ```

The bot will open in your default browser at `http://localhost:8501`

## 🚀 Usage Guide

### Getting Started
1. Launch the Science Bot using one of the methods above
2. Select your **difficulty level** (Elementary to Advanced Research)
3. Choose a **science subject** (Physics, Chemistry, Biology, etc.)
4. Pick your preferred **learning style** (Quick Formula, Explained, Detailed, or Lab Simulation)
5. (Optional) Enter your **current topic** for more focused responses

### Asking Questions
- Type your science question in the input field
- Examples:
  - "What is E=mc² and what does it mean?"
  - "Explain the photosynthesis formula"
  - "How does Newton's second law work?"
  - "What is the formula for pH calculation?"
  - "Explain quantum entanglement"

### Features Explained

**Quick Formula Mode**
- Returns just the formula with minimal explanation
- Perfect for quick reference
- Best for: Formula lookup, exam prep

**Formula Explained Mode**
- Provides formula + variable definitions
- Explains what each symbol means
- Includes SI units
- Best for: Understanding the parts

**Detailed Theory Mode**
- Full mathematical derivation
- Scientific theory and principles
- Real-world applications
- Common misconceptions
- Best for: Deep learning

**Lab Simulation Mode**
- Experimental approach
- How to verify the concept
- Expected observations
- Hands-on learning guide
- Best for: Practical understanding

### Customization Options
- ✅ **Show Formula Derivation**: Toggle to see step-by-step math
- ✅ **Show Real-World Applications**: Get practical examples
- 📝 **Current Topic**: Helps tailor responses to what you're studying

## 📚 Example Topics

### Physics
- Newton's Laws (F=ma, a=F/m)
- Kinetic Energy (KE = ½mv²)
- Potential Energy (PE = mgh)
- Wave Equation (v = fλ)
- Einstein's Relativity (E=mc²)
- Ohm's Law (V=IR)
- Force (F = m·a)

### Chemistry
- Chemical Reactions (aA + bB → cC + dD)
- Molar Mass Calculations
- pH Formula (pH = -log[H⁺])
- Ideal Gas Law (PV = nRT)
- Le Chatelier's Principle
- Electron Configuration
- Stoichiometry

### Biology
- Photosynthesis (6CO₂ + 6H₂O + light → C₆H₁₂O₆ + 6O₂)
- Cellular Respiration
- DNA Replication
- Mendel's Laws of Inheritance
- Hardy-Weinberg Equation
- Population Growth Models

### Earth & Environmental Science
- Richter Scale (Magnitude = log₁₀(Amplitude) + constant)
- Carbon Cycle
- Water Cycle
- Plate Tectonics
- Climate Change Models

## ⚙️ System Requirements

- **OS**: Windows, macOS, or Linux
- **Python**: 3.8 or higher
- **RAM**: Minimum 4GB (8GB recommended)
- **Storage**: 2GB for Ollama model
- **Internet**: Required for initial setup only

## 🔧 Troubleshooting

### Issue: "Ollama is not running"
**Solution:**
- Make sure Ollama application is launched
- On Windows: Look for Ollama icon in system tray
- Check if running on `http://localhost:11434`

### Issue: "Model not found"
**Solution:**
```bash
ollama pull qwen2:1.5b
```

### Issue: Slow response times
**Solution:**
- Check system RAM usage
- Close other applications
- Ensure stable internet connection
- Restart Ollama service

### Issue: App crashes
**Solution:**
- Verify all dependencies are installed: `pip install -r requirements.txt`
- Update Streamlit: `pip install --upgrade streamlit`
- Clear Streamlit cache: Delete `.streamlit/cache` folder

## 📖 Science Formulas Reference

### Physics Formulas
- **Force**: F = ma (Newton's Second Law)
- **Work**: W = Fd·cos(θ)
- **Power**: P = W/t = Fd/t
- **Energy**: E = mc² (Mass-Energy Equivalence)
- **Momentum**: p = mv
- **Pressure**: P = F/A
- **Density**: ρ = m/V
- **Acceleration**: a = (v_f - v_i)/t
- **Frequency & Wavelength**: c = fλ
- **Ohm's Law**: V = IR

### Chemistry Formulas
- **Molarity**: M = n/V
- **pH**: pH = -log[H⁺]
- **Ideal Gas Law**: PV = nRT
- **Molar Mass**: M = m/n
- **Stoichiometry**: n₁/a = n₂/b

### Biology Formulas
- **Cell Division**: Mitosis and Meiosis equations
- **Population Growth**: N(t) = N₀·e^(rt)
- **Hardy-Weinberg**: p² + 2pq + q² = 1

## 📞 Support & Resources

- **Ollama Documentation**: https://ollama.ai/library
- **Science Education**: Khan Academy, OpenStax, MIT OpenCourseWare
- **Model Information**: Qwen2 LLM by Alibaba

## 📝 License

This project is created for educational purposes.

## 🙏 Credits

- Built with **Streamlit** for interactive UI
- AI powered by **Ollama** and **Qwen2 LLM**
- Designed for science learners at all levels

---

**Happy Learning! 🔬✨**

