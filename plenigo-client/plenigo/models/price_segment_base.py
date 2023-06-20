import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PriceSegmentBase")


@attr.s(auto_attribs=True)
class PriceSegmentBase:
    """
    Attributes:
        price (float): price of the product
        currency (str): currency of the order formatted as <a href='https://en.wikipedia.org/wiki/ISO_4217'
            target='_blank'>ISO 4217, alphabetic code</a>
        valid_from (datetime.date): date price segment is valid from in full-date notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-21
        world_segment (Union[Unset, bool]): flag indicating if price is valid for the complete world if no other price
            segments are provided - must be set if price country segment id is not provided
    """

    price: float
    currency: str
    valid_from: datetime.date
    world_segment: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        price = self.price
        currency = self.currency
        valid_from = self.valid_from.isoformat()
        world_segment = self.world_segment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "price": price,
                "currency": currency,
                "validFrom": valid_from,
            }
        )
        if world_segment is not UNSET:
            field_dict["worldSegment"] = world_segment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        price = d.pop("price")

        currency = d.pop("currency")

        valid_from = isoparse(d.pop("validFrom")).date()

        world_segment = d.pop("worldSegment", UNSET)

        price_segment_base = cls(
            price=price,
            currency=currency,
            valid_from=valid_from,
            world_segment=world_segment,
        )

        price_segment_base.additional_properties = d
        return price_segment_base

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
