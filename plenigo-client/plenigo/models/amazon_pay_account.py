import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AmazonPayAccount")


@attr.s(auto_attribs=True)
class AmazonPayAccount:
    """
    Attributes:
        amazon_pay_account_id (int): unique id of the Amazon pay account
        charge_permission_id (str): charge permisson id of the Amazon pay account
        customer_id (str): unique id of the customer the Amazon pay account belongs to
        changed_date (datetime.datetime): date time the Amazon pay account entity was changed with date-time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 2017-07-21T17:32:28Z
        preferred (Union[Unset, bool]): flag indicating if Amazon pay account is the preferred Amazon pay account - only
            one Amazon pay account can be preferred.
        active (Union[Unset, bool]): flag indicating if Amazon pay account is active - a bank account can become
            inactive by getting closed, etc.
    """

    amazon_pay_account_id: int
    charge_permission_id: str
    customer_id: str
    changed_date: datetime.datetime
    preferred: Union[Unset, bool] = UNSET
    active: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amazon_pay_account_id = self.amazon_pay_account_id
        charge_permission_id = self.charge_permission_id
        customer_id = self.customer_id
        changed_date = self.changed_date.isoformat()

        preferred = self.preferred
        active = self.active

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amazonPayAccountId": amazon_pay_account_id,
                "chargePermissionId": charge_permission_id,
                "customerId": customer_id,
                "changedDate": changed_date,
            }
        )
        if preferred is not UNSET:
            field_dict["preferred"] = preferred
        if active is not UNSET:
            field_dict["active"] = active

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amazon_pay_account_id = d.pop("amazonPayAccountId")

        charge_permission_id = d.pop("chargePermissionId")

        customer_id = d.pop("customerId")

        changed_date = isoparse(d.pop("changedDate"))

        preferred = d.pop("preferred", UNSET)

        active = d.pop("active", UNSET)

        amazon_pay_account = cls(
            amazon_pay_account_id=amazon_pay_account_id,
            charge_permission_id=charge_permission_id,
            customer_id=customer_id,
            changed_date=changed_date,
            preferred=preferred,
            active=active,
        )

        amazon_pay_account.additional_properties = d
        return amazon_pay_account

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
