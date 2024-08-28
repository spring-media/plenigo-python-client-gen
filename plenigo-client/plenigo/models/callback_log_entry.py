import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_base_changed_by_type import ApiBaseChangedByType
from ..models.api_base_created_by_type import ApiBaseCreatedByType
from ..models.callback_log_entry_callback_type import CallbackLogEntryCallbackType
from ..models.callback_log_entry_entity_type import CallbackLogEntryEntityType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CallbackLogEntry")


@_attrs_define
class CallbackLogEntry:
    """
    Attributes:
        created_date (Union[None, Unset, datetime.datetime]): Time the object was created in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        changed_date (Union[None, Unset, datetime.datetime]): Time the object was changed in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        created_by (Union[Unset, str]): ID of who created the object
        created_by_type (Union[Unset, ApiBaseCreatedByType]): Type of creator
        changed_by (Union[Unset, str]): ID of who changed the object
        changed_by_type (Union[Unset, ApiBaseChangedByType]): Type of changer
        callback_log_entry_id (Union[Unset, int]): unique id of the callback log entry
        entity_type (Union[Unset, CallbackLogEntryEntityType]): entity type to get entries for
        callback_type (Union[Unset, CallbackLogEntryCallbackType]): callback type to get entries for
        entity_version (Union[Unset, str]): version of the entity returned
        entity_id (Union[Unset, str]): unique id inside a contract company of the entity that changed
        success (Union[Unset, bool]): flag indicating if callback was successful
        error_msg (Union[Unset, str]): description of the error occurred
        msg (Union[Unset, str]): description
    """

    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_by_type: Union[Unset, ApiBaseCreatedByType] = UNSET
    changed_by: Union[Unset, str] = UNSET
    changed_by_type: Union[Unset, ApiBaseChangedByType] = UNSET
    callback_log_entry_id: Union[Unset, int] = UNSET
    entity_type: Union[Unset, CallbackLogEntryEntityType] = UNSET
    callback_type: Union[Unset, CallbackLogEntryCallbackType] = UNSET
    entity_version: Union[Unset, str] = UNSET
    entity_id: Union[Unset, str] = UNSET
    success: Union[Unset, bool] = UNSET
    error_msg: Union[Unset, str] = UNSET
    msg: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_date: Union[None, Unset, str]
        if isinstance(self.created_date, Unset):
            created_date = UNSET
        elif isinstance(self.created_date, datetime.datetime):
            created_date = self.created_date.isoformat()
        else:
            created_date = self.created_date

        changed_date: Union[None, Unset, str]
        if isinstance(self.changed_date, Unset):
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

        callback_log_entry_id = self.callback_log_entry_id

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
        if callback_log_entry_id is not UNSET:
            field_dict["callbackLogEntryId"] = callback_log_entry_id
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

        def _parse_created_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
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
            if isinstance(data, Unset):
                return data
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
        created_by_type: Union[Unset, ApiBaseCreatedByType]
        if isinstance(_created_by_type, Unset) or not _created_by_type:
            created_by_type = UNSET
        else:
            created_by_type = ApiBaseCreatedByType(_created_by_type)

        changed_by = d.pop("changedBy", UNSET)

        _changed_by_type = d.pop("changedByType", UNSET)
        changed_by_type: Union[Unset, ApiBaseChangedByType]
        if isinstance(_changed_by_type, Unset) or not _changed_by_type:
            changed_by_type = UNSET
        else:
            changed_by_type = ApiBaseChangedByType(_changed_by_type)

        callback_log_entry_id = d.pop("callbackLogEntryId", UNSET)

        _entity_type = d.pop("entityType", UNSET)
        entity_type: Union[Unset, CallbackLogEntryEntityType]
        if isinstance(_entity_type, Unset) or not _entity_type:
            entity_type = UNSET
        else:
            entity_type = CallbackLogEntryEntityType(_entity_type)

        _callback_type = d.pop("callbackType", UNSET)
        callback_type: Union[Unset, CallbackLogEntryCallbackType]
        if isinstance(_callback_type, Unset) or not _callback_type:
            callback_type = UNSET
        else:
            callback_type = CallbackLogEntryCallbackType(_callback_type)

        entity_version = d.pop("entityVersion", UNSET)

        entity_id = d.pop("entityId", UNSET)

        success = d.pop("success", UNSET)

        error_msg = d.pop("errorMsg", UNSET)

        msg = d.pop("msg", UNSET)

        callback_log_entry = cls(
            created_date=created_date,
            changed_date=changed_date,
            created_by=created_by,
            created_by_type=created_by_type,
            changed_by=changed_by,
            changed_by_type=changed_by_type,
            callback_log_entry_id=callback_log_entry_id,
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
