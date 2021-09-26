from dataclasses import dataclass
from typing import Optional

import dns.resolver
from dns.rdatatype import PTR

__all__ = [
    "Resolver"
]


@dataclass
class Resolver:
    """Class which enables to query a given `domain`."""

    domain: str

    def __post_init__(self) -> None:
        """Create a DNS Resolver."""
        self.dns_resolver = dns.resolver.Resolver()

    def resolve_ip(self, ip_address: str) -> Optional[str]:
        """Try to resolve an `ip_address`. Return None if error occurs."""
        try:
            result: PTR = self.dns_resolver.resolve_address(ip_address)[0]
            name = result.to_text()

            # Omit final dot
            return name[:-1]
        except dns.resolver.NXDOMAIN:
            return None

    def get_ip_addresses(self) -> list[str]:
        """Get all ip addresses for the domain."""
        answers = self.dns_resolver.resolve(self.domain)

        return [
            ip.to_text()
            for ip in answers
        ]

    def get_canonical_name(self) -> str:
        """Get canonical_name for the domain."""
        return self.dns_resolver\
            .canonical_name(self.domain)\
            .to_text(True)

    def get_ip_addresses_with_resolved_names(self) -> list:
        """Get ip addresses with resolved names."""
        ip_addresses = self.get_ip_addresses()

        return [
            {
                "ip_address": ip_address,
                "resolved_address": self.resolve_ip(ip_address)
            }
            for ip_address in ip_addresses
        ]
