from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostFinanceAccountChange")


@_attrs_define
class PostFinanceAccountChange:
    """
    Attributes:
        charge_permission_id (str): the PostFinance charge permission id
        preferred (Union[Unset, bool]): flag indicating if PostFinance account is the preferred PostFinance account -
            only one PostFinance account can be preferred.
        invalid (Union[Unset, bool]): flag indicating if payment method should be handled as invalid
    """

    charge_permission_id: str
    preferred: Union[Unset, bool] = UNSET
    invalid: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        charge_permission_id = self.charge_permission_id

        preferred = self.preferred

        invalid = self.invalid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chargePermissionId": charge_permission_id,
            }
        )
        if preferred is not UNSET:
            field_dict["preferred"] = preferred
        if invalid is not UNSET:
            field_dict["invalid"] = invalid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        charge_permission_id = d.pop("chargePermissionId")

        preferred = d.pop("preferred", UNSET)

        invalid = d.pop("invalid", UNSET)

        post_finance_account_change = cls(
            charge_permission_id=charge_permission_id,
            preferred=preferred,
            invalid=invalid,
        )

        post_finance_account_change.additional_properties = d
        return post_finance_account_change

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
