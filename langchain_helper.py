from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain
from dotenv import load_dotenv
load_dotenv()

    
llm = OpenAI(temperature=0.9)



def generate_name_and_tagline(industry):
    #Sequential Chain
    #Chain1: Startup name
    prompt_template_name = PromptTemplate(
        input_variables = ['industry'],
        template= "Suggest one name for my startup which is based on {industry} industry"
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="startup_name")

    #Chain2: Startup tagline
    prompt_template_tagline = PromptTemplate(
        input_variables = ['startup_name'],
        template= "Suggest me an short tagline for my startup {startup_name} using relevent rhyming words"
    )

    tagline_chain = LLMChain(llm=llm, prompt=prompt_template_tagline,  output_key="startup_tagline")
    
    # ---------------------
    
    chain = SequentialChain(
    chains = [name_chain, tagline_chain],
    input_variables = ['industry'],
    output_variables= ['startup_name', 'startup_tagline']
    )

    response = chain.invoke({'industry': industry})
    
    return response

    
# if __name__ == "__main__":
#     print(generate_name_and_tagline('Tech'))