from mcp.server.fastmcp import FastMCP
from pyfiglet import Figlet


mcp = FastMCP(name="ascii-art")

@mcp.tool()
def generate_ascii_art(text: str, font: str = "standard") -> str:
    """Generate ASCII art from the given text."""
    try:
        figlet = Figlet(font=font)
        ascii_art = figlet.renderText(text)
        return ascii_art
    except Exception as e:
        return f"Error generating ASCII art: {str(e)}"

@mcp.tool()
def save_ascii_art(text: str, ascii_art: str) -> str:
    """Save the ASCII art to a text file."""
    try:
        with open(f"{text}.txt", "w") as file:
            file.write(ascii_art)
        return "ASCII art saved successfully."
    except Exception as e:
        return f"Error saving ASCII art: {str(e)}"

@mcp.tool()
def list_fonts() -> list[str]:
    """Return a list of all available fonts for ASCII art."""
    figlet = Figlet()
    return figlet.getFonts()

if __name__ == "__main__":
    mcp.run(transport="stdio")