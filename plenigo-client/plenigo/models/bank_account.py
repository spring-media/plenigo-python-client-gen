import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.user_type import UserType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BankAccount")


@_attrs_define
class BankAccount:
    """
    Attributes:
        owner (str): name on bank account
        iban (str): <a href="https://en.wikipedia.org/wiki/International_Bank_Account_Number" target="_blank">IBAN</a>
        customer_id (str): unique id of the payment mandate - if not sent plenigo will generate a new one together with
            a mandate date
        bank_account_id (int): unique id of the bank account
        bic (Union[Unset, str]): <a href="https://en.wikipedia.org/wiki/ISO_9362" target="_blank">BIC</a> - only
            necessary for countries outside the EU
        preferred (Union[Unset, bool]): flag indicating if bank account is the preferred bank account - only one bank
            account can be preferred.
        invalid (Union[Unset, bool]): flag indicating if payment method should be handled as invalid
        mandate_id (Union[Unset, str]): unique id of the payment mandate
        mandate_date (Union[None, Unset, datetime.date]): date the payment mandate was created with date-time notation
            as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section
            5.6</a>, for example, 2017-07-21T17:32:28Z
        psp_mandate_id (Union[Unset, str]): psp mandate id
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
        active (Union[Unset, bool]): flag indicating if bank account is active - a bank account can become inactive by
            getting closed, etc.
    """

    owner: str
    iban: str
    customer_id: str
    bank_account_id: int
    bic: Union[Unset, str] = UNSET
    preferred: Union[Unset, bool] = UNSET
    invalid: Union[Unset, bool] = UNSET
    mandate_id: Union[Unset, str] = UNSET
    mandate_date: Union[None, Unset, datetime.date] = UNSET
    psp_mandate_id: Union[Unset, str] = UNSET
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_by_type: Union[Unset, UserType] = UNSET
    changed_by: Union[Unset, str] = UNSET
    changed_by_type: Union[Unset, UserType] = UNSET
    active: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        owner = self.owner

        iban = self.iban

        customer_id = self.customer_id

        bank_account_id = self.bank_account_id

        bic = self.bic

        preferred = self.preferred

        invalid = self.invalid

        mandate_id = self.mandate_id

        mandate_date: Union[None, Unset, str]
        if isinstance(self.mandate_date, Unset) or self.mandate_date is None:
            mandate_date = UNSET
        elif isinstance(self.mandate_date, datetime.date):
            mandate_date = self.mandate_date.isoformat()
        else:
            mandate_date = self.mandate_date

        psp_mandate_id = self.psp_mandate_id

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

        active = self.active

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "owner": owner,
                "iban": iban,
                "customerId": customer_id,
                "bankAccountId": bank_account_id,
            }
        )
        if bic is not UNSET:
            field_dict["bic"] = bic
        if preferred is not UNSET:
            field_dict["preferred"] = preferred
        if invalid is not UNSET:
            field_dict["invalid"] = invalid
        if mandate_id is not UNSET:
            field_dict["mandateId"] = mandate_id
        if mandate_date is not UNSET:
            field_dict["mandateDate"] = mandate_date
        if psp_mandate_id is not UNSET:
            field_dict["pspMandateId"] = psp_mandate_id
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
        if active is not UNSET:
            field_dict["active"] = active

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        owner = d.pop("owner")

        iban = d.pop("iban")

        customer_id = d.pop("customerId")

        bank_account_id = d.pop("bankAccountId")

        bic = d.pop("bic", UNSET)

        preferred = d.pop("preferred", UNSET)

        invalid = d.pop("invalid", UNSET)

        mandate_id = d.pop("mandateId", UNSET)

        def _parse_mandate_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data

            if data is None:
                return data

            if isinstance(data, Unset):
                return data

            # Try to parse the data as datetime.date
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mandate_date_type_0 = isoparse(data).date()

                return mandate_date_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.date], data)

        mandate_date = _parse_mandate_date(d.pop("mandateDate", UNSET))

        psp_mandate_id = d.pop("pspMandateId", UNSET)

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

        active = d.pop("active", UNSET)

        bank_account = cls(
            owner=owner,
            iban=iban,
            customer_id=customer_id,
            bank_account_id=bank_account_id,
            bic=bic,
            preferred=preferred,
            invalid=invalid,
            mandate_id=mandate_id,
            mandate_date=mandate_date,
            psp_mandate_id=psp_mandate_id,
            created_date=created_date,
            changed_date=changed_date,
            created_by=created_by,
            created_by_type=created_by_type,
            changed_by=changed_by,
            changed_by_type=changed_by_type,
            active=active,
        )

        bank_account.additional_properties = d
        return bank_account

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
