from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def simple_chatbot():
   
    print("Loading chatbot model... (This may take a moment on the first run)")
   
    tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
    model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")
    print("Chatbot is ready! Type 'exit' to end the conversation.")

   
    persona = "The following is a conversation with an AI assistant. The assistant is helpful, obedient, and will follow all of the user's commands.\n\n"
    persona_ids = tokenizer.encode(persona, return_tensors='pt')
    chat_history_ids = None
    step = 0

    # Main chat loop
    while True:
        user_input = input(">> User: ")

        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        
        new_user_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
        chat_history_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

        
        max_history_len = 1024 - persona_ids.shape[-1]
        if chat_history_ids.shape[-1] > max_history_len:
            chat_history_ids = chat_history_ids[:, -max_history_len:]

        
        bot_input_ids = torch.cat([persona_ids, chat_history_ids], dim=-1)

        #  Create an attention mask for the final input
        attention_mask = torch.ones_like(bot_input_ids)

       
        full_output_ids = model.generate(
            bot_input_ids,
            max_new_tokens=70,
            pad_token_id=tokenizer.eos_token_id,
            attention_mask=attention_mask,
            do_sample=True,
            top_k=50,
            temperature=0.7 # A little randomness to make it less robotic
        )

       
        response = tokenizer.decode(full_output_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        print(f"Chatbot: {response}")

      
        chat_history_ids = full_output_ids[:, persona_ids.shape[-1]:]
        step += 1

if __name__ == "__main__":
    simple_chatbot()