import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="BankAccountCreation")


@_attrs_define
class BankAccountCreation:
    """
    Attributes:
        owner (str): name on bank account
        iban (str): <a href="https://en.wikipedia.org/wiki/International_Bank_Account_Number" target="_blank">IBAN</a>
        customer_id (str): unique id of the payment mandate - if not sent plenigo will generate a new one together with
            a mandate date
        bic (Union[Unset, str]): <a href="https://en.wikipedia.org/wiki/ISO_9362" target="_blank">BIC</a> - only
            necessary for countries outside the EU
        preferred (Union[Unset, bool]): flag indicating if bank account is the preferred bank account - only one bank
            account can be preferred.
        invalid (Union[Unset, bool]): flag indicating if payment method should be handled as invalid
        mandate_id (Union[Unset, str]): unique id of the payment mandate
        mandate_date (Union[None, Unset, datetime.datetime]): date the payment mandate was created with date-time
            notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339,
            section 5.6</a>, for example, 2017-07-21T17:32:28Z
        psp_mandate_id (Union[Unset, str]): psp mandate id
    """

    owner: str
    iban: str
    customer_id: str
    bic: Union[Unset, str] = UNSET
    preferred: Union[Unset, bool] = UNSET
    invalid: Union[Unset, bool] = UNSET
    mandate_id: Union[Unset, str] = UNSET
    mandate_date: Union[None, Unset, datetime.datetime] = UNSET
    psp_mandate_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        owner = self.owner

        iban = self.iban

        customer_id = self.customer_id

        bic = self.bic

        preferred = self.preferred

        invalid = self.invalid

        mandate_id = self.mandate_id

        mandate_date: Union[None, Unset, str]
        if isinstance(self.mandate_date, Unset) or self.mandate_date is None:
            mandate_date = UNSET
        elif isinstance(self.mandate_date, datetime.datetime):
            mandate_date = self.mandate_date.isoformat()
        else:
            mandate_date = self.mandate_date

        psp_mandate_id = self.psp_mandate_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "owner": owner,
                "iban": iban,
                "customerId": customer_id,
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        owner = d.pop("owner")

        iban = d.pop("iban")

        customer_id = d.pop("customerId")

        bic = d.pop("bic", UNSET)

        preferred = d.pop("preferred", UNSET)

        invalid = d.pop("invalid", UNSET)

        mandate_id = d.pop("mandateId", UNSET)

        def _parse_mandate_date(data: object) -> Union[None, Unset, datetime.datetime]:
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
                mandate_date_type_0 = isoparse(data)

                return mandate_date_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        mandate_date = _parse_mandate_date(d.pop("mandateDate", UNSET))

        psp_mandate_id = d.pop("pspMandateId", UNSET)

        bank_account_creation = cls(
            owner=owner,
            iban=iban,
            customer_id=customer_id,
            bic=bic,
            preferred=preferred,
            invalid=invalid,
            mandate_id=mandate_id,
            mandate_date=mandate_date,
            psp_mandate_id=psp_mandate_id,
        )

        bank_account_creation.additional_properties = d
        return bank_account_creation

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
