from composio import App
from crewai_tools import ComposioTool
from crewai import Agent, Task


# tools = [ComposioTool.from_action(action=Action.GITHUB_ACTIVITY_STAR_REPO_FOR_AUTHENTICATED_USER)]
tools = ComposioTool.from_app(App.GITHUB, tags=["important"])

crewai_agent = Agent(
    role="Github Agent",
    goal="You take action on Github using Github APIs",
    backstory=(
        "You are AI agent that is responsible for taking actions on Github "
        "on users behalf. You need to take action on Github using Github APIs"
    ),
    verbose=True,
    tools=tools,
)

task = Task(
    description="Star a repo ASM313/Text-to-SQL",
    agent=crewai_agent,
    expected_output="if the star happened",
)

task.execute()


