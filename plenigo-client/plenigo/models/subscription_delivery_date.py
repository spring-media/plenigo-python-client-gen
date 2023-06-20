import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriptionDeliveryDate")


@attr.s(auto_attribs=True)
class SubscriptionDeliveryDate:
    """
    Attributes:
        subscription_delivery_date_id (int): unique id of the subscription delivery date in the context of a company
        title (str): title of the subscripiton delivery date
        publishing_date (datetime.datetime): publishing date time of the subscription delivery list with date-time
            notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339,
            section 5.6</a>, for example, 2017-07-21T17:32:28Z
        subscription_id (int): unique id of the subscription in the context of a company
        delivery_list_id (int): id of the delivery list the subscription delivery date belongs to
        delivery_list_date_id (int): id of the delivery list date the subscription delivery date belongs to
        created_date (Union[Unset, datetime.datetime]): date the delivery date entity was created with date-time
            notation as defined by RFC 3339, section 5.6, for example, 2017-07-21T17:32:28Z
        changed_date (Union[Unset, datetime.datetime]): date the delivery date entity was changed with date-time
            notation as defined by RFC 3339, section 5.6, for example, 2017-07-21T17:32:28Z
        delivery_customer_id (Union[Unset, str]): id of the customer the delivery belongs to (also includes digital
            products)
        delivery_address_id (Union[Unset, int]): id of the delivery address that is associated with this subscription
    """

    subscription_delivery_date_id: int
    title: str
    publishing_date: datetime.datetime
    subscription_id: int
    delivery_list_id: int
    delivery_list_date_id: int
    created_date: Union[Unset, datetime.datetime] = UNSET
    changed_date: Union[Unset, datetime.datetime] = UNSET
    delivery_customer_id: Union[Unset, str] = UNSET
    delivery_address_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subscription_delivery_date_id = self.subscription_delivery_date_id
        title = self.title
        publishing_date = self.publishing_date.isoformat()

        subscription_id = self.subscription_id
        delivery_list_id = self.delivery_list_id
        delivery_list_date_id = self.delivery_list_date_id
        created_date: Union[Unset, str] = UNSET
        if not isinstance(self.created_date, Unset):
            created_date = self.created_date.isoformat()

        changed_date: Union[Unset, str] = UNSET
        if not isinstance(self.changed_date, Unset):
            changed_date = self.changed_date.isoformat()

        delivery_customer_id = self.delivery_customer_id
        delivery_address_id = self.delivery_address_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subscriptionDeliveryDateId": subscription_delivery_date_id,
                "title": title,
                "publishingDate": publishing_date,
                "subscriptionId": subscription_id,
                "deliveryListId": delivery_list_id,
                "deliveryListDateId": delivery_list_date_id,
            }
        )
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if delivery_customer_id is not UNSET:
            field_dict["deliveryCustomerId"] = delivery_customer_id
        if delivery_address_id is not UNSET:
            field_dict["deliveryAddressId"] = delivery_address_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subscription_delivery_date_id = d.pop("subscriptionDeliveryDateId")

        title = d.pop("title")

        publishing_date = isoparse(d.pop("publishingDate"))

        subscription_id = d.pop("subscriptionId")

        delivery_list_id = d.pop("deliveryListId")

        delivery_list_date_id = d.pop("deliveryListDateId")

        _created_date = d.pop("createdDate", UNSET)
        created_date: Union[Unset, datetime.datetime]
        if isinstance(_created_date, Unset):
            created_date = UNSET
        else:
            created_date = isoparse(_created_date)

        _changed_date = d.pop("changedDate", UNSET)
        changed_date: Union[Unset, datetime.datetime]
        if isinstance(_changed_date, Unset):
            changed_date = UNSET
        else:
            changed_date = isoparse(_changed_date)

        delivery_customer_id = d.pop("deliveryCustomerId", UNSET)

        delivery_address_id = d.pop("deliveryAddressId", UNSET)

        subscription_delivery_date = cls(
            subscription_delivery_date_id=subscription_delivery_date_id,
            title=title,
            publishing_date=publishing_date,
            subscription_id=subscription_id,
            delivery_list_id=delivery_list_id,
            delivery_list_date_id=delivery_list_date_id,
            created_date=created_date,
            changed_date=changed_date,
            delivery_customer_id=delivery_customer_id,
            delivery_address_id=delivery_address_id,
        )

        subscription_delivery_date.additional_properties = d
        return subscription_delivery_date

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
