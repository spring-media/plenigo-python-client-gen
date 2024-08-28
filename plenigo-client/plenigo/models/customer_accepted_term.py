import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomerAcceptedTerm")


@_attrs_define
class CustomerAcceptedTerm:
    """
    Attributes:
        term_id (Union[Unset, int]): technical id of the term for relation to the merchant backend term id
        unique_id (Union[Unset, str]): unique id of the last active term
        acceptance_date (Union[None, Unset, datetime.datetime]): date time the term was accepted with date-time notation
            as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section
            5.6</a>, for example, 2017-07-21T17:32:28Z
    """

    term_id: Union[Unset, int] = UNSET
    unique_id: Union[Unset, str] = UNSET
    acceptance_date: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        term_id = self.term_id

        unique_id = self.unique_id

        acceptance_date: Union[None, Unset, str]
        if isinstance(self.acceptance_date, Unset):
            acceptance_date = UNSET
        elif isinstance(self.acceptance_date, datetime.datetime):
            acceptance_date = self.acceptance_date.isoformat()
        else:
            acceptance_date = self.acceptance_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if term_id is not UNSET:
            field_dict["termId"] = term_id
        if unique_id is not UNSET:
            field_dict["uniqueId"] = unique_id
        if acceptance_date is not UNSET:
            field_dict["acceptanceDate"] = acceptance_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        term_id = d.pop("termId", UNSET)

        unique_id = d.pop("uniqueId", UNSET)

        def _parse_acceptance_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                acceptance_date_type_0 = isoparse(data)

                return acceptance_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        acceptance_date = _parse_acceptance_date(d.pop("acceptanceDate", UNSET))

        customer_accepted_term = cls(
            term_id=term_id,
            unique_id=unique_id,
            acceptance_date=acceptance_date,
        )

        customer_accepted_term.additional_properties = d
        return customer_accepted_term

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
