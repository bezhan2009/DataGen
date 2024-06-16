class Url:
    def __init__(
            self,
            protocol: str,
            address: str,
            domain: str
    ) -> None:
        self.protocol: str = protocol
        self.address: str = address
        self.domain: str = domain

    @property
    def full_address(self) -> str:
        return f"{self.protocol}{self.address}{self.domain}"

    def __str__(self) -> str:
        return f"{self.protocol}{self.address}{self.domain}"

    def __len__(self) -> int:
        return len(self.full_address)

    def __repr__(self) -> str:
        return f"{self.protocol}{self.address}{self.domain}"
