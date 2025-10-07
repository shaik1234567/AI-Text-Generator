# 🤖 AI Text Generator

An intelligent text generation system that analyzes sentiment from input prompts and generates sentiment-aligned paragraphs or essays. Built with state-of-the-art NLP models and an intuitive web interface.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)

---

## 🎯 Overview

This project demonstrates the integration of sentiment analysis and text generation to create an AI system that produces emotionally aligned content. The application detects whether an input prompt has a positive, negative, or neutral sentiment, then generates text that matches that emotional tone.

**Use Cases:**
- Content creation with specific emotional tones
- Creative writing assistance
- Educational demonstrations of NLP capabilities
- Sentiment-aware chatbot responses

---

## ✨ Features

### Core Features
- ✅ **Sentiment Analysis**: Automatically detects positive, negative, or neutral sentiment from input prompts
- ✅ **Sentiment-Aligned Generation**: Produces text matching the detected emotional tone
- ✅ **Interactive Web Interface**: User-friendly Streamlit-based UI
- ✅ **Confidence Scores**: Displays sentiment detection confidence levels
- ✅ **Adjustable Length**: Generate short, medium, or long text outputs
- ✅ **Manual Override**: Option to manually select desired sentiment

### Additional Features
- 📊 Real-time sentiment visualization with emojis
- 💾 Download generated text as `.txt` file
- 🎨 Clean, professional UI with custom styling
- ⚡ Model caching for fast performance
- 📱 Responsive design
- 🔧 Advanced settings for power users

---

## 🛠️ Technology Stack

### Machine Learning
- **Sentiment Analysis**: DistilBERT (distilbert-base-uncased-finetuned-sst-2-english)
- **Text Generation**: DistilGPT2
- **Framework**: Hugging Face Transformers
- **Deep Learning**: PyTorch

### Web Development
- **Frontend**: Streamlit
- **Backend**: Python 3.8+

### Why These Models?
- **DistilBERT**: Lightweight (66M parameters), fast inference, 97% of BERT's performance
- **DistilGPT2**: Smaller than GPT-2 (82M parameters), works well on CPU, suitable for real-time generation

---

## 📥 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- 2GB+ RAM recommended
- Internet connection (for first-time model download)

### Step 1: Clone or Download the Project
```bash
git clone <your-repo-url>
cd ai-text-generator
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

**Note**: First installation may take 5-10 minutes as it downloads AI models (~500MB).

### Step 4: Verify Installation
```bash
# Test sentiment analyzer
python sentiment_analyzer.py

# Test text generator
python text_generator.py
```

---

## 🚀 Usage

### Running the Application

1. **Start the Streamlit app**:
```bash
streamlit run app.py
```

2. **Browser opens automatically** at `http://localhost:8501`

3. **Enter your prompt** in the text area

4. **Click "Generate Text"** and watch the magic happen!

### Example Prompts

| Prompt | Expected Sentiment | Generated Text Style |
|--------|-------------------|---------------------|
| "I love sunny days at the beach" | Positive | Uplifting, cheerful |
| "Traffic jams are frustrating" | Negative | Critical, pessimistic |
| "Climate change statistics" | Neutral | Objective, balanced |

### Using Manual Sentiment Override

1. Check "Override Sentiment Detection" in sidebar
2. Select desired sentiment (positive/negative/neutral)
3. Enter any prompt - it will generate text in the selected sentiment regardless of prompt sentiment

---

## 📁 Project Structure

```
ai-text-generator/
│
├── app.py                      # Main Streamlit web application
├── sentiment_analyzer.py       # Sentiment detection module
├── text_generator.py           # Text generation module
├── config.py                   # Configuration settings
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation (this file)
├── .gitignore                  # Git ignore rules
│
└── (auto-generated folders)
    ├── .streamlit/             # Streamlit config (auto-created)
    └── models/                 # Cached AI models (auto-downloaded)
```

### File Descriptions

| File | Purpose |
|------|---------|
| `app.py` | Main application entry point with Streamlit UI |
| `sentiment_analyzer.py` | Sentiment detection logic using DistilBERT |
| `text_generator.py` | Text generation logic using DistilGPT2 |
| `config.py` | Central configuration (model names, parameters, templates) |
| `requirements.txt` | Python package dependencies |

---

## 🔍 How It Works

### Workflow Diagram
```
User Input Prompt
       ↓
[Sentiment Analyzer]
       ↓
Detected Sentiment (+ Confidence Score)
       ↓
[Prompt Engineering]
       ↓
[Text Generator]
       ↓
Generated Sentiment-Aligned Text
```

### Technical Pipeline

#### 1. **Sentiment Analysis**
```python
# User enters: "I love sunny days"
# Model: DistilBERT analyzes sentiment
# Output: POSITIVE (confidence: 0.98)
```

#### 2. **Prompt Engineering**
```python
# Original: "sunny days"
# Enhanced: "Write an uplifting and positive text about: sunny days. This is wonderful."
# Purpose: Guide the generation model toward positive tone
```

#### 3. **Text Generation**
```python
# Model: DistilGPT2 generates text
# Parameters: temperature=0.8, top_k=50, top_p=0.95
# Output: Coherent paragraph matching positive sentiment
```

#### 4. **Post-Processing**
```python
# Clean output (remove prompt prefix)
# Format text (punctuation, spacing)
# Display with sentiment metadata
```

---

## 🧠 Methodology

### Sentiment Analysis Approach
- **Model**: Pre-trained DistilBERT fine-tuned on SST-2 (Stanford Sentiment Treebank)
- **Classes**: Binary classification (Positive/Negative) mapped to 3 classes (Positive/Negative/Neutral)
- **Threshold**: Confidence < 0.6 treated as Neutral

### Text Generation Strategy
- **Base Model**: DistilGPT2 (causal language model)
- **Prompt Templates**: Sentiment-specific prefixes guide generation tone
- **Sampling**: Temperature-based sampling for diverse, natural outputs
- **Length Control**: User-configurable (50-500 tokens)

### Optimization for CPU
- Used distilled models (66M-82M parameters vs 110M-340M)
- Disabled GPU (device=-1) for broader compatibility
- Cached models to avoid reloading
- Efficient tokenization

---

## 🚀 Future Enhancements

### Short-term Improvements
- [ ] Add more sentiment categories (e.g., angry, joyful, fearful)
- [ ] Support multiple languages
- [ ] Implement text style transfer (formal/informal)
- [ ] Add word count target input
- [ ] Save generation history

### Long-term Goals
- [ ] Fine-tune models on domain-specific data
- [ ] Implement user feedback loop for model improvement
- [ ] Add GPT-3.5/4 API integration option
- [ ] Create mobile app version
- [ ] Multi-paragraph essay generation
- [ ] Real-time collaborative editing

---

## 🌐 Deployment

### Deploy to Streamlit Cloud (Free)

1. **Push code to GitHub**:
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <your-github-repo>
git push -u origin main
```

2. **Go to**: [streamlit.io/cloud](https://streamlit.io/cloud)

3. **Sign in** with GitHub

4. **Click "New app"**:
   - Repository: Select your repo
   - Branch: `main`
   - Main file path: `app.py`

5. **Click "Deploy"** - Done! 🎉

**Live URL**: Your app will be available at `https://<your-app-name>.streamlit.app`

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👨‍💻 Author

**Your Name**
- GitHub: [@shaik1234567](https://github.com/shaik1234567)
- LinkedIn: [shaik shivaji](https://www.linkedin.com/in/shivaji-shaik-b92b19270/)
- Email: shaikshivaji2004@gmail.com

---

## 🙏 Acknowledgments

- **Hugging Face** for providing pre-trained models and transformers library
- **Streamlit** for the amazing web framework
- **PyTorch** team for the deep learning framework
- **OpenAI** for inspiration in text generation research

---

## 📚 References

- [DistilBERT Paper](https://arxiv.org/abs/1910.01108)
- [GPT-2 Paper](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)
- [Hugging Face Transformers Documentation](https://huggingface.co/docs/transformers)
- [Streamlit Documentation](https://docs.streamlit.io)

---

## 📞 Support

Having issues? Here's how to get help:

1. Check the [Issues](../../issues) page
2. Review the [FAQ](#faq) section below
3. Contact the author


**⭐ If you found this project helpful, please give it a star!**

---

*Built with ❤️ for AI/ML enthusiasts and developers*