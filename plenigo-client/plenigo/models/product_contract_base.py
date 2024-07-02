from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.product_contract_base_contract_type import ProductContractBaseContractType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credit_based_product_contract_condition import CreditBasedProductContractCondition
    from ..models.issue_based_product_contract_condition import IssueBasedProductContractCondition
    from ..models.time_based_product_contract_condition import TimeBasedProductContractCondition


T = TypeVar("T", bound="ProductContractBase")


@_attrs_define
class ProductContractBase:
    """
    Attributes:
        title (str): title of the product contract
        contract_type (ProductContractBaseContractType): contract type
        leaf_id (Union[Unset, int]): id of the leaf the contract is related to
        description (Union[Unset, str]): description of the product contract
        product_tag_ids (Union[Unset, List[int]]): tags associated with this product
        ivw_rule_id (Union[Unset, int]): unique id of this ivw rule
        time_based_condition (Union[Unset, TimeBasedProductContractCondition]):
        issue_based_condition (Union[Unset, IssueBasedProductContractCondition]):
        credit_based_condition (Union[Unset, CreditBasedProductContractCondition]):
    """

    title: str
    contract_type: ProductContractBaseContractType
    leaf_id: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    product_tag_ids: Union[Unset, List[int]] = UNSET
    ivw_rule_id: Union[Unset, int] = UNSET
    time_based_condition: Union[Unset, "TimeBasedProductContractCondition"] = UNSET
    issue_based_condition: Union[Unset, "IssueBasedProductContractCondition"] = UNSET
    credit_based_condition: Union[Unset, "CreditBasedProductContractCondition"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title

        contract_type = self.contract_type.value

        leaf_id = self.leaf_id

        description = self.description

        product_tag_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.product_tag_ids, Unset):
            product_tag_ids = self.product_tag_ids

        ivw_rule_id = self.ivw_rule_id

        time_based_condition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.time_based_condition, Unset):
            time_based_condition = self.time_based_condition.to_dict()

        issue_based_condition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.issue_based_condition, Unset):
            issue_based_condition = self.issue_based_condition.to_dict()

        credit_based_condition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credit_based_condition, Unset):
            credit_based_condition = self.credit_based_condition.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "contractType": contract_type,
            }
        )
        if leaf_id is not UNSET:
            field_dict["leafId"] = leaf_id
        if description is not UNSET:
            field_dict["description"] = description
        if product_tag_ids is not UNSET:
            field_dict["productTagIds"] = product_tag_ids
        if ivw_rule_id is not UNSET:
            field_dict["ivwRuleId"] = ivw_rule_id
        if time_based_condition is not UNSET:
            field_dict["timeBasedCondition"] = time_based_condition
        if issue_based_condition is not UNSET:
            field_dict["issueBasedCondition"] = issue_based_condition
        if credit_based_condition is not UNSET:
            field_dict["creditBasedCondition"] = credit_based_condition

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.credit_based_product_contract_condition import CreditBasedProductContractCondition
        from ..models.issue_based_product_contract_condition import IssueBasedProductContractCondition
        from ..models.time_based_product_contract_condition import TimeBasedProductContractCondition

        d = src_dict.copy()
        title = d.pop("title")

        contract_type = ProductContractBaseContractType(d.pop("contractType"))

        leaf_id = d.pop("leafId", UNSET)

        description = d.pop("description", UNSET)

        product_tag_ids = cast(List[int], d.pop("productTagIds", UNSET))

        ivw_rule_id = d.pop("ivwRuleId", UNSET)

        _time_based_condition = d.pop("timeBasedCondition", UNSET)
        time_based_condition: Union[Unset, TimeBasedProductContractCondition]
        if isinstance(_time_based_condition, Unset):
            time_based_condition = UNSET
        else:
            time_based_condition = TimeBasedProductContractCondition.from_dict(_time_based_condition)

        _issue_based_condition = d.pop("issueBasedCondition", UNSET)
        issue_based_condition: Union[Unset, IssueBasedProductContractCondition]
        if isinstance(_issue_based_condition, Unset):
            issue_based_condition = UNSET
        else:
            issue_based_condition = IssueBasedProductContractCondition.from_dict(_issue_based_condition)

        _credit_based_condition = d.pop("creditBasedCondition", UNSET)
        credit_based_condition: Union[Unset, CreditBasedProductContractCondition]
        if isinstance(_credit_based_condition, Unset):
            credit_based_condition = UNSET
        else:
            credit_based_condition = CreditBasedProductContractCondition.from_dict(_credit_based_condition)

        product_contract_base = cls(
            title=title,
            contract_type=contract_type,
            leaf_id=leaf_id,
            description=description,
            product_tag_ids=product_tag_ids,
            ivw_rule_id=ivw_rule_id,
            time_based_condition=time_based_condition,
            issue_based_condition=issue_based_condition,
            credit_based_condition=credit_based_condition,
        )

        product_contract_base.additional_properties = d
        return product_contract_base

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
