"""
Custom MCP Server - [Your Server Name]
Built during AWS Workshop: Everyday Productivity Accelerators
"""
from mcp.server import FastMCP
from typing import Dict
from datetime import datetime

# Change the server name
mcp = FastMCP("Temperature Conversion Server")

# Implement first tool
@mcp.tool(description="Convert Fahrenheit to Celsius")
def fahrenheit_to_celsius(temp_f: str) -> Dict:
    """
    Convert temperature from Fahrenheit to Celsius.
    
    Args:
        temp_f: Temperature in Fahrenheit (as string)
    
    Returns:
        Dictionary with converted temperature
    """
    try:
        # Parse the temperature
        fahrenheit = float(temp_f.strip())
        
        # Convert to Celsius
        celsius = (fahrenheit - 32) * 5/9
        
        return {
            "success": True,
            "fahrenheit": fahrenheit,
            "celsius": round(celsius, 2),
            "message": f"{fahrenheit}°F = {round(celsius, 2)}°C",
            "timestamp": datetime.now().isoformat()
        }
        
    except ValueError:
        return {
            "success": False,
            "error": "Invalid temperature format. Please provide a number.",
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }

# Add more functions as needed...

if __name__ == "__main__":
    print(f"🚀 Starting {mcp.name}...")
    mcp.run(transport="stdio")