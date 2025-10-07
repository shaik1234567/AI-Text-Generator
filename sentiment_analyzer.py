"""
Sentiment Analyzer Module
Detects sentiment (positive/negative/neutral) from input text
"""

from transformers import pipeline
import config

class SentimentAnalyzer:
    """
    Class to analyze sentiment of input text using pre-trained models
    """
    
    def __init__(self):
        """
        Initialize the sentiment analysis pipeline
        """
        print("Loading sentiment analysis model...")
        try:
            # Load pre-trained sentiment analysis model
            self.classifier = pipeline(
                "sentiment-analysis",
                model=config.SENTIMENT_MODEL,
                device=-1  # Use CPU (use 0 for GPU)
            )
            print("✓ Sentiment model loaded successfully!")
        except Exception as e:
            print(f"Error loading sentiment model: {e}")
            raise
    
    def analyze(self, text):
        """
        Analyze sentiment of input text
        
        Args:
            text (str): Input text to analyze
            
        Returns:
            dict: Contains 'label' (sentiment) and 'confidence' (score)
        """
        if not text or text.strip() == "":
            return {
                "label": "neutral",
                "confidence": 0.0,
                "error": "Empty input"
            }
        
        try:
            # Get sentiment prediction
            result = self.classifier(text)[0]
            
            # Map model output to our labels
            label = result['label'].upper()
            confidence = result['score']
            
            # Convert to our sentiment format
            if label == "POSITIVE":
                sentiment = "positive"
            elif label == "NEGATIVE":
                sentiment = "negative"
            else:
                sentiment = "neutral"
            
            return {
                "label": sentiment,
                "confidence": confidence
            }
            
        except Exception as e:
            print(f"Error during sentiment analysis: {e}")
            return {
                "label": "neutral",
                "confidence": 0.0,
                "error": str(e)
            }
    
    def get_sentiment_with_details(self, text):
        """
        Get detailed sentiment analysis with interpretation
        
        Args:
            text (str): Input text to analyze
            
        Returns:
            dict: Detailed sentiment information
        """
        result = self.analyze(text)
        
        # Add interpretation
        confidence = result.get('confidence', 0)
        label = result.get('label', 'neutral')
        
        if confidence > 0.9:
            interpretation = "Very confident"
        elif confidence > 0.7:
            interpretation = "Confident"
        elif confidence > 0.5:
            interpretation = "Moderately confident"
        else:
            interpretation = "Low confidence"
        
        result['interpretation'] = interpretation
        result['emoji'] = self._get_emoji(label)
        
        return result
    
    def _get_emoji(self, sentiment):
        """
        Get emoji representation for sentiment
        
        Args:
            sentiment (str): Sentiment label
            
        Returns:
            str: Emoji representing the sentiment
        """
        emoji_map = {
            "positive": "😊",
            "negative": "😞",
            "neutral": "😐"
        }
        return emoji_map.get(sentiment, "😐")


# Test function (for standalone testing)
if __name__ == "__main__":
    # Test the sentiment analyzer
    analyzer = SentimentAnalyzer()
    
    test_texts = [
        "I love this wonderful day!",
        "This is terrible and disappointing.",
        "The weather is normal today."
    ]
    
    print("\n" + "="*50)
    print("Testing Sentiment Analyzer")
    print("="*50 + "\n")
    
    for text in test_texts:
        result = analyzer.get_sentiment_with_details(text)
        print(f"Text: {text}")
        print(f"Sentiment: {result['emoji']} {result['label'].upper()}")
        print(f"Confidence: {result['confidence']:.2%}")
        print(f"Interpretation: {result['interpretation']}")
        print("-"*50)