from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_used_by_object import ApiUsedByObject
    from ..models.api_used_by_offer import ApiUsedByOffer


T = TypeVar("T", bound="ApiUsedBy")


@_attrs_define
class ApiUsedBy:
    """
    Attributes:
        voucher_purchases (Union[Unset, List['ApiUsedByOffer']]):
        relation_rules (Union[Unset, List['ApiUsedByObject']]):
        age_rules (Union[Unset, List['ApiUsedByObject']]):
    """

    voucher_purchases: Union[Unset, List["ApiUsedByOffer"]] = UNSET
    relation_rules: Union[Unset, List["ApiUsedByObject"]] = UNSET
    age_rules: Union[Unset, List["ApiUsedByObject"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        voucher_purchases: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.voucher_purchases, Unset):
            voucher_purchases = []
            for voucher_purchases_item_data in self.voucher_purchases:
                voucher_purchases_item = voucher_purchases_item_data.to_dict()
                voucher_purchases.append(voucher_purchases_item)

        relation_rules: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.relation_rules, Unset):
            relation_rules = []
            for relation_rules_item_data in self.relation_rules:
                relation_rules_item = relation_rules_item_data.to_dict()
                relation_rules.append(relation_rules_item)

        age_rules: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.age_rules, Unset):
            age_rules = []
            for age_rules_item_data in self.age_rules:
                age_rules_item = age_rules_item_data.to_dict()
                age_rules.append(age_rules_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if voucher_purchases is not UNSET:
            field_dict["voucherPurchases"] = voucher_purchases
        if relation_rules is not UNSET:
            field_dict["relationRules"] = relation_rules
        if age_rules is not UNSET:
            field_dict["ageRules"] = age_rules

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_used_by_object import ApiUsedByObject
        from ..models.api_used_by_offer import ApiUsedByOffer

        d = src_dict.copy()
        voucher_purchases = []
        _voucher_purchases = d.pop("voucherPurchases", UNSET)
        for voucher_purchases_item_data in _voucher_purchases or []:
            voucher_purchases_item = ApiUsedByOffer.from_dict(voucher_purchases_item_data)

            voucher_purchases.append(voucher_purchases_item)

        relation_rules = []
        _relation_rules = d.pop("relationRules", UNSET)
        for relation_rules_item_data in _relation_rules or []:
            relation_rules_item = ApiUsedByObject.from_dict(relation_rules_item_data)

            relation_rules.append(relation_rules_item)

        age_rules = []
        _age_rules = d.pop("ageRules", UNSET)
        for age_rules_item_data in _age_rules or []:
            age_rules_item = ApiUsedByObject.from_dict(age_rules_item_data)

            age_rules.append(age_rules_item)

        api_used_by = cls(
            voucher_purchases=voucher_purchases,
            relation_rules=relation_rules,
            age_rules=age_rules,
        )

        api_used_by.additional_properties = d
        return api_used_by

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
