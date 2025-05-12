import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load model and tokenizer once at startup for efficiency
MODEL_NAME = "microsoft/DialoGPT-medium"
try:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
except Exception as e:
    raise RuntimeError(f"Failed to load Hugging Face model: {e}")


def create_prompt(user_input, mood="default"):
    """Create a tailored prompt based on user input and mood."""
    mood_prompts = {
        "sarcastic": "Respond with a sharp, witty, and sarcastic tone to: ",
        "enthusiastic": "Respond with high energy and enthusiasm to: ",
        "serious": "Respond with a formal and serious tone to: ",
        "default": "",
    }
    prefix = mood_prompts.get(mood.lower(), "")
    return f"{prefix}{user_input}"


def get_ai_response(user_input, mood):
    """Generate an AI response using the Hugging Face model."""
    if not user_input:
        return "No input provided."

    prompt = create_prompt(user_input, mood)
    try:
        input_ids = tokenizer.encode(prompt + tokenizer.eos_token, return_tensors="pt")
        response_ids = model.generate(
            input_ids,
            max_length=1000,
            pad_token_id=tokenizer.eos_token_id,
            do_sample=True,
            temperature=0.7,
            top_k=50,
            top_p=0.95,
        )
        response = tokenizer.decode(
            response_ids[:, input_ids.shape[-1] :][0], skip_special_tokens=True
        )
        return response.strip() or "Sorry, I have nothing to say!"
    except Exception as e:
        return f"Error generating response: {e}"
