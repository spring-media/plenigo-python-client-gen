import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SchemasAmazonPayAccount")


@_attrs_define
class SchemasAmazonPayAccount:
    """
    Attributes:
        charge_permission_id (str): the amazon pay charge permission id
        amazon_pay_account_id (int): unique id of the amazon pay account
        customer_id (str): unique id of the customer the amazon pay account belongs to
        preferred (Union[Unset, bool]): flag indicating if amazon pay account is the preferred amazon pay account - only
            one amazon pay account can be preferred.
        invalid (Union[Unset, bool]): flag indicating if payment method should be handled as invalid
        created_date (Union[None, Unset, datetime.datetime]): time the object was created with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        changed_date (Union[None, Unset, datetime.datetime]): time the object was changed with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        active (Union[Unset, bool]): flag indicating if amazon pay account is active - a amazon pay account can become
            inactive by getting closed, etc.
    """

    charge_permission_id: str
    amazon_pay_account_id: int
    customer_id: str
    preferred: Union[Unset, bool] = UNSET
    invalid: Union[Unset, bool] = UNSET
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    active: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        charge_permission_id = self.charge_permission_id

        amazon_pay_account_id = self.amazon_pay_account_id

        customer_id = self.customer_id

        preferred = self.preferred

        invalid = self.invalid

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

        active = self.active

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chargePermissionId": charge_permission_id,
                "amazonPayAccountId": amazon_pay_account_id,
                "customerId": customer_id,
            }
        )
        if preferred is not UNSET:
            field_dict["preferred"] = preferred
        if invalid is not UNSET:
            field_dict["invalid"] = invalid
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if active is not UNSET:
            field_dict["active"] = active

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        charge_permission_id = d.pop("chargePermissionId")

        amazon_pay_account_id = d.pop("amazonPayAccountId")

        customer_id = d.pop("customerId")

        preferred = d.pop("preferred", UNSET)

        invalid = d.pop("invalid", UNSET)

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
                created_date_type_1 = isoparse(data)

                return created_date_type_1
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
                changed_date_type_1 = isoparse(data)

                return changed_date_type_1
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        changed_date = _parse_changed_date(d.pop("changedDate", UNSET))

        active = d.pop("active", UNSET)

        schemas_amazon_pay_account = cls(
            charge_permission_id=charge_permission_id,
            amazon_pay_account_id=amazon_pay_account_id,
            customer_id=customer_id,
            preferred=preferred,
            invalid=invalid,
            created_date=created_date,
            changed_date=changed_date,
            active=active,
        )

        schemas_amazon_pay_account.additional_properties = d
        return schemas_amazon_pay_account

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
