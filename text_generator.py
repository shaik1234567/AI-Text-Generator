"""
Text Generator Module
Generates sentiment-aligned text based on prompts and detected sentiment
"""

from transformers import pipeline, set_seed
import config
import random

class TextGenerator:
    """
    Class to generate text aligned with specific sentiment
    """
    
    def __init__(self):
        """
        Initialize the text generation pipeline
        """
        print("Loading text generation model...")
        try:
            # Load pre-trained text generation model
            self.generator = pipeline(
                "text-generation",
                model=config.TEXT_GENERATION_MODEL,
                device=-1  # Use CPU (use 0 for GPU)
            )
            print("✓ Text generation model loaded successfully!")
            
            # Set random seed for reproducibility (optional)
            set_seed(42)
            
        except Exception as e:
            print(f"Error loading text generation model: {e}")
            raise
    
    def generate(self, prompt, sentiment, length=None):
        """
        Generate text based on prompt and sentiment
        
        Args:
            prompt (str): User's input prompt
            sentiment (str): Detected sentiment (positive/negative/neutral)
            length (int): Desired length of generated text
            
        Returns:
            str: Generated text
        """
        if not prompt or prompt.strip() == "":
            return "Error: Empty prompt provided."
        
        # Use default length if not specified
        if length is None:
            length = config.DEFAULT_MAX_LENGTH
        
        # Ensure length is within bounds
        length = max(config.MIN_LENGTH, min(length, config.MAX_LENGTH))
        
        try:
            # Create sentiment-aligned prompt
            enhanced_prompt = self._create_sentiment_prompt(prompt, sentiment)
            
            # Generate text
            result = self.generator(
                enhanced_prompt,
                max_length=length,
                num_return_sequences=1,
                temperature=config.TEMPERATURE,
                top_k=config.TOP_K,
                top_p=config.TOP_P,
                do_sample=True,
                pad_token_id=50256  # GPT2 pad token
            )
            
            # Extract generated text
            generated_text = result[0]['generated_text']
            
            # Clean up the output (remove the prompt prefix)
            cleaned_text = self._clean_output(generated_text, enhanced_prompt)
            
            return cleaned_text
            
        except Exception as e:
            print(f"Error during text generation: {e}")
            return f"Error generating text: {str(e)}"
    
    def _create_sentiment_prompt(self, prompt, sentiment):
        """
        Create a sentiment-aligned prompt using templates
        
        Args:
            prompt (str): Original user prompt
            sentiment (str): Target sentiment
            
        Returns:
            str: Enhanced prompt with sentiment guidance
        """
        sentiment = sentiment.lower()
        
        # Get template for the sentiment
        template = config.PROMPT_TEMPLATES.get(sentiment, config.PROMPT_TEMPLATES["neutral"])
        
        # Create enhanced prompt
        enhanced_prompt = f"{template['prefix']}{prompt}. "
        
        # Add a style word to guide generation
        style_word = random.choice(template['style_words'])
        enhanced_prompt += f"This is {style_word}. "
        
        return enhanced_prompt
    
    def _clean_output(self, generated_text, prompt_prefix):
        """
        Clean the generated output
        
        Args:
            generated_text (str): Raw generated text
            prompt_prefix (str): The prompt that was prepended
            
        Returns:
            str: Cleaned text
        """
        # Remove the prompt prefix if it exists
        if generated_text.startswith(prompt_prefix):
            cleaned = generated_text[len(prompt_prefix):].strip()
        else:
            cleaned = generated_text.strip()
        
        # Basic cleanup
        cleaned = cleaned.replace("  ", " ")  # Remove double spaces
        
        # Ensure it ends with proper punctuation
        if cleaned and cleaned[-1] not in ['.', '!', '?']:
            cleaned += '.'
        
        return cleaned
    
    def generate_multiple(self, prompt, sentiment, length=None, num_outputs=3):
        """
        Generate multiple variations of text
        
        Args:
            prompt (str): User's input prompt
            sentiment (str): Target sentiment
            length (int): Desired length
            num_outputs (int): Number of variations to generate
            
        Returns:
            list: List of generated texts
        """
        outputs = []
        
        for i in range(num_outputs):
            # Add slight randomness by adjusting seed
            set_seed(42 + i)
            text = self.generate(prompt, sentiment, length)
            outputs.append(text)
        
        return outputs


# Test function (for standalone testing)
if __name__ == "__main__":
    # Test the text generator
    generator = TextGenerator()
    
    test_cases = [
        ("sunny days", "positive", 100),
        ("traffic jams", "negative", 100),
        ("climate change", "neutral", 100)
    ]
    
    print("\n" + "="*50)
    print("Testing Text Generator")
    print("="*50 + "\n")
    
    for prompt, sentiment, length in test_cases:
        print(f"Prompt: {prompt}")
        print(f"Sentiment: {sentiment}")
        print(f"Length: {length}")
        print("\nGenerated Text:")
        
        generated = generator.generate(prompt, sentiment, length)
        print(generated)
        print("\n" + "-"*50 + "\n")