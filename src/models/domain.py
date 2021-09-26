from pydantic import BaseModel

__all__ = [
    "GetDomainInformationResult"
]


class GetDomainInformationResult(BaseModel):
    """Result for the get_domain_information endpoint."""

    canonical_name: str
    ip_addresses: list[str]
