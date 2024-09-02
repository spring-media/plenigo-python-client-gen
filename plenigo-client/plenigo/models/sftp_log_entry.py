import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SftpLogEntry")


@_attrs_define
class SftpLogEntry:
    """
    Attributes:
        created_date (Union[None, Unset, datetime.datetime]): Time the object was created in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        changed_date (Union[None, Unset, datetime.datetime]): Time the object was changed in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        sftp_log_entry_id (Union[Unset, int]): unique id of the sftp log entry
        server (Union[Unset, str]): sftp server used
        username (Union[Unset, str]): username used to connect
        target_directory (Union[Unset, str]): target directory used
        success (Union[Unset, bool]): flag indicating if call succeeded
        error_msg (Union[Unset, str]): error message in case of an error
    """

    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    sftp_log_entry_id: Union[Unset, int] = UNSET
    server: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    target_directory: Union[Unset, str] = UNSET
    success: Union[Unset, bool] = UNSET
    error_msg: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

        sftp_log_entry_id = self.sftp_log_entry_id

        server = self.server

        username = self.username

        target_directory = self.target_directory

        success = self.success

        error_msg = self.error_msg

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if sftp_log_entry_id is not UNSET:
            field_dict["sftpLogEntryId"] = sftp_log_entry_id
        if server is not UNSET:
            field_dict["server"] = server
        if username is not UNSET:
            field_dict["username"] = username
        if target_directory is not UNSET:
            field_dict["targetDirectory"] = target_directory
        if success is not UNSET:
            field_dict["success"] = success
        if error_msg is not UNSET:
            field_dict["errorMsg"] = error_msg

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

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

        sftp_log_entry_id = d.pop("sftpLogEntryId", UNSET)

        server = d.pop("server", UNSET)

        username = d.pop("username", UNSET)

        target_directory = d.pop("targetDirectory", UNSET)

        success = d.pop("success", UNSET)

        error_msg = d.pop("errorMsg", UNSET)

        sftp_log_entry = cls(
            created_date=created_date,
            changed_date=changed_date,
            sftp_log_entry_id=sftp_log_entry_id,
            server=server,
            username=username,
            target_directory=target_directory,
            success=success,
            error_msg=error_msg,
        )

        sftp_log_entry.additional_properties = d
        return sftp_log_entry

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
