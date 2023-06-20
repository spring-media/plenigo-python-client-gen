import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delivery_list_dates_creation_additional_data import DeliveryListDatesCreationAdditionalData


T = TypeVar("T", bound="DeliveryListDatesCreation")


@attr.s(auto_attribs=True)
class DeliveryListDatesCreation:
    """
    Attributes:
        title (str): title of the delivery list date
        publishing_date (datetime.datetime): date the item associated with the delivery list is published
        delivery_date (Union[Unset, datetime.datetime]): date the delivery list should be created at with full-date
            notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339,
            section 5.6</a>, for example, 2017-07-21
        redelivery_date (Union[Unset, datetime.datetime]): date the redelivery list should be created at with full-date
            notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339,
            section 5.6</a>, for example, 2017-07-21
        additional_data (Union[Unset, DeliveryListDatesCreationAdditionalData]):
    """

    title: str
    publishing_date: datetime.datetime
    delivery_date: Union[Unset, datetime.datetime] = UNSET
    redelivery_date: Union[Unset, datetime.datetime] = UNSET
    additional_data: Union[Unset, "DeliveryListDatesCreationAdditionalData"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        publishing_date = self.publishing_date.isoformat()

        delivery_date: Union[Unset, str] = UNSET
        if not isinstance(self.delivery_date, Unset):
            delivery_date = self.delivery_date.isoformat()

        redelivery_date: Union[Unset, str] = UNSET
        if not isinstance(self.redelivery_date, Unset):
            redelivery_date = self.redelivery_date.isoformat()

        additional_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.additional_data, Unset):
            additional_data = self.additional_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "publishingDate": publishing_date,
            }
        )
        if delivery_date is not UNSET:
            field_dict["deliveryDate"] = delivery_date
        if redelivery_date is not UNSET:
            field_dict["redeliveryDate"] = redelivery_date
        if additional_data is not UNSET:
            field_dict["additionalData"] = additional_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.delivery_list_dates_creation_additional_data import DeliveryListDatesCreationAdditionalData

        d = src_dict.copy()
        title = d.pop("title")

        publishing_date = isoparse(d.pop("publishingDate"))

        _delivery_date = d.pop("deliveryDate", UNSET)
        delivery_date: Union[Unset, datetime.datetime]
        if isinstance(_delivery_date, Unset):
            delivery_date = UNSET
        else:
            delivery_date = isoparse(_delivery_date)

        _redelivery_date = d.pop("redeliveryDate", UNSET)
        redelivery_date: Union[Unset, datetime.datetime]
        if isinstance(_redelivery_date, Unset):
            redelivery_date = UNSET
        else:
            redelivery_date = isoparse(_redelivery_date)

        _additional_data = d.pop("additionalData", UNSET)
        additional_data: Union[Unset, DeliveryListDatesCreationAdditionalData]
        if isinstance(_additional_data, Unset):
            additional_data = UNSET
        else:
            additional_data = DeliveryListDatesCreationAdditionalData.from_dict(_additional_data)

        delivery_list_dates_creation = cls(
            title=title,
            publishing_date=publishing_date,
            delivery_date=delivery_date,
            redelivery_date=redelivery_date,
            additional_data=additional_data,
        )

        delivery_list_dates_creation.additional_properties = d
        return delivery_list_dates_creation

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
