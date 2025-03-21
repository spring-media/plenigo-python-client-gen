import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.product_contract_base_contract_type import ProductContractBaseContractType
from ..models.user_type import UserType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credit_based_product_contract_condition import CreditBasedProductContractCondition
    from ..models.issue_based_product_contract_condition import IssueBasedProductContractCondition
    from ..models.time_based_product_contract_condition import TimeBasedProductContractCondition


T = TypeVar("T", bound="ProductContract")


@_attrs_define
class ProductContract:
    """
    Attributes:
        title (str): title of the product contract
        contract_type (ProductContractBaseContractType): contract type
        product_contract_id (int): unique id of the product contract within a contract company
        archived (bool): flag indicating if price country segment is archived
        created_date (Union[None, Unset, datetime.datetime]): time the object was created with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        changed_date (Union[None, Unset, datetime.datetime]): time the object was changed with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        created_by (Union[Unset, str]): id who created the object
        created_by_type (Union[Unset, UserType]): type of user who performs the action
        changed_by (Union[Unset, str]): id who changed the object
        changed_by_type (Union[Unset, UserType]): type of user who performs the action
        leaf_id (Union[Unset, int]): id of the leaf the contract is related to
        description (Union[Unset, str]): description of the product contract
        product_tag_ids (Union[Unset, list[int]]): tags associated with this product
        ivw_rule_id (Union[Unset, int]): unique id of this ivw rule
        time_based_condition (Union[Unset, TimeBasedProductContractCondition]):
        issue_based_condition (Union[Unset, IssueBasedProductContractCondition]):
        credit_based_condition (Union[Unset, CreditBasedProductContractCondition]):
        price_issue_id (Union[Unset, int]): price issue to use (is only not required when it is a multiuser contract.
    """

    title: str
    contract_type: ProductContractBaseContractType
    product_contract_id: int
    archived: bool
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_by_type: Union[Unset, UserType] = UNSET
    changed_by: Union[Unset, str] = UNSET
    changed_by_type: Union[Unset, UserType] = UNSET
    leaf_id: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    product_tag_ids: Union[Unset, list[int]] = UNSET
    ivw_rule_id: Union[Unset, int] = UNSET
    time_based_condition: Union[Unset, "TimeBasedProductContractCondition"] = UNSET
    issue_based_condition: Union[Unset, "IssueBasedProductContractCondition"] = UNSET
    credit_based_condition: Union[Unset, "CreditBasedProductContractCondition"] = UNSET
    price_issue_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title

        contract_type = self.contract_type.value

        product_contract_id = self.product_contract_id

        archived = self.archived

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

        created_by = self.created_by

        created_by_type: Union[Unset, str] = UNSET
        if not isinstance(self.created_by_type, Unset):
            created_by_type = self.created_by_type.value

        changed_by = self.changed_by

        changed_by_type: Union[Unset, str] = UNSET
        if not isinstance(self.changed_by_type, Unset):
            changed_by_type = self.changed_by_type.value

        leaf_id = self.leaf_id

        description = self.description

        product_tag_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.product_tag_ids, Unset):
            product_tag_ids = self.product_tag_ids

        ivw_rule_id = self.ivw_rule_id

        time_based_condition: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.time_based_condition, Unset):
            time_based_condition = self.time_based_condition.to_dict()

        issue_based_condition: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.issue_based_condition, Unset):
            issue_based_condition = self.issue_based_condition.to_dict()

        credit_based_condition: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.credit_based_condition, Unset):
            credit_based_condition = self.credit_based_condition.to_dict()

        price_issue_id = self.price_issue_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "contractType": contract_type,
                "productContractId": product_contract_id,
                "archived": archived,
            }
        )
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_by_type is not UNSET:
            field_dict["createdByType"] = created_by_type
        if changed_by is not UNSET:
            field_dict["changedBy"] = changed_by
        if changed_by_type is not UNSET:
            field_dict["changedByType"] = changed_by_type
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
        if price_issue_id is not UNSET:
            field_dict["priceIssueId"] = price_issue_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.credit_based_product_contract_condition import CreditBasedProductContractCondition
        from ..models.issue_based_product_contract_condition import IssueBasedProductContractCondition
        from ..models.time_based_product_contract_condition import TimeBasedProductContractCondition

        d = src_dict.copy()
        title = d.pop("title")

        contract_type = ProductContractBaseContractType(d.pop("contractType"))

        product_contract_id = d.pop("productContractId")

        archived = d.pop("archived")

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

        created_by = d.pop("createdBy", UNSET)

        _created_by_type = d.pop("createdByType", UNSET)
        created_by_type: Union[Unset, UserType]
        if isinstance(_created_by_type, Unset) or not _created_by_type:
            created_by_type = UNSET
        else:
            created_by_type = UserType(_created_by_type)

        changed_by = d.pop("changedBy", UNSET)

        _changed_by_type = d.pop("changedByType", UNSET)
        changed_by_type: Union[Unset, UserType]
        if isinstance(_changed_by_type, Unset) or not _changed_by_type:
            changed_by_type = UNSET
        else:
            changed_by_type = UserType(_changed_by_type)

        leaf_id = d.pop("leafId", UNSET)

        description = d.pop("description", UNSET)

        product_tag_ids = cast(list[int], d.pop("productTagIds", UNSET))

        ivw_rule_id = d.pop("ivwRuleId", UNSET)

        _time_based_condition = d.pop("timeBasedCondition", UNSET)
        time_based_condition: Union[Unset, TimeBasedProductContractCondition]
        if isinstance(_time_based_condition, Unset) or not _time_based_condition:
            time_based_condition = UNSET
        else:
            time_based_condition = TimeBasedProductContractCondition.from_dict(_time_based_condition)

        _issue_based_condition = d.pop("issueBasedCondition", UNSET)
        issue_based_condition: Union[Unset, IssueBasedProductContractCondition]
        if isinstance(_issue_based_condition, Unset) or not _issue_based_condition:
            issue_based_condition = UNSET
        else:
            issue_based_condition = IssueBasedProductContractCondition.from_dict(_issue_based_condition)

        _credit_based_condition = d.pop("creditBasedCondition", UNSET)
        credit_based_condition: Union[Unset, CreditBasedProductContractCondition]
        if isinstance(_credit_based_condition, Unset) or not _credit_based_condition:
            credit_based_condition = UNSET
        else:
            credit_based_condition = CreditBasedProductContractCondition.from_dict(_credit_based_condition)

        price_issue_id = d.pop("priceIssueId", UNSET)

        product_contract = cls(
            title=title,
            contract_type=contract_type,
            product_contract_id=product_contract_id,
            archived=archived,
            created_date=created_date,
            changed_date=changed_date,
            created_by=created_by,
            created_by_type=created_by_type,
            changed_by=changed_by,
            changed_by_type=changed_by_type,
            leaf_id=leaf_id,
            description=description,
            product_tag_ids=product_tag_ids,
            ivw_rule_id=ivw_rule_id,
            time_based_condition=time_based_condition,
            issue_based_condition=issue_based_condition,
            credit_based_condition=credit_based_condition,
            price_issue_id=price_issue_id,
        )

        product_contract.additional_properties = d
        return product_contract

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
