import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.customer_session_type import CustomerSessionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomerSession")


@attr.s(auto_attribs=True)
class CustomerSession:
    """
    Attributes:
        id (Union[Unset, str]): unique id of the session
        customer_id (Union[Unset, str]): unique id of the customer within a contract company
        contract_company_id (Union[Unset, str]): id of the contract company the customer belongs to
        company_id (Union[Unset, str]): id of the company the customer belongs to
        created (Union[Unset, datetime.datetime]): time the session was createdwith date-time notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-21T17:32:28Z
        type (Union[Unset, CustomerSessionType]): type of the session
    """

    id: Union[Unset, str] = UNSET
    customer_id: Union[Unset, str] = UNSET
    contract_company_id: Union[Unset, str] = UNSET
    company_id: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    type: Union[Unset, CustomerSessionType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        customer_id = self.customer_id
        contract_company_id = self.contract_company_id
        company_id = self.company_id
        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if contract_company_id is not UNSET:
            field_dict["contractCompanyId"] = contract_company_id
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if created is not UNSET:
            field_dict["created"] = created
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        customer_id = d.pop("customerId", UNSET)

        contract_company_id = d.pop("contractCompanyId", UNSET)

        company_id = d.pop("companyId", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _type = d.pop("type", UNSET)
        type: Union[Unset, CustomerSessionType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = CustomerSessionType(_type)

        customer_session = cls(
            id=id,
            customer_id=customer_id,
            contract_company_id=contract_company_id,
            company_id=company_id,
            created=created,
            type=type,
        )

        customer_session.additional_properties = d
        return customer_session

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
