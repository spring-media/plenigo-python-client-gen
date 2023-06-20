import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.mail_log_entry_mail_settings_type import MailLogEntryMailSettingsType
from ..models.mail_log_entry_mail_template_type import MailLogEntryMailTemplateType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mail_log_entry_error_detail import MailLogEntryErrorDetail


T = TypeVar("T", bound="MailLogEntry")


@attr.s(auto_attribs=True)
class MailLogEntry:
    """
    Attributes:
        mail_log_entry_id (Union[Unset, int]): unique id of the mail log entry
        changed_date (Union[Unset, datetime.datetime]): date time the mail log entry entity was changed with date-time
            notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339,
            section 5.6</a>, for example, 2017-07-21T17:32:28Z
        customer_id (Union[Unset, str]): id of the customer the mail was sent to
        mail_settings_type (Union[Unset, MailLogEntryMailSettingsType]): mail settings type configured
        mail_template_type (Union[Unset, MailLogEntryMailTemplateType]): mail template type of the mail sent
        to (Union[Unset, str]): mail receiver email address
        from_ (Union[Unset, str]): mail sender email address
        bcc (Union[Unset, str]): comma separated list of bcc receivers is there are any
        reply_to (Union[Unset, str]): reply to email address
        subject (Union[Unset, str]): Subject of the email sent
        success (Union[Unset, bool]): success state of the email delivery
        error_reason (Union[Unset, str]): reason for failure if success is false
        error_detail (Union[Unset, MailLogEntryErrorDetail]): string or json object with error details
    """

    mail_log_entry_id: Union[Unset, int] = UNSET
    changed_date: Union[Unset, datetime.datetime] = UNSET
    customer_id: Union[Unset, str] = UNSET
    mail_settings_type: Union[Unset, MailLogEntryMailSettingsType] = UNSET
    mail_template_type: Union[Unset, MailLogEntryMailTemplateType] = UNSET
    to: Union[Unset, str] = UNSET
    from_: Union[Unset, str] = UNSET
    bcc: Union[Unset, str] = UNSET
    reply_to: Union[Unset, str] = UNSET
    subject: Union[Unset, str] = UNSET
    success: Union[Unset, bool] = UNSET
    error_reason: Union[Unset, str] = UNSET
    error_detail: Union[Unset, "MailLogEntryErrorDetail"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mail_log_entry_id = self.mail_log_entry_id
        changed_date: Union[Unset, str] = UNSET
        if not isinstance(self.changed_date, Unset):
            changed_date = self.changed_date.isoformat()

        customer_id = self.customer_id
        mail_settings_type: Union[Unset, str] = UNSET
        if not isinstance(self.mail_settings_type, Unset):
            mail_settings_type = self.mail_settings_type.value

        mail_template_type: Union[Unset, str] = UNSET
        if not isinstance(self.mail_template_type, Unset):
            mail_template_type = self.mail_template_type.value

        to = self.to
        from_ = self.from_
        bcc = self.bcc
        reply_to = self.reply_to
        subject = self.subject
        success = self.success
        error_reason = self.error_reason
        error_detail: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.error_detail, Unset):
            error_detail = self.error_detail.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mail_log_entry_id is not UNSET:
            field_dict["mailLogEntryId"] = mail_log_entry_id
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if mail_settings_type is not UNSET:
            field_dict["mailSettingsType"] = mail_settings_type
        if mail_template_type is not UNSET:
            field_dict["mailTemplateType"] = mail_template_type
        if to is not UNSET:
            field_dict["to"] = to
        if from_ is not UNSET:
            field_dict["from"] = from_
        if bcc is not UNSET:
            field_dict["bcc"] = bcc
        if reply_to is not UNSET:
            field_dict["replyTo"] = reply_to
        if subject is not UNSET:
            field_dict["subject"] = subject
        if success is not UNSET:
            field_dict["success"] = success
        if error_reason is not UNSET:
            field_dict["errorReason"] = error_reason
        if error_detail is not UNSET:
            field_dict["errorDetail"] = error_detail

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.mail_log_entry_error_detail import MailLogEntryErrorDetail

        d = src_dict.copy()
        mail_log_entry_id = d.pop("mailLogEntryId", UNSET)

        _changed_date = d.pop("changedDate", UNSET)
        changed_date: Union[Unset, datetime.datetime]
        if isinstance(_changed_date, Unset):
            changed_date = UNSET
        else:
            changed_date = isoparse(_changed_date)

        customer_id = d.pop("customerId", UNSET)

        _mail_settings_type = d.pop("mailSettingsType", UNSET)
        mail_settings_type: Union[Unset, MailLogEntryMailSettingsType]
        if isinstance(_mail_settings_type, Unset):
            mail_settings_type = UNSET
        else:
            mail_settings_type = MailLogEntryMailSettingsType(_mail_settings_type)

        _mail_template_type = d.pop("mailTemplateType", UNSET)
        mail_template_type: Union[Unset, MailLogEntryMailTemplateType]
        if isinstance(_mail_template_type, Unset):
            mail_template_type = UNSET
        else:
            mail_template_type = MailLogEntryMailTemplateType(_mail_template_type)

        to = d.pop("to", UNSET)

        from_ = d.pop("from", UNSET)

        bcc = d.pop("bcc", UNSET)

        reply_to = d.pop("replyTo", UNSET)

        subject = d.pop("subject", UNSET)

        success = d.pop("success", UNSET)

        error_reason = d.pop("errorReason", UNSET)

        _error_detail = d.pop("errorDetail", UNSET)
        error_detail: Union[Unset, MailLogEntryErrorDetail]
        if isinstance(_error_detail, Unset):
            error_detail = UNSET
        else:
            error_detail = MailLogEntryErrorDetail.from_dict(_error_detail)

        mail_log_entry = cls(
            mail_log_entry_id=mail_log_entry_id,
            changed_date=changed_date,
            customer_id=customer_id,
            mail_settings_type=mail_settings_type,
            mail_template_type=mail_template_type,
            to=to,
            from_=from_,
            bcc=bcc,
            reply_to=reply_to,
            subject=subject,
            success=success,
            error_reason=error_reason,
            error_detail=error_detail,
        )

        mail_log_entry.additional_properties = d
        return mail_log_entry

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
