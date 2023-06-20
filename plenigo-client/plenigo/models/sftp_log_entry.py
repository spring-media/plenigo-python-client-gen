import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SftpLogEntry")


@attr.s(auto_attribs=True)
class SftpLogEntry:
    """
    Attributes:
        sftp_log_entry_id (Union[Unset, int]): unique id of the sftp log entry
        changed_date (Union[Unset, datetime.datetime]): date time the sftp log entry entity was changed with date-time
            notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339,
            section 5.6</a>, for example, 2017-07-21T17:32:28Z
        server (Union[Unset, str]): sftp server used
        username (Union[Unset, str]): username used to connect
        target_directory (Union[Unset, str]): target directory used
        success (Union[Unset, bool]): flag indicating if call succeeded
        error_msg (Union[Unset, str]): error message in case of an error
    """

    sftp_log_entry_id: Union[Unset, int] = UNSET
    changed_date: Union[Unset, datetime.datetime] = UNSET
    server: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    target_directory: Union[Unset, str] = UNSET
    success: Union[Unset, bool] = UNSET
    error_msg: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sftp_log_entry_id = self.sftp_log_entry_id
        changed_date: Union[Unset, str] = UNSET
        if not isinstance(self.changed_date, Unset):
            changed_date = self.changed_date.isoformat()

        server = self.server
        username = self.username
        target_directory = self.target_directory
        success = self.success
        error_msg = self.error_msg

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sftp_log_entry_id is not UNSET:
            field_dict["sftpLogEntryId"] = sftp_log_entry_id
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
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
        sftp_log_entry_id = d.pop("sftpLogEntryId", UNSET)

        _changed_date = d.pop("changedDate", UNSET)
        changed_date: Union[Unset, datetime.datetime]
        if isinstance(_changed_date, Unset):
            changed_date = UNSET
        else:
            changed_date = isoparse(_changed_date)

        server = d.pop("server", UNSET)

        username = d.pop("username", UNSET)

        target_directory = d.pop("targetDirectory", UNSET)

        success = d.pop("success", UNSET)

        error_msg = d.pop("errorMsg", UNSET)

        sftp_log_entry = cls(
            sftp_log_entry_id=sftp_log_entry_id,
            changed_date=changed_date,
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
