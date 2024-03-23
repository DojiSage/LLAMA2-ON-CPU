from langchain import PromptTemplate
from langchain import LLMChain
from langchain.llms import CTransformers
from src.helper import *

B_INST, E_INST = "[INST]", "[/INST]"
B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"

SYSTEM_PROMPT = B_SYS + DEFAULT_SYSTEM_PROMPT + E_SYS

instruction = "give a summary of the movie: \n\n {text}"

prompt_template = B_INST + SYSTEM_PROMPT + instruction + E_INST

prompt = PromptTemplate(template=prompt_template, input_variable=["text"])

llm = CTransformers(
    model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",
    model_type="llama",
    config={"max_new_tokens": 128, "temperature": 0.01},
)


LLM_Chain = LLMChain(prompt=prompt, llm=llm)

print(LLM_Chain.run("Dune"))
