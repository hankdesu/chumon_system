from dataclasses import dataclass


@dataclass
class PaginationParams:
    limit: int = 10
    offset: int = 0


@dataclass
class OrderParams:
    sort_by: str = "created_at"
    order: str = "desc"


@dataclass
class FilterParams:
    query: str | None = None
