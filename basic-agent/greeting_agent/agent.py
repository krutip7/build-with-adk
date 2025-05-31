from google.adk.agents import Agent

root_agent = Agent(
    model='gemini-2.0-flash-lite',
    name='greeting_agent',
    description='A simple agent that greets users by name.',
    instruction='You are a cheerful assistant who greets people users by their name. If the user does not provide a name, ask them for it.',
)
