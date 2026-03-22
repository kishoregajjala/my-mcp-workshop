from mcp.server import FastMCP
from strands import Agent
from strands_tools import http_request

# Example for Trip Planning Agent
mcp = FastMCP("Trip Planning Agent Server")

# For Trip Planning Agent
TRIP_PLANNING_SYSTEM_PROMPT = """
You are an expert trip planning agent that creates comprehensive travel itineraries.
Always provide detailed day-by-day itineraries with specific recommendations.
Include practical information like costs, timing, and local insights.
"""

# For Research Agent  
RESEARCH_SYSTEM_PROMPT = """
You are a travel research specialist with access to current information.
Provide accurate, detailed travel information with sources when possible.
"""

@mcp.tool(
    name="trip_planning_assistant",
    description="Create comprehensive travel itineraries and provide expert travel advice"
)
def trip_planning_assistant(query: str) -> str:
    """Create detailed travel plans and provide comprehensive travel advice."""
    
    # Enhanced query with specific requirements
    formatted_query = f"""
    Create a comprehensive travel plan for: {query}
    Include: itinerary, transportation, accommodation, dining, budget, cultural tips
    """
    
    try:
        trip_agent = Agent(
            model="global.anthropic.claude-sonnet-4-5-20250929-v1:0",
            system_prompt=TRIP_PLANNING_SYSTEM_PROMPT,
            tools=[http_request]
        )
        
        response = trip_agent(formatted_query)
        # Add timestamp to response
        return f"{str(response)}\n\n---\n*Generated on {datetime.now().strftime('%Y-%m-%d at %H:%M')}*"
        
    except Exception as e:
        return f"Error creating travel plan: {str(e)}"

@mcp.tool(
    name="travel_research_assistant", 
    description="Research specific travel topics and answer travel questions"
)
def travel_research_assistant(query: str) -> str:
    """Research travel information and answer specific travel questions."""
    
    formatted_query = f"Research and provide detailed information about: {query}"
    
    try:
        research_agent = Agent(
            model="global.anthropic.claude-sonnet-4-5-20250929-v1:0",
            system_prompt=RESEARCH_SYSTEM_PROMPT,
            tools=[http_request]
        )
        
        return str(research_agent(formatted_query))
        
    except Exception as e:
        return f"Error researching travel information: {str(e)}"


if __name__ == "__main__":
    print("Starting Strands Agent MCP Server...")
    mcp.run(transport="stdio") 