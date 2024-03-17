import os
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

load_dotenv()
class Reference:
    """
    A class to store the previous response from the llm.
    """
    def __init__(self) -> None:
        self.response = ""



# Create a reference object to store the previous response
reference = Reference()


# Initialize bot and dispatcher
bot = Bot(token= os.getenv("TELEGRAM_TOKEN"))
dispatcher = Dispatcher(bot)


#2
def clear_past():
    """
    A function to clear the previous conversation and context.
    """
    reference.response = ""



@dispatcher.message_handler(commands=['start'])
async def welcome(message: types.Message):
    """
    A handler to welcome the user and clear past conversation and context.
    """
    clear_past()
    await message.reply("Hello! \nI'm a Telegram bot.\n How can I assist you?")



@dispatcher.message_handler(commands=['clear'])
async def clear(message: types.Message):
    """
    A handler to clear the previous conversation and context.
    """
    clear_past()
    await message.reply("I've cleared the past conversation and context.")




@dispatcher.message_handler(commands=['help'])
async def helper(message: types.Message):
    """
    A handler to display the help menu.
    """
    help_command = """
    Hi There, I'm a Telegram bot! Please follow these commands - 
    /start - to start the conversation
    /clear - to clear the past conversation and context.
    /help - to get this help menu.
    I hope this helps. :)
    """
    await message.reply(help_command)

class LOAD_MODEL:
    model = None
    
    @classmethod
    def load_model(cls, model_name: str):
        if cls.model is None:
            from chat_model.huggingface import HuggingFaceLlm
            cls.model = HuggingFaceLlm.load_model(model_name)
        return cls.model



@dispatcher.message_handler()
async def llm(message: types.Message):
    """
    A handler to process the user's input and generate a response using the HF API.
    """
    print(f">>> USER: \n\t{message.text}")
    model = LOAD_MODEL.load_model("HuggingFaceH4/zephyr-7b-beta")
    reference.response = model(prompt=message.text, reference_response=reference.response)  # Pass reference_response
    print(f">>> model: \n\t{reference.response}")
    await bot.send_message(chat_id = message.chat.id, text = reference.response)




if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)
