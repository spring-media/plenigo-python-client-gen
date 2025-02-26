import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.price_country_segment import PriceCountrySegment


T = TypeVar("T", bound="PriceSegment")


@_attrs_define
class PriceSegment:
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
        created_date (Union[None, Unset, datetime.datetime]): time the object was created with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        changed_date (Union[None, Unset, datetime.datetime]): time the object was changed with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        price_segment_id (Union[Unset, int]): unique id of the price segment within a contract company
        country_segments (Union[Unset, PriceCountrySegment]):
    """

    price: float
    currency: str
    valid_from: Union[None, datetime.date]
    valid_from_existing_subscription: Union[None, Unset, datetime.date] = UNSET
    world_segment: Union[Unset, bool] = UNSET
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    price_segment_id: Union[Unset, int] = UNSET
    country_segments: Union[Unset, "PriceCountrySegment"] = UNSET
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
        if isinstance(self.valid_from_existing_subscription, Unset) or self.valid_from_existing_subscription is None:
            valid_from_existing_subscription = UNSET
        elif isinstance(self.valid_from_existing_subscription, datetime.date):
            valid_from_existing_subscription = self.valid_from_existing_subscription.isoformat()
        else:
            valid_from_existing_subscription = self.valid_from_existing_subscription

        world_segment = self.world_segment

        created_date: Union[None, Unset, str]
        if isinstance(self.created_date, Unset) or self.created_date is None:
            created_date = UNSET
        elif isinstance(self.created_date, datetime.datetime):
            created_date = self.created_date.isoformat()
        else:
            created_date = self.created_date

        changed_date: Union[None, Unset, str]
        if isinstance(self.changed_date, Unset) or self.changed_date is None:
            changed_date = UNSET
        elif isinstance(self.changed_date, datetime.datetime):
            changed_date = self.changed_date.isoformat()
        else:
            changed_date = self.changed_date

        price_segment_id = self.price_segment_id

        country_segments: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.country_segments, Unset):
            country_segments = self.country_segments.to_dict()

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
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if price_segment_id is not UNSET:
            field_dict["priceSegmentId"] = price_segment_id
        if country_segments is not UNSET:
            field_dict["countrySegments"] = country_segments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.price_country_segment import PriceCountrySegment

        d = src_dict.copy()
        price = d.pop("price")

        currency = d.pop("currency")

        def _parse_valid_from(data: object) -> Union[None, datetime.date]:
            if data is None:
                return data

            # Try to parse the data as datetime.date
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

            if data is None:
                return data

            if isinstance(data, Unset):
                return data

            # Try to parse the data as datetime.date
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

        def _parse_created_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data

            if data is None:
                return data

            if isinstance(data, Unset):
                return data

            # Try to parse the data as datetime.datetime
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_date_type_0 = isoparse(data)

                return created_date_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        created_date = _parse_created_date(d.pop("createdDate", UNSET))

        def _parse_changed_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data

            if data is None:
                return data

            if isinstance(data, Unset):
                return data

            # Try to parse the data as datetime.datetime
            try:
                if not isinstance(data, str):
                    raise TypeError()
                changed_date_type_0 = isoparse(data)

                return changed_date_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        changed_date = _parse_changed_date(d.pop("changedDate", UNSET))

        price_segment_id = d.pop("priceSegmentId", UNSET)

        _country_segments = d.pop("countrySegments", UNSET)
        country_segments: Union[Unset, PriceCountrySegment]
        if isinstance(_country_segments, Unset) or not _country_segments:
            country_segments = UNSET
        else:
            country_segments = PriceCountrySegment.from_dict(_country_segments)

        price_segment = cls(
            price=price,
            currency=currency,
            valid_from=valid_from,
            valid_from_existing_subscription=valid_from_existing_subscription,
            world_segment=world_segment,
            created_date=created_date,
            changed_date=changed_date,
            price_segment_id=price_segment_id,
            country_segments=country_segments,
        )

        price_segment.additional_properties = d
        return price_segment

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
