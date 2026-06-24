from rich.console import Console
from rich.text import Text


def print_llm_result(prompt, response):
    console = Console()

    console.print(Text("USER PROMPT:", style="bold green"))
    console.print(Text(prompt, style="bold blue"), end="\n\n")

    console.print(Text("LLM RESPONSE:", style="bold green"))
    console.print(Text(response.content, style="bold blue"), end="\n\n")

    usage = response.response_metadata.get("token_usage")

    if usage:
        input_tokens = usage.get("prompt_tokens", 0)
        output_tokens = usage.get("completion_tokens", 0)
        total_tokens = usage.get("total_tokens", 0)
    else:
        usage = getattr(response, "usage_metadata", {}) or {}
        input_tokens = usage.get("input_tokens", 0)
        output_tokens = usage.get("output_tokens", 0)
        total_tokens = usage.get("total_tokens", 0)

    console.print(
        f"[bold white]Input tokens:[/bold white] [bright_black]{input_tokens}[/bright_black]"
    )
    console.print(
        f"[bold white]Output tokens:[/bold white] [bright_black]{output_tokens}[/bright_black]"
    )
    console.print(
        f"[bold white]Total tokens:[/bold white] [bright_black]{total_tokens}[/bright_black]"
    )

    console.print(f"[yellow]{'-' * 50}[/yellow]")