import importlib
import logging
import os
from typing import Any
from langchain_community.llms import HuggingFaceHub
from langchain_community.chat_models.huggingface import ChatHuggingFace
from langchain.schema import HumanMessage, SystemMessage

logger = logging.getLogger(__name__)

class HuggingFaceLlm():
    def __init__(self, model: Any):
        self.model = model

    @classmethod
    def load_model(cls, model_name: str) -> 'HuggingFaceLlm':
        if "HUGGINGFACEHUB_API_TOKEN" not in os.environ:
            raise ValueError("Please set the HUGGINGFACEHUB_API_TOKEN environment variable.")
        
        try:
            importlib.import_module("huggingface_hub")
            cls.login_with_token()
        except ModuleNotFoundError:
            raise ModuleNotFoundError(
                "The required dependencies for HuggingFaceHub are not installed."
                'Please install with `pip install --upgrade "huggingface-hub"'
            ) from None  

        llm = HuggingFaceHub(
            repo_id=model_name,
            task="text-generation",
            model_kwargs={
                "max_new_tokens": 512,
                "top_k": 30,
                "temperature": 0.1,
                "repetition_penalty": 1.03,
            },
        )
        return cls(llm)

    @staticmethod
    def login_with_token():
        """
        Log in to the Hugging Face Hub using the provided API token.
        """
        if "HUGGINGFACEHUB_API_TOKEN" in os.environ:
            try:
                from huggingface_hub import login
                login(os.environ["HUGGINGFACEHUB_API_TOKEN"])
            except ImportError:
                pass

    def predict(self, query: str, reference_response:str) -> str:
        messages = [
            SystemMessage(content= reference_response),
            HumanMessage(content=query),
        ]
        chat_model = ChatHuggingFace(llm=self.model)
        op = chat_model(messages)
        response = op.content.replace(chat_model._to_chat_prompt(messages), "")
        return response

    def __call__(self, prompt: str, reference_response:str) -> str:
        return self.predict(prompt, reference_response)  # Pass reference_response to predict method
