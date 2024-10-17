import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.refund_status_change_status import RefundStatusChangeStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="SchemasStatusHistory")


@_attrs_define
class SchemasStatusHistory:
    """
    Attributes:
        status (RefundStatusChangeStatus): status of the refund
        reason (Union[Unset, str]): reason for status change
        change_date (Union[None, Unset, datetime.datetime]): date the refund was changed with date-time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 2017-07-21T17:32:28Z
    """

    status: RefundStatusChangeStatus
    reason: Union[Unset, str] = UNSET
    change_date: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        reason = self.reason

        change_date: Union[None, Unset, str]
        if isinstance(self.change_date, Unset) or self.change_date is None:
            change_date = UNSET
        elif isinstance(self.change_date, datetime.datetime):
            change_date = self.change_date.isoformat()
        else:
            change_date = self.change_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason
        if change_date is not UNSET:
            field_dict["changeDate"] = change_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = RefundStatusChangeStatus(d.pop("status"))

        reason = d.pop("reason", UNSET)

        def _parse_change_date(data: object) -> Union[None, Unset, datetime.datetime]:
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
                change_date_type_1 = isoparse(data)

                return change_date_type_1
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        change_date = _parse_change_date(d.pop("changeDate", UNSET))

        schemas_status_history = cls(
            status=status,
            reason=reason,
            change_date=change_date,
        )

        schemas_status_history.additional_properties = d
        return schemas_status_history

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
