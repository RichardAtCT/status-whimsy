# Status Whimsy

A lightweight Python library that transforms boring status updates into delightful, whimsical messages using Claude Haiku 3.

## Features

- 🎨 Transform plain status messages into engaging updates
- 🎚️ Adjustable whimsy levels (1-10)
- 📏 Configurable output length (short, medium, long)
- 🚀 Simple API with both class-based and functional interfaces
- 🔧 Batch processing support
- 🌡️ Dynamic temperature scaling based on whimsy level

## Installation

```bash
pip install status-whimsy
```

## Quick Start

```python
from status_whimsy import StatusWhimsy

# Initialize with your Anthropic API key
whimsy = StatusWhimsy(api_key="your-api-key")

# Transform a boring status
result = whimsy.generate(
    "Server is running",
    whimsicalness=7,
    length="short"
)
print(result)
# Output: "The server is dancing merrily in the digital clouds! 🎉"
```

## Usage

### Basic Usage

```python
from status_whimsy import StatusWhimsy

# Initialize the client
whimsy = StatusWhimsy()  # Uses ANTHROPIC_API_KEY env variable

# Generate whimsical status updates
update = whimsy.generate("Database backup complete", whimsicalness=5)
```

### One-off Usage

```python
from status_whimsy import whimsify

# Quick transformation without creating a client
result = whimsify("User logged in", whimsicalness=8, length="medium")
```

### Batch Processing

```python
statuses = [
    "Server is running",
    "Database backup complete",
    "User authentication failed"
]

whimsical_updates = whimsy.batch_generate(
    statuses,
    whimsicalness=6,
    length="short"
)
```

## Configuration

### API Key

Set your Anthropic API key in one of two ways:

1. Environment variable:
   ```bash
   export ANTHROPIC_API_KEY="your-api-key"
   ```

2. Pass directly to the constructor:
   ```python
   whimsy = StatusWhimsy(api_key="your-api-key")
   ```

### Whimsy Levels

- **1**: Professional and straightforward
- **2**: Slightly friendly
- **3**: Casually friendly
- **4**: Lightly playful
- **5**: Moderately playful and fun
- **6**: Quite playful with personality
- **7**: Very whimsical and creative
- **8**: Highly whimsical with metaphors
- **9**: Extremely whimsical and imaginative
- **10**: Maximum whimsy with wild creativity

### Output Lengths

- **short**: 10-20 words
- **medium**: 20-40 words
- **long**: 40-60 words

## Examples

```python
from status_whimsy import StatusWhimsy

whimsy = StatusWhimsy()

# Professional (Level 1)
whimsy.generate("Server is running", whimsicalness=1)
# "Server operational and functioning normally."

# Moderate whimsy (Level 5)
whimsy.generate("Server is running", whimsicalness=5)
# "The server is humming along happily, serving requests with a smile!"

# Maximum whimsy (Level 10)
whimsy.generate("Server is running", whimsicalness=10)
# "The digital dragon awakens, breathing binary fire across the realm of electrons, ready to grant your computational wishes!"
```

## API Reference

### StatusWhimsy Class

#### `__init__(api_key: Optional[str] = None)`
Initialize the StatusWhimsy client.

#### `generate(status: str, whimsicalness: int = 5, length: Literal["short", "medium", "long"] = "short") -> str`
Generate a whimsical version of the given status.

#### `batch_generate(statuses: list[str], whimsicalness: int = 5, length: Literal["short", "medium", "long"] = "short") -> list[str]`
Generate whimsical versions for multiple status messages.

### Function

#### `whimsify(status: str, api_key: Optional[str] = None, whimsicalness: int = 5, length: Literal["short", "medium", "long"] = "short") -> str`
Quick function to whimsify a single status without creating a client.

## API Costs

This library uses Claude Haiku 3, which offers extremely affordable pricing:

### Claude Haiku 3 Pricing (as of January 2025)
- **Input tokens**: $0.25 per million tokens
- **Output tokens**: $1.25 per million tokens

### Cost Per Status Update

**Token Estimation:**
- Input tokens (your prompt + system instructions): ~150-200 tokens
- Output tokens (generated status):
  - Short (10-20 words): ~15-30 tokens
  - Medium (20-40 words): ~30-60 tokens
  - Long (40-60 words): ~60-90 tokens

**Cost Calculation:**
Per single status update:
- Input cost: 200 tokens × $0.00000025 = $0.00005
- Output cost (short): 30 tokens × $0.00000125 = $0.0000375
- **Total per call: ~$0.00009** (less than 1/100th of a cent)

### Practical Examples

| Usage Volume | Approximate Cost |
|--------------|------------------|
| 100 status updates | $0.009 (less than 1¢) |
| 1,000 status updates | $0.09 (9¢) |
| 10,000 status updates | $0.90 (90¢) |
| 100,000 status updates | $9.00 |

### Example Monthly Cost
If your application generates 100 status updates per hour, 24/7:
- 100 × 24 × 30 = 72,000 updates/month
- **Cost: ~$6.48/month**

### Cost Optimization Tips
1. **Batch processing**: The `batch_generate()` method is more efficient for multiple statuses
2. **Shorter outputs**: Use `length="short"` to minimize output tokens
3. **Cache common statuses**: Store frequently used transformations locally

The library is extremely cost-effective due to Haiku's low pricing and the minimal token usage for status updates.

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/RichardAtCT/status-whimsy.git
cd status-whimsy

# Install in development mode
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

### Code Style

```bash
# Format code
black status_whimsy

# Sort imports
isort status_whimsy

# Type checking
mypy status_whimsy
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Anthropic's Claude API](https://www.anthropic.com/)
- Inspired by the need for more joy in system status messages

## Support

If you encounter any issues or have questions, please [open an issue](https://github.com/RichardAtCT/status-whimsy/issues) on GitHub.