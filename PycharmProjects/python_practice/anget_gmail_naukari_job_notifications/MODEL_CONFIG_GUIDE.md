# 🤖 Ollama Model Configuration Guide

## Current Model: Qwen2 1.5B

Your project is now configured to use **Qwen2 1.5B**, a lightweight and efficient language model.

---

## 📊 Model Comparison

| Aspect | Qwen2 1.5B | Llama3 | Qwen2 7B |
|--------|-----------|--------|----------|
| **Size** | 1.5 GB | ~4 GB | 7 GB |
| **Speed** | Fast (2-5s) | Medium (5-10s) | Slower (10-15s) |
| **Memory** | ~3 GB | ~8 GB | ~16 GB |
| **Accuracy** | Good | Excellent | Excellent |
| **Recommended** | ✅ Default | General use | High accuracy |

---

## 🚀 Quick Start with Qwen2 1.5B

### Step 1: Download the Model
```bash
ollama pull qwen2:1.5b
```

### Step 2: Start Ollama
```bash
ollama serve
```

### Step 3: Run Your App
```bash
streamlit run ai_streamlit.py
```

---

## 🔧 How to Change Models

### Option 1: Change in Code
Edit `summarize_emails.py` line 26:
```python
response = ollama.chat(
    model="qwen2:1.5b",  # ← Change this
    messages=[{"role": "user", "content": prompt}]
)
```

### Option 2: Available Models

#### Lightweight Models (Recommended for laptops)
```bash
ollama pull qwen2:1.5b        # 1.5 GB (CURRENT)
ollama pull qwen2:0.5b        # 500 MB (Ultra-fast)
ollama pull phi:2.7b          # 1.6 GB (Fast & accurate)
```

#### Medium Models
```bash
ollama pull qwen2:7b          # 7 GB (Good balance)
ollama pull mistral:7b        # 4 GB (Fast & smart)
```

#### Large Models (Needs powerful computer)
```bash
ollama pull llama3            # 4 GB (Excellent)
ollama pull qwen2:72b         # 42 GB (Very powerful)
```

---

## 📋 Installation Steps by Model

### For Qwen2 1.5B (Current - Recommended)
```bash
# Download model
ollama pull qwen2:1.5b

# Verify installation
ollama list

# Should show: qwen2:1.5b     1.5 GB
```

### For Qwen2 0.5B (Ultra-Lightweight)
```bash
ollama pull qwen2:0.5b
# Then update summarize_emails.py to use "qwen2:0.5b"
```

### For Llama3 (Powerful)
```bash
ollama pull llama3
# Then update summarize_emails.py to use "llama3"
```

---

## ✅ Verify Model is Working

```bash
# Test the model
ollama run qwen2:1.5b "What is a software engineer?"

# Should respond with relevant text

# Then run your app
streamlit run ai_streamlit.py
```

---

## 🎯 Performance Metrics

### Qwen2 1.5B (Current)
- **Download Time:** ~5 minutes
- **Storage:** 1.5 GB
- **RAM Usage:** 3-4 GB
- **Processing Time:** 2-5 seconds per email
- **Quality:** Good job extraction
- **Best For:** Laptops, normal usage

### Qwen2 0.5B
- **Download Time:** ~2 minutes
- **Storage:** 500 MB
- **RAM Usage:** 1-2 GB
- **Processing Time:** 1-3 seconds per email
- **Quality:** Fast but less detailed
- **Best For:** Ultra-lightweight systems

### Llama3
- **Download Time:** ~20 minutes
- **Storage:** 4 GB
- **RAM Usage:** 8 GB
- **Processing Time:** 5-10 seconds per email
- **Quality:** Excellent accuracy
- **Best For:** High-quality summaries, powerful machines

---

## 🖥️ System Requirements by Model

### Qwen2 1.5B (Recommended)
- **RAM:** 4 GB minimum
- **Disk:** 2 GB free
- **CPU:** Intel i5 or equivalent
- **Status:** ✅ Works on most laptops

### Qwen2 0.5B (Ultra-Lightweight)
- **RAM:** 2 GB minimum
- **Disk:** 1 GB free
- **CPU:** Any modern CPU
- **Status:** ✅ Works on older machines

### Llama3
- **RAM:** 8 GB minimum
- **Disk:** 5 GB free
- **CPU:** Intel i7 or equivalent
- **Status:** ✅ Needs better specs

---

## 🔄 Switch Models (Example)

### To Switch from Qwen2 1.5B to Llama3:

```bash
# Step 1: Download Llama3
ollama pull llama3

# Step 2: Edit summarize_emails.py
# Change line 26 from:
#   model="qwen2:1.5b"
# To:
#   model="llama3"

# Step 3: Restart app
streamlit run ai_streamlit.py
```

---

## 📝 Configuration File

Your current configuration in `summarize_emails.py`:
```python
response = ollama.chat(
    model="qwen2:1.5b",  # ← Current model
    messages=[{"role": "user", "content": prompt}]
)
```

---

## 🎓 Model Selection Guide

### Choose Qwen2 1.5B if:
- ✅ You have a laptop
- ✅ You want fast processing (2-5 sec/email)
- ✅ You need low memory (3 GB)
- ✅ You want balanced speed & quality
- ✅ **You are here now**

### Choose Qwen2 0.5B if:
- ✅ You have very limited resources
- ✅ You need ultra-fast processing (1-3 sec/email)
- ✅ Speed is more important than accuracy
- ✅ You have <2 GB RAM

### Choose Llama3 if:
- ✅ You have a powerful computer
- ✅ You need high-quality summaries
- ✅ You can wait 5-10 seconds per email
- ✅ You have 8+ GB RAM

---

## 🚨 Troubleshooting

### "Model not found" error
```bash
# Solution: Download the model
ollama pull qwen2:1.5b
```

### "Connection refused" error
```bash
# Solution: Start Ollama service
ollama serve
```

### "Slow processing"
```bash
# Solution: Try lighter model
ollama pull qwen2:0.5b
# Then update summarize_emails.py to use "qwen2:0.5b"
```

### "Out of memory"
```bash
# Solution: Use lighter model
ollama pull qwen2:0.5b
```

---

## 📊 Model Status

**Current Model:** qwen2:1.5b ✅  
**Status:** Ready to use  
**Performance:** Optimized  
**Last Updated:** 2026-04-25  

---

## 🔗 Useful Commands

```bash
# List all installed models
ollama list

# Download a model
ollama pull <model-name>

# Delete a model
ollama rm <model-name>

# Start Ollama
ollama serve

# Test a model
ollama run <model-name> "Your question here"

# Get model info
ollama show <model-name>
```

---

## 💡 Pro Tips

1. **First Time Setup:**
   - Install: `ollama pull qwen2:1.5b`
   - Start: `ollama serve`
   - Run: `streamlit run ai_streamlit.py`

2. **Performance Optimization:**
   - Use Qwen2 1.5B for good balance
   - Use Qwen2 0.5B if you need speed
   - Use Llama3 if you need quality

3. **Multiple Models:**
   - You can have multiple models installed
   - Switch between them by changing the model name
   - Only one runs at a time

4. **Free Up Space:**
   - Delete unused models: `ollama rm llama3`
   - Check space: `ollama list`

---

## 📚 Resources

- **Ollama Official:** https://ollama.ai
- **Qwen2 Details:** https://huggingface.co/Qwen
- **Llama3 Details:** https://llama.meta.com
- **Model Comparison:** https://huggingface.co/models

---

**Your Current Setup: Qwen2 1.5B ✅ Ready to Go!**

