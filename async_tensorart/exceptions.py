class TensorArtError(Exception):
    """Base exception for all TensorArt errors."""

    error_code: int
    error_type: str
    general_solution: str

    def __init__(
        self,
        code: int | None = None,
        remote_message: str | None = None,
    ) -> None:
        self.code = code or self.error_code
        super().__init__(
            f"[{self.code}] {self.error_type} - {self.general_solution} - "
            f"{remote_message or '(/)'}",
        )


class TensorArtBadRequestError(TensorArtError):
    """400 - Bad Request."""

    error_code = 400
    error_type = "Illegal protocol or parameter"
    general_solution = (
        "Check your program based on the detailed information returned by the API"
    )


class TensorArtUnauthorizedError(TensorArtError):
    """401 - Unauthorized."""

    error_code = 401
    error_type = "Signature verification failed"
    general_solution = (
        "Check if signature parameters and methods comply with "
        "signature algorithm requirements"
    )


class TensorArtForbiddenError(TensorArtError):
    """403 - Forbidden."""

    error_code = 403
    error_type = "Permission exception"
    general_solution = "/"


class TensorArtNotFoundError(TensorArtError):
    """404 - Not Found."""

    error_code = 404
    error_type = "Requested resource does not exist"
    general_solution = "/"


class TensorArtTooManyRequestsError(TensorArtError):
    """429 - Too Many Requests."""

    error_code = 429
    error_type = "Request exceeds frequency limit"
    general_solution = "Request not accepted, please reduce frequency and try again"


class TensorArtInternalServerError(TensorArtError):
    """500 - Internal Server Error."""

    error_code = 500
    error_type = "Server error"
    general_solution = "Retry based on specific API error guidance"


class TensorArtBadGatewayError(TensorArtError):
    """502 - Bad Gateway."""

    error_code = 502
    error_type = "Service offline, temporarily unavailable"
    general_solution = "Request cannot be processed, please try again later"


class TensorArtServiceUnavailableError(TensorArtError):
    """503 - Service Unavailable."""

    error_code = 503
    error_type = "Service unavailable, overload protection"
    general_solution = "Request cannot be processed, please try again later"


class TensorArtUnknownError(TensorArtError):
    """Unknown error."""

    error_code = 0
    error_type = "Unknown error"
    general_solution = "Please contact the TensorArt team"
