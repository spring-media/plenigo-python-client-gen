import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.credit_card_change_card_type import CreditCardChangeCardType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreditCardChange")


@_attrs_define
class CreditCardChange:
    """
    Attributes:
        owner (str): name on credit card
        provider_token (str): unique credit card token provided by the payment service provider to identify credit card
        obfuscated_number (str): obfuscated credit card number
        valid_to (Union[None, datetime.date]): date the credit card is valid to with full-date notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-01 - must be in the future
        card_type (Union[Unset, CreditCardChangeCardType]): type of the credit card provided
        preferred (Union[Unset, bool]): flag indicating if credit card is the preferred credit card - only one credit
            card can be preferred.
        invalid (Union[Unset, bool]): flag indicating if payment method should be handled as invalid
    """

    owner: str
    provider_token: str
    obfuscated_number: str
    valid_to: Union[None, datetime.date]
    card_type: Union[Unset, CreditCardChangeCardType] = UNSET
    preferred: Union[Unset, bool] = UNSET
    invalid: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        owner = self.owner

        provider_token = self.provider_token

        obfuscated_number = self.obfuscated_number

        valid_to: Union[None, str]
        if isinstance(self.valid_to, datetime.date):
            valid_to = self.valid_to.isoformat()
        else:
            valid_to = self.valid_to

        card_type: Union[Unset, str] = UNSET
        if not isinstance(self.card_type, Unset):
            card_type = self.card_type.value

        preferred = self.preferred

        invalid = self.invalid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "owner": owner,
                "providerToken": provider_token,
                "obfuscatedNumber": obfuscated_number,
                "validTo": valid_to,
            }
        )
        if card_type is not UNSET:
            field_dict["cardType"] = card_type
        if preferred is not UNSET:
            field_dict["preferred"] = preferred
        if invalid is not UNSET:
            field_dict["invalid"] = invalid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        owner = d.pop("owner")

        provider_token = d.pop("providerToken")

        obfuscated_number = d.pop("obfuscatedNumber")

        def _parse_valid_to(data: object) -> Union[None, datetime.date]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                valid_to_type_0 = isoparse(data).date()

                return valid_to_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.date], data)

        valid_to = _parse_valid_to(d.pop("validTo"))

        _card_type = d.pop("cardType", UNSET)
        card_type: Union[Unset, CreditCardChangeCardType]
        if isinstance(_card_type, Unset) or not _card_type:
            card_type = UNSET
        else:
            card_type = CreditCardChangeCardType(_card_type)

        preferred = d.pop("preferred", UNSET)

        invalid = d.pop("invalid", UNSET)

        credit_card_change = cls(
            owner=owner,
            provider_token=provider_token,
            obfuscated_number=obfuscated_number,
            valid_to=valid_to,
            card_type=card_type,
            preferred=preferred,
            invalid=invalid,
        )

        credit_card_change.additional_properties = d
        return credit_card_change

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
