#!/usr/bin/env python3
"""
Basic usage examples for status_whimsy.

Make sure to set your ANTHROPIC_API_KEY environment variable before running.
"""

import os
from status_whimsy import StatusWhimsy, whimsify


def main():
    # Check for API key
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Please set your ANTHROPIC_API_KEY environment variable")
        print("export ANTHROPIC_API_KEY='your-api-key'")
        return

    print("Status Whimsy Examples")
    print("=" * 50)

    # Initialize the client
    whimsy = StatusWhimsy()

    # Example statuses
    statuses = [
        "Server is running",
        "Database backup complete",
        "User authentication failed",
        "System update in progress",
        "Memory usage at 85%"
    ]

    # Example 1: Different whimsy levels
    print("\n1. Different Whimsy Levels")
    print("-" * 30)
    status = "Server is running"
    for level in [1, 5, 10]:
        result = whimsy.generate(status, whimsicalness=level)
        print(f"Level {level}: {result}")

    # Example 2: Different lengths
    print("\n2. Different Output Lengths")
    print("-" * 30)
    status = "Database backup complete"
    for length in ["short", "medium", "long"]:
        result = whimsy.generate(status, whimsicalness=7, length=length)
        print(f"{length.capitalize()}: {result}")

    # Example 3: Batch processing
    print("\n3. Batch Processing")
    print("-" * 30)
    batch_results = whimsy.batch_generate(
        statuses[:3],
        whimsicalness=6,
        length="short"
    )
    for original, whimsical in zip(statuses[:3], batch_results):
        print(f"Original: {original}")
        print(f"Whimsical: {whimsical}")
        print()

    # Example 4: Using the convenience function
    print("\n4. Using whimsify() Function")
    print("-" * 30)
    result = whimsify("System is healthy", whimsicalness=8)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()