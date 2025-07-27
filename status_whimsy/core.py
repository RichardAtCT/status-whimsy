"""
Core implementation of the status_whimsy library.
"""

import os
from typing import Literal, Optional

from anthropic import Anthropic


class StatusWhimsy:
    """Generate whimsical status updates using Claude Haiku 3."""

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the StatusWhimsy client.

        Args:
            api_key: Anthropic API key. If not provided, looks for ANTHROPIC_API_KEY env var.
        """
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError(
                "API key must be provided or set as ANTHROPIC_API_KEY environment variable"
            )

        self.client = Anthropic(api_key=self.api_key)
        self.model = "claude-3-haiku-20240307"

    def generate(
        self,
        status: str,
        whimsicalness: int = 5,
        length: Literal["short", "medium", "long"] = "short",
    ) -> str:
        """
        Generate a whimsical version of the given status.

        Args:
            status: The original status message to transform
            whimsicalness: Level of whimsy from 1-10 (1=professional, 10=extremely whimsical)
            length: Desired length of the output ("short", "medium", or "long")

        Returns:
            A whimsical version of the status message
        """
        if not 1 <= whimsicalness <= 10:
            raise ValueError("Whimsicalness must be between 1 and 10")

        length_guidance = {"short": "10-20 words", "medium": "20-40 words", "long": "40-60 words"}

        whimsy_descriptions = {
            1: "professional and straightforward",
            2: "slightly friendly",
            3: "casually friendly",
            4: "lightly playful",
            5: "moderately playful and fun",
            6: "quite playful with personality",
            7: "very whimsical and creative",
            8: "highly whimsical with metaphors",
            9: "extremely whimsical and imaginative",
            10: "maximum whimsy with wild creativity",
        }

        whimsy_desc = whimsy_descriptions[whimsicalness]
        prompt = f"""Transform this status update into a {whimsy_desc} version.

Original status: {status}

Requirements:
- Keep it {length_guidance[length]}
- Maintain the core meaning
- Add personality according to whimsicalness level {whimsicalness}
- Make it engaging but still informative

Respond with ONLY the transformed status, no explanations."""

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=150,
                temperature=0.7 + (whimsicalness * 0.03),  # Scale temperature with whimsy
                messages=[{"role": "user", "content": prompt}],
            )

            # Handle the response content properly
            content = response.content[0]
            if hasattr(content, "text"):
                return content.text.strip()
            else:
                raise Exception("Unexpected response format from API")

        except Exception as e:
            raise Exception(f"Failed to generate whimsical status: {str(e)}")

    def batch_generate(
        self,
        statuses: list[str],
        whimsicalness: int = 5,
        length: Literal["short", "medium", "long"] = "short",
    ) -> list[str]:
        """
        Generate whimsical versions for multiple status messages.

        Args:
            statuses: List of status messages to transform
            whimsicalness: Level of whimsy from 1-10
            length: Desired length of outputs

        Returns:
            List of whimsical status messages
        """
        return [self.generate(status, whimsicalness, length) for status in statuses]


# Convenience function for one-off usage
def whimsify(
    status: str,
    api_key: Optional[str] = None,
    whimsicalness: int = 5,
    length: Literal["short", "medium", "long"] = "short",
) -> str:
    """
    Quick function to whimsify a single status without creating a client.

    Args:
        status: The status message to transform
        api_key: Anthropic API key (optional if set in environment)
        whimsicalness: Level of whimsy from 1-10
        length: Desired length of output

    Returns:
        A whimsical version of the status
    """
    whimsy = StatusWhimsy(api_key)
    return whimsy.generate(status, whimsicalness, length)


# Example usage
if __name__ == "__main__":
    # Example statuses
    examples = [
        "Server is running",
        "Database backup complete",
        "User authentication failed",
        "System update in progress",
        "Memory usage at 85%",
    ]

    print("Status Whimsy Examples")
    print("=" * 50)

    # Note: You'll need to set your API key
    # whimsy = StatusWhimsy()

    for status in examples:
        print(f"\nOriginal: {status}")
        print("Whimsical versions:")
        for level in [1, 5, 10]:
            # result = whimsy.generate(status, whimsicalness=level, length="short")
            # print(f"  Level {level}: {result}")
            print(f"  Level {level}: [Would generate with API key]")
