from langchain.llms import AI21
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType


load_dotenv()


def generate_pet_name(animal_type, pet_color):

    prompt_template_name = PromptTemplate(
        input_variables=["animal_type", "pet_color"],
        template="I have a {animal_type} pet and I want a cool name for it, it is {pet_color} in color. Suggest me five cool names for my pet"
    )

    llm = AI21(temperature=0.7)

    name_chain = LLMChain(prompt=prompt_template_name,
                          llm=llm, output_key="pet_name")

    name = name_chain({'animal_type': animal_type, "pet_color": pet_color})

    return name


def langchain_agent():

    llm = AI21(temperature=0.1)

    tools = load_tools(["wikipedia", "llm-math"], llm=llm)

    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    result = agent.run(
        "What is the average age of a dog? Multiply the age by 3"
    )

    print(result)


if __name__ == "__main__":
    langchain_agent()
