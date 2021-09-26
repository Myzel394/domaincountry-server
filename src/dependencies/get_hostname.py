import socket

from fastapi import HTTPException

from starlette import status


__all__ = [
    "get_hostname"
]


async def get_hostname(
    domain: str
) -> str:
    """Return hostname of `url`."""
    try:
        socket.gethostbyname(domain)
    except socket.gaierror:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The given domain is not valid."
        )

    return domain
