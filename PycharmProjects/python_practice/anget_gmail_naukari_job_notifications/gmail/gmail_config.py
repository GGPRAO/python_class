"""
Gmail Configuration Module
Contains hardcoded credentials for chatbot integration.
"""


class GmailConfig:
    """Gmail configuration with hardcoded credentials for chatbot."""

    # Hardcoded email and passcode
    EMAIL = "ggpsmo@gmail.com"
    PASSCODE = "lodqerzdhzjppwph"

    # IMAP settings
    IMAP_SERVER = "imap.gmail.com"
    IMAP_PORT = 993

    # Default settings
    DEFAULT_EMAIL_LIMIT = 5
    SEARCH_QUERY = 'FROM "naukri"'  # Search for Naukri emails

    @classmethod
    def get_credentials(cls):
        """
        Get email and passcode for authentication.

        Returns:
            tuple: (email, passcode)
        """
        return (cls.EMAIL, cls.PASSCODE)

    @classmethod
    def get_imap_connection_settings(cls):
        """
        Get IMAP connection settings.

        Returns:
            dict: IMAP connection configuration
        """
        return {
            "server": cls.IMAP_SERVER,
            "port": cls.IMAP_PORT,
            "email": cls.EMAIL,
            "passcode": cls.PASSCODE
        }

