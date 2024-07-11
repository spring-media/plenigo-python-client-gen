import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostFinanceAccountCreation")


@_attrs_define
class PostFinanceAccountCreation:
    """
    Attributes:
        charge_permission_id (str): the PostFinance charge permission id
        customer_id (str): unique id of the customer the PostFinance account belongs to
        preferred (Union[Unset, bool]): flag indicating if PostFinance account is the preferred PostFinance account -
            only one PostFinance account can be preferred.
        invalid (Union[Unset, bool]): flag indicating if payment method should be handled as invalid
        created_at (Union[None, Unset, datetime.datetime]): date time the PostFinance account entity was created with
            date-time notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC
            3339, section 5.6</a>, for example, 2017-07-21T17:32:28Z
        updated_at (Union[None, Unset, datetime.datetime]): date time the PostFinance account entity was changed with
            date-time notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC
            3339, section 5.6</a>, for example, 2017-07-21T17:32:28Z
    """

    charge_permission_id: str
    customer_id: str
    preferred: Union[Unset, bool] = UNSET
    invalid: Union[Unset, bool] = UNSET
    created_at: Union[None, Unset, datetime.datetime] = UNSET
    updated_at: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        charge_permission_id = self.charge_permission_id

        customer_id = self.customer_id

        preferred = self.preferred

        invalid = self.invalid

        created_at: Union[None, Unset, str]
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: Union[None, Unset, str]
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chargePermissionId": charge_permission_id,
                "customerId": customer_id,
            }
        )
        if preferred is not UNSET:
            field_dict["preferred"] = preferred
        if invalid is not UNSET:
            field_dict["invalid"] = invalid
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        charge_permission_id = d.pop("chargePermissionId")

        customer_id = d.pop("customerId")

        preferred = d.pop("preferred", UNSET)

        invalid = d.pop("invalid", UNSET)

        def _parse_created_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)

                return created_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))

        def _parse_updated_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)

                return updated_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))

        post_finance_account_creation = cls(
            charge_permission_id=charge_permission_id,
            customer_id=customer_id,
            preferred=preferred,
            invalid=invalid,
            created_at=created_at,
            updated_at=updated_at,
        )

        post_finance_account_creation.additional_properties = d
        return post_finance_account_creation

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
