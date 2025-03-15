import asyncio
import openai 
from agents import Agent, Runner, set_default_openai_key
import os

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
print(f"OPENAI_API_KEY {OPENAI_API_KEY}")
set_default_openai_key(OPENAI_API_KEY)

# get OPEANAI_API_KEY from codespaces secrets

    # This is the default and can be omitted

if not OPENAI_API_KEY :
    raise ValueError("OPENAI_API_KEY environment variable not set")


async def main():
    agent = Agent(
        name="Assistant",
        instructions="You only respond in haikus.",
    )

    result = await Runner.run(agent, "Tell me about recursion in programming.")
    print(result.final_output)
    # Function calls itself,
    # Looping in smaller pieces,
    # Endless by design.


if __name__ == "__main__":
    asyncio.run(main())
