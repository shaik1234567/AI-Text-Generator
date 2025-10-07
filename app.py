"""
AI Text Generator - Main Streamlit Application
A web interface for sentiment-aligned text generation
"""

import streamlit as st
from sentiment_analyzer import SentimentAnalyzer
from text_generator import TextGenerator
import config

# Page configuration
st.set_page_config(
    page_title="AI Text Generator",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1F77B4;
        margin-bottom: 1rem;
    }
    .sentiment-box {
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        text-align: center;
    }
    .positive-box {
        background-color: #d4edda;
        border: 2px solid #28a745;
    }
    .negative-box {
        background-color: #f8d7da;
        border: 2px solid #dc3545;
    }
    .neutral-box {
        background-color: #d1ecf1;
        border: 2px solid #17a2b8;
    }
    .output-box {
        padding: 1.5rem;
        border-radius: 10px;
        background-color: #f8f9fa;
        border-left: 5px solid #1F77B4;
        margin-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state for models (load only once)
@st.cache_resource
def load_models():
    """Load models once and cache them"""
    sentiment_analyzer = SentimentAnalyzer()
    text_generator = TextGenerator()
    return sentiment_analyzer, text_generator

# Main app
def main():
    # Header
    st.markdown('<p class="main-header">🤖 AI Text Generator</p>', unsafe_allow_html=True)
    st.markdown(config.APP_DESCRIPTION)
    
    # Load models
    with st.spinner("Loading AI models... (This may take a minute on first run)"):
        sentiment_analyzer, text_generator = load_models()
    
    # Sidebar configuration
    st.sidebar.title("⚙️ Settings")
    
    # Manual sentiment override option
    use_manual_sentiment = st.sidebar.checkbox("Override Sentiment Detection", value=False)
    
    if use_manual_sentiment:
        manual_sentiment = st.sidebar.selectbox(
            "Select Sentiment:",
            ["positive", "negative", "neutral"]
        )
    
    # Text length selection
    length_option = st.sidebar.selectbox(
        "Output Length:",
        list(config.LENGTH_PRESETS.keys())
    )
    selected_length = config.LENGTH_PRESETS[length_option]
    
    # Advanced settings (collapsible)
    with st.sidebar.expander("🔧 Advanced Settings"):
        st.info("These settings affect text generation quality")
        st.write(f"**Temperature:** {config.TEMPERATURE}")
        st.write(f"**Top-K:** {config.TOP_K}")
        st.write(f"**Top-P:** {config.TOP_P}")
    
    # About section
    with st.sidebar.expander("ℹ️ About"):
        st.write("""
        **AI Text Generator** uses:
        - **DistilBERT** for sentiment analysis
        - **DistilGPT2** for text generation
        
        Created as an internship project demonstrating:
        - NLP & ML integration
        - Sentiment-aligned text generation
        - Web application development
        """)
    
    st.markdown("---")
    
    # Main input area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📝 Enter Your Prompt")
        user_prompt = st.text_area(
            "Type your prompt here:",
            height=120,
            placeholder="Example: Write about a beautiful sunset...",
            help="Enter any topic or prompt. The AI will detect its sentiment and generate matching text."
        )
    
    with col2:
        st.subheader("💡 Examples")
        if st.button("🌅 Beautiful Day"):
            user_prompt = "a beautiful sunny day at the beach"
            st.rerun()
        if st.button("😞 Bad Traffic"):
            user_prompt = "terrible traffic jams in the city"
            st.rerun()
        if st.button("📊 Climate Data"):
            user_prompt = "climate change statistics and trends"
            st.rerun()
    
    # Generate button
    generate_button = st.button("🚀 Generate Text", type="primary", use_container_width=True)
    
    # Main generation logic
    if generate_button:
        if not user_prompt or user_prompt.strip() == "":
            st.error("⚠️ Please enter a prompt before generating!")
        else:
            # Step 1: Sentiment Analysis
            with st.spinner("🔍 Analyzing sentiment..."):
                if use_manual_sentiment:
                    detected_sentiment = manual_sentiment
                    confidence = 1.0
                    st.info(f"Using manually selected sentiment: **{detected_sentiment.upper()}**")
                else:
                    sentiment_result = sentiment_analyzer.get_sentiment_with_details(user_prompt)
                    detected_sentiment = sentiment_result['label']
                    confidence = sentiment_result['confidence']
                    emoji = sentiment_result['emoji']
                    interpretation = sentiment_result['interpretation']
                    
                    # Display sentiment result
                    st.subheader("🎯 Detected Sentiment")
                    
                    sentiment_class = f"{detected_sentiment}-box"
                    st.markdown(
                        f'<div class="sentiment-box {sentiment_class}">'
                        f'<h2>{emoji} {detected_sentiment.upper()}</h2>'
                        f'<p>Confidence: {confidence:.1%} ({interpretation})</p>'
                        f'</div>',
                        unsafe_allow_html=True
                    )
            
            # Step 2: Text Generation
            with st.spinner(f"✨ Generating {detected_sentiment} text..."):
                generated_text = text_generator.generate(
                    user_prompt,
                    detected_sentiment,
                    selected_length
                )
            
            # Display generated text
            st.subheader("📄 Generated Text")
            st.markdown(
                f'<div class="output-box">'
                f'<p style="font-size: 1.1rem; line-height: 1.6;">{generated_text}</p>'
                f'</div>',
                unsafe_allow_html=True
            )
            
            # Additional info
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.metric("Sentiment", detected_sentiment.upper())
            with col_b:
                st.metric("Confidence", f"{confidence:.1%}")
            with col_c:
                st.metric("Word Count", len(generated_text.split()))
            
            # Download option
            st.download_button(
                label="💾 Download Generated Text",
                data=generated_text,
                file_name="generated_text.txt",
                mime="text/plain"
            )
            
            # Success message
            st.success("✅ Text generated successfully!")
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<p style='text-align: center; color: gray;'>"
        "Built with ❤️ using Streamlit, Transformers, and PyTorch | "
        "AI Text Generator v1.0"
        "</p>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()