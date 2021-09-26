from fastapi import APIRouter, Depends

from src.dependencies import get_hostname
from src.models import GetDomainInformationResult
from src.utils import Resolver

__all__ = [
    "router"
]


router = APIRouter()


@router.get("/", response_model=GetDomainInformationResult)
async def get_domain_information(
    domain: str = Depends(get_hostname)
):
    """Get information about a `domain`."""
    resolver = Resolver(domain)

    return {
        "canonical_name": resolver.get_canonical_name(),
        "ip_addresses": resolver.get_ip_addresses()
    }
