from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalCreditUpload")


@_attrs_define
class ExternalCreditUpload:
    """
    Attributes:
        customer_id (Union[Unset, str]): id of the customer the credit usage should be accounted to
        unique_id (Union[Unset, str]): unique id of the wallet to use
        title (Union[Unset, str]): title of upload
        credit_count (Union[Unset, int]): amount of credits to add
    """

    customer_id: Union[Unset, str] = UNSET
    unique_id: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    credit_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer_id = self.customer_id

        unique_id = self.unique_id

        title = self.title

        credit_count = self.credit_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if unique_id is not UNSET:
            field_dict["uniqueId"] = unique_id
        if title is not UNSET:
            field_dict["title"] = title
        if credit_count is not UNSET:
            field_dict["creditCount"] = credit_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        customer_id = d.pop("customerId", UNSET)

        unique_id = d.pop("uniqueId", UNSET)

        title = d.pop("title", UNSET)

        credit_count = d.pop("creditCount", UNSET)

        external_credit_upload = cls(
            customer_id=customer_id,
            unique_id=unique_id,
            title=title,
            credit_count=credit_count,
        )

        external_credit_upload.additional_properties = d
        return external_credit_upload

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
