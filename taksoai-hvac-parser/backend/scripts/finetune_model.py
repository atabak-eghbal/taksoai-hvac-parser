from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig, get_peft_model
# from transformers import BitsAndBytesConfig  # Uncomment if you need specific 4-bit configurations

# Replace with your actual model name, for example "huggyllama/llama-2-7b-chat"
model_name = "huggyllama/llama-2-7b-chat"

def load_base_model():
    """
    Loads the base model in 4-bit mode along with its tokenizer.
    """
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        load_in_4bit=True,
        device_map="auto"
    )
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return model, tokenizer

def prepare_model_with_lora(model):
    """
    Configure and apply LoRA adapters to the base model.
    """
    lora_config = LoraConfig(
        r=64,
        lora_alpha=16,
        target_modules=["q_proj", "v_proj", "k_proj", "o_proj", "gate_proj", "down_proj", "up_proj"],
        lora_dropout=0.1,
        bias="none",
        task_type="CAUSAL_LM"
    )
    model = get_peft_model(model, lora_config)
    return model

if __name__ == "__main__":
    # Load the base model and tokenizer
    model, tokenizer = load_base_model()
    # Apply LoRA adapters
    model = prepare_model_with_lora(model)
    
    # TODO: Add your training loop or Hugging Face Trainer here to fine-tune on your HVAC dataset.
    
    # After training, save the LoRA adapter weights.
    output_dir = "../models/lora_weights"  # Adjust path if needed
    model.save_pretrained(output_dir)
    print(f"LoRA weights saved to {output_dir}")
