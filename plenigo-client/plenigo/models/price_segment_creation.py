import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PriceSegmentCreation")


@_attrs_define
class PriceSegmentCreation:
    """
    Attributes:
        price (float): price of the product
        currency (str): currency of the order formatted as <a href='https://en.wikipedia.org/wiki/ISO_4217'
            target='_blank'>ISO 4217, alphabetic code</a>
        valid_from (Union[None, datetime.date]): date price segment is valid from in full-date notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-21
        valid_from_existing_subscription (Union[None, Unset, datetime.date]): date price segment is valid for exisiting
            subscriptions from in full-date notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6"
            target="_blank">RFC 3339, section 5.6</a>, for example, 2017-07-21
        world_segment (Union[Unset, bool]): flag indicating if price is valid for the complete world if no other price
            segments are provided - must be set if price country segment id is not provided
        price_country_segment_id (Union[Unset, int]): id of the price country segment to associate with this price
            segment - can be empty if world segment flag is set
    """

    price: float
    currency: str
    valid_from: Union[None, datetime.date]
    valid_from_existing_subscription: Union[None, Unset, datetime.date] = UNSET
    world_segment: Union[Unset, bool] = UNSET
    price_country_segment_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        price = self.price

        currency = self.currency

        valid_from: Union[None, str]
        if isinstance(self.valid_from, datetime.date):
            valid_from = self.valid_from.isoformat()
        else:
            valid_from = self.valid_from

        valid_from_existing_subscription: Union[None, Unset, str]
        if isinstance(self.valid_from_existing_subscription, Unset):
            valid_from_existing_subscription = UNSET
        elif isinstance(self.valid_from_existing_subscription, datetime.date):
            valid_from_existing_subscription = self.valid_from_existing_subscription.isoformat()
        else:
            valid_from_existing_subscription = self.valid_from_existing_subscription

        world_segment = self.world_segment

        price_country_segment_id = self.price_country_segment_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "price": price,
                "currency": currency,
                "validFrom": valid_from,
            }
        )
        if valid_from_existing_subscription is not UNSET:
            field_dict["validFromExistingSubscription"] = valid_from_existing_subscription
        if world_segment is not UNSET:
            field_dict["worldSegment"] = world_segment
        if price_country_segment_id is not UNSET:
            field_dict["priceCountrySegmentId"] = price_country_segment_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        price = d.pop("price")

        currency = d.pop("currency")

        def _parse_valid_from(data: object) -> Union[None, datetime.date]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                valid_from_type_0 = isoparse(data).date()

                return valid_from_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.date], data)

        valid_from = _parse_valid_from(d.pop("validFrom"))

        def _parse_valid_from_existing_subscription(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                valid_from_existing_subscription_type_0 = isoparse(data).date()

                return valid_from_existing_subscription_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        valid_from_existing_subscription = _parse_valid_from_existing_subscription(
            d.pop("validFromExistingSubscription", UNSET)
        )

        world_segment = d.pop("worldSegment", UNSET)

        price_country_segment_id = d.pop("priceCountrySegmentId", UNSET)

        price_segment_creation = cls(
            price=price,
            currency=currency,
            valid_from=valid_from,
            valid_from_existing_subscription=valid_from_existing_subscription,
            world_segment=world_segment,
            price_country_segment_id=price_country_segment_id,
        )

        price_segment_creation.additional_properties = d
        return price_segment_creation

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