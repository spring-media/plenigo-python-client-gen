import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="IDealAccount")


@_attrs_define
class IDealAccount:
    """
    Attributes:
        owner (str): name on bank account
        obfuscated_iban (str): obfuscated IBAN
        psp_account_id (str): payment service provider iDeal account id
        fingerprint (str): fingerprint to check account uniqueness
        preferred (bool): flag indicating if iDeal account is the preferred one
        invalid (Union[Unset, bool]): flag indicating if payment method should be handled as invalid
        created_date (Union[None, Unset, datetime.datetime]): time the object was created with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        changed_date (Union[None, Unset, datetime.datetime]): time the object was changed with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        i_deal_account_id (Union[Unset, int]): unique id of the iDeal account
        active (Union[Unset, bool]): flag indicating if iDeal account is active - an iDeal account can become inactive
            by getting closed, etc.
    """

    owner: str
    obfuscated_iban: str
    psp_account_id: str
    fingerprint: str
    preferred: bool
    invalid: Union[Unset, bool] = UNSET
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    i_deal_account_id: Union[Unset, int] = UNSET
    active: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        owner = self.owner

        obfuscated_iban = self.obfuscated_iban

        psp_account_id = self.psp_account_id

        fingerprint = self.fingerprint

        preferred = self.preferred

        invalid = self.invalid

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

        i_deal_account_id = self.i_deal_account_id

        active = self.active

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "owner": owner,
                "obfuscatedIban": obfuscated_iban,
                "pspAccountId": psp_account_id,
                "fingerprint": fingerprint,
                "preferred": preferred,
            }
        )
        if invalid is not UNSET:
            field_dict["invalid"] = invalid
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if i_deal_account_id is not UNSET:
            field_dict["iDealAccountId"] = i_deal_account_id
        if active is not UNSET:
            field_dict["active"] = active

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        owner = d.pop("owner")

        obfuscated_iban = d.pop("obfuscatedIban")

        psp_account_id = d.pop("pspAccountId")

        fingerprint = d.pop("fingerprint")

        preferred = d.pop("preferred")

        invalid = d.pop("invalid", UNSET)

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
                created_date_type_1 = isoparse(data)

                return created_date_type_1
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
                changed_date_type_1 = isoparse(data)

                return changed_date_type_1
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        changed_date = _parse_changed_date(d.pop("changedDate", UNSET))

        i_deal_account_id = d.pop("iDealAccountId", UNSET)

        active = d.pop("active", UNSET)

        i_deal_account = cls(
            owner=owner,
            obfuscated_iban=obfuscated_iban,
            psp_account_id=psp_account_id,
            fingerprint=fingerprint,
            preferred=preferred,
            invalid=invalid,
            created_date=created_date,
            changed_date=changed_date,
            i_deal_account_id=i_deal_account_id,
            active=active,
        )

        i_deal_account.additional_properties = d
        return i_deal_account

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
