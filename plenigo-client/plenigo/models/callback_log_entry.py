import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.callback_log_entry_callback_type import CallbackLogEntryCallbackType
from ..models.callback_log_entry_entity_type import CallbackLogEntryEntityType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CallbackLogEntry")


@attr.s(auto_attribs=True)
class CallbackLogEntry:
    """
    Attributes:
        callback_log_entry_id (Union[Unset, int]): unique id of the callback log entry
        changed_date (Union[Unset, datetime.datetime]): date time the callback log entry entity was changed with date-
            time notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339,
            section 5.6</a>, for example, 2017-07-21T17:32:28Z
        entity_type (Union[Unset, CallbackLogEntryEntityType]): entity type to get entries for
        callback_type (Union[Unset, CallbackLogEntryCallbackType]): callback type to get entries for
        entity_version (Union[Unset, str]): version of the entity returned
        entity_id (Union[Unset, str]): unique id inside a contract company of the entity that changed
        success (Union[Unset, bool]): flag indicating if callback was successful
        error_msg (Union[Unset, str]): description of the error occured
        msg (Union[Unset, str]): description
    """

    callback_log_entry_id: Union[Unset, int] = UNSET
    changed_date: Union[Unset, datetime.datetime] = UNSET
    entity_type: Union[Unset, CallbackLogEntryEntityType] = UNSET
    callback_type: Union[Unset, CallbackLogEntryCallbackType] = UNSET
    entity_version: Union[Unset, str] = UNSET
    entity_id: Union[Unset, str] = UNSET
    success: Union[Unset, bool] = UNSET
    error_msg: Union[Unset, str] = UNSET
    msg: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        callback_log_entry_id = self.callback_log_entry_id
        changed_date: Union[Unset, str] = UNSET
        if not isinstance(self.changed_date, Unset):
            changed_date = self.changed_date.isoformat()

        entity_type: Union[Unset, str] = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type.value

        callback_type: Union[Unset, str] = UNSET
        if not isinstance(self.callback_type, Unset):
            callback_type = self.callback_type.value

        entity_version = self.entity_version
        entity_id = self.entity_id
        success = self.success
        error_msg = self.error_msg
        msg = self.msg

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if callback_log_entry_id is not UNSET:
            field_dict["callbackLogEntryId"] = callback_log_entry_id
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if callback_type is not UNSET:
            field_dict["callbackType"] = callback_type
        if entity_version is not UNSET:
            field_dict["entityVersion"] = entity_version
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if success is not UNSET:
            field_dict["success"] = success
        if error_msg is not UNSET:
            field_dict["errorMsg"] = error_msg
        if msg is not UNSET:
            field_dict["msg"] = msg

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        callback_log_entry_id = d.pop("callbackLogEntryId", UNSET)

        _changed_date = d.pop("changedDate", UNSET)
        changed_date: Union[Unset, datetime.datetime]
        if isinstance(_changed_date, Unset):
            changed_date = UNSET
        else:
            changed_date = isoparse(_changed_date)

        _entity_type = d.pop("entityType", UNSET)
        entity_type: Union[Unset, CallbackLogEntryEntityType]
        if isinstance(_entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = CallbackLogEntryEntityType(_entity_type)

        _callback_type = d.pop("callbackType", UNSET)
        callback_type: Union[Unset, CallbackLogEntryCallbackType]
        if isinstance(_callback_type, Unset):
            callback_type = UNSET
        else:
            callback_type = CallbackLogEntryCallbackType(_callback_type)

        entity_version = d.pop("entityVersion", UNSET)

        entity_id = d.pop("entityId", UNSET)

        success = d.pop("success", UNSET)

        error_msg = d.pop("errorMsg", UNSET)

        msg = d.pop("msg", UNSET)

        callback_log_entry = cls(
            callback_log_entry_id=callback_log_entry_id,
            changed_date=changed_date,
            entity_type=entity_type,
            callback_type=callback_type,
            entity_version=entity_version,
            entity_id=entity_id,
            success=success,
            error_msg=error_msg,
            msg=msg,
        )

        callback_log_entry.additional_properties = d
        return callback_log_entry

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
