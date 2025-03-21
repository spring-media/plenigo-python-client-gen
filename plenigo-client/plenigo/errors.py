""" Contains shared errors types that can be raised from API functions """


class UnexpectedStatus(Exception):
    """Raised by api functions when the response status an undocumented status and Client.raise_on_unexpected_status is True"""

    def __init__(self, status_code: int, content: bytes):
        self.status_code = status_code
        self.content = content

        super().__init__(
            f"Unexpected status code: {status_code}\n\nResponse content:\n{content.decode(errors='ignore')}"
        )


class RetryableError(Exception):
    """Raised because of a problem with the gateway or proxy server, indenpended on the api server or clinet"""

    def __init__(self, *args, **kwargs):
        super().__init__("Gateway error, retrying the request")


__all__ = ["UnexpectedStatus", "RetryableError"]
