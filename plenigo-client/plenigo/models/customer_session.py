import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.customer_session_type import CustomerSessionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomerSession")


@_attrs_define
class CustomerSession:
    """
    Attributes:
        id (Union[Unset, str]): unique id of the session
        customer_id (Union[Unset, str]): unique id of the customer within a contract company
        contract_company_id (Union[Unset, str]): id of the contract company the customer belongs to
        company_id (Union[Unset, str]): id of the company the customer belongs to
        created (Union[None, Unset, datetime.datetime]): time the session was created with date-time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 2017-07-21T17:32:28Z
        type (Union[Unset, CustomerSessionType]): type of the session
    """

    id: Union[Unset, str] = UNSET
    customer_id: Union[Unset, str] = UNSET
    contract_company_id: Union[Unset, str] = UNSET
    company_id: Union[Unset, str] = UNSET
    created: Union[None, Unset, datetime.datetime] = UNSET
    type: Union[Unset, CustomerSessionType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        customer_id = self.customer_id

        contract_company_id = self.contract_company_id

        company_id = self.company_id

        created: Union[None, Unset, str]
        if isinstance(self.created, Unset):
            created = UNSET
        elif isinstance(self.created, datetime.datetime):
            created = self.created.isoformat()
        else:
            created = self.created

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

        def _parse_created(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_type_0 = isoparse(data)

                return created_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        created = _parse_created(d.pop("created", UNSET))

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
