"""Tests for status_whimsy package."""

from unittest.mock import Mock, patch

import pytest

from status_whimsy import StatusWhimsy, whimsify


class TestStatusWhimsy:
    """Test cases for StatusWhimsy class."""

    def test_init_with_api_key(self):
        """Test initialization with API key."""
        client = StatusWhimsy(api_key="test-key")
        assert client.api_key == "test-key"

    def test_init_with_env_var(self):
        """Test initialization with environment variable."""
        with patch.dict("os.environ", {"ANTHROPIC_API_KEY": "env-key"}):
            client = StatusWhimsy()
            assert client.api_key == "env-key"

    def test_init_without_api_key(self):
        """Test initialization without API key raises error."""
        with patch.dict("os.environ", {}, clear=True):
            with pytest.raises(ValueError, match="API key must be provided"):
                StatusWhimsy()

    def test_whimsicalness_validation(self):
        """Test whimsicalness parameter validation."""
        client = StatusWhimsy(api_key="test-key")

        with patch.object(client.client.messages, "create") as mock_create:
            mock_create.return_value = Mock(content=[Mock(text="Mocked response")])

            # Test invalid whimsicalness levels
            with pytest.raises(ValueError, match="Whimsicalness must be between 1 and 10"):
                client.generate("test", whimsicalness=0)

            with pytest.raises(ValueError, match="Whimsicalness must be between 1 and 10"):
                client.generate("test", whimsicalness=11)

    @patch("status_whimsy.core.Anthropic")
    def test_generate_success(self, mock_anthropic):
        """Test successful generation."""
        # Mock the API response
        mock_client = Mock()
        mock_response = Mock()
        mock_response.content = [Mock(text="The server is dancing! 🎉")]
        mock_client.messages.create.return_value = mock_response
        mock_anthropic.return_value = mock_client

        client = StatusWhimsy(api_key="test-key")
        result = client.generate("Server is running", whimsicalness=7)

        assert result == "The server is dancing! 🎉"
        mock_client.messages.create.assert_called_once()

    @patch("status_whimsy.core.Anthropic")
    def test_batch_generate(self, mock_anthropic):
        """Test batch generation."""
        # Mock the API responses
        mock_client = Mock()
        mock_responses = [
            Mock(content=[Mock(text="Response 1")]),
            Mock(content=[Mock(text="Response 2")]),
            Mock(content=[Mock(text="Response 3")]),
        ]
        mock_client.messages.create.side_effect = mock_responses
        mock_anthropic.return_value = mock_client

        client = StatusWhimsy(api_key="test-key")
        results = client.batch_generate(["Status 1", "Status 2", "Status 3"], whimsicalness=5)

        assert results == ["Response 1", "Response 2", "Response 3"]
        assert mock_client.messages.create.call_count == 3

    @patch("status_whimsy.core.Anthropic")
    def test_temperature_scaling(self, mock_anthropic):
        """Test that temperature scales with whimsicalness."""
        mock_client = Mock()
        mock_response = Mock(content=[Mock(text="Response")])
        mock_client.messages.create.return_value = mock_response
        mock_anthropic.return_value = mock_client

        client = StatusWhimsy(api_key="test-key")

        # Test different whimsicalness levels
        for whimsy in [1, 5, 10]:
            client.generate("Test", whimsicalness=whimsy)

            # Get the call arguments
            call_args = mock_client.messages.create.call_args
            temperature = call_args[1]["temperature"]

            # Check temperature scaling: 0.7 + (whimsy * 0.03)
            expected_temp = 0.7 + (whimsy * 0.03)
            assert temperature == pytest.approx(expected_temp)

    @patch("status_whimsy.core.Anthropic")
    def test_whimsify_function(self, mock_anthropic):
        """Test the whimsify convenience function."""
        mock_client = Mock()
        mock_response = Mock(content=[Mock(text="Whimsified!")])
        mock_client.messages.create.return_value = mock_response
        mock_anthropic.return_value = mock_client

        result = whimsify("Test status", api_key="test-key", whimsicalness=8)
        assert result == "Whimsified!"
