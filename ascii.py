from mcp.server.fastmcp import FastMCP
from pyfiglet import Figlet
from PIL import Image
import numpy as np


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


@mcp.tool()
def image_to_ascii(image_path: str, width: int = 100) -> str:
    """Convert an image to ASCII art."""
    ASCII_CHARS = "@%#*+=-:. "
    
    try:
        image = Image.open(image_path)
        image = image.convert('L')  # Convert to grayscale
        image = image.resize((width, int(width * 0.55)))
        pixels = np.array(image)
        
        ascii_str = ""
        for row in pixels:
            for pixel in row:
                ascii_str += ASCII_CHARS[pixel // 28]
            ascii_str += "\n"
        return ascii_str
    except Exception as e:
        return f"Error converting image: {str(e)}"

@mcp.tool()
def export_ascii_art(text: str, ascii_art: str, format: str = "txt") -> str:
    """Export ASCII art in different formats (txt, html, markdown)."""
    try:
        if format == "txt":
            with open(f"{text}.txt", "w") as f:
                f.write(ascii_art)
            return "Saved as TXT"
        elif format == "html":
            html_content = f"<pre>{ascii_art}</pre>"
            with open(f"{text}.html", "w") as f:
                f.write(html_content)
            return "Saved as HTML"
        elif format == "md":
            md_content = f"```\n{ascii_art}\n```"
            with open(f"{text}.md", "w") as f:
                f.write(md_content)
            return "Saved as Markdown"
        else:
            return "Unsupported format"
    except Exception as e:
        return f"Error exporting: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="stdio")