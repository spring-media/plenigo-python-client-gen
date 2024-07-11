import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_base_changed_by_type import ApiBaseChangedByType
from ..models.api_base_created_by_type import ApiBaseCreatedByType
from ..models.credit_card_change_card_type import CreditCardChangeCardType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreditCard")


@_attrs_define
class CreditCard:
    """
    Attributes:
        owner (str): name on credit card
        provider_token (str): unique credit card token provided by the payment service provider to identify credit card
        obfuscated_number (str): obfuscated credit card number
        valid_to (Union[None, datetime.date]): date the credit card is valid to with full-date notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-01 - must be in the future
        credit_card_id (int): unique id of the credit card
        active (bool): flag indicating if credit card is active - a credit card can become inactive by a passed validity
            date, loss, etc.
        card_type (Union[Unset, CreditCardChangeCardType]): type of the credit card provided
        preferred (Union[Unset, bool]): flag indicating if credit card is the preferred credit card - only one credit
            card can be preferred.
        invalid (Union[Unset, bool]): flag indicating if payment method should be handled as invalid
        customer_id (Union[Unset, str]): unique id of the customer the credit card belongs to
        created_date (Union[None, Unset, datetime.datetime]): Time the object was created in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        changed_date (Union[None, Unset, datetime.datetime]): Time the object was changed in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        created_by (Union[Unset, str]): ID of who created the object
        created_by_type (Union[Unset, ApiBaseCreatedByType]): Type of creator
        changed_by (Union[Unset, str]): ID of who changed the object
        changed_by_type (Union[Unset, ApiBaseChangedByType]): Type of changer
        payment_provider (Union[Unset, str]): payment provider credit card is associated with
        issuer (Union[Unset, str]): describes the issuer of the field if available - this can be used to identify
            ApplePay, GooglePay, etc.
    """

    owner: str
    provider_token: str
    obfuscated_number: str
    valid_to: Union[None, datetime.date]
    credit_card_id: int
    active: bool
    card_type: Union[Unset, CreditCardChangeCardType] = UNSET
    preferred: Union[Unset, bool] = UNSET
    invalid: Union[Unset, bool] = UNSET
    customer_id: Union[Unset, str] = UNSET
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_by_type: Union[Unset, ApiBaseCreatedByType] = UNSET
    changed_by: Union[Unset, str] = UNSET
    changed_by_type: Union[Unset, ApiBaseChangedByType] = UNSET
    payment_provider: Union[Unset, str] = UNSET
    issuer: Union[Unset, str] = UNSET
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

        credit_card_id = self.credit_card_id

        active = self.active

        card_type: Union[Unset, str] = UNSET
        if not isinstance(self.card_type, Unset):
            card_type = self.card_type.value

        preferred = self.preferred

        invalid = self.invalid

        customer_id = self.customer_id

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

        payment_provider = self.payment_provider

        issuer = self.issuer

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "owner": owner,
                "providerToken": provider_token,
                "obfuscatedNumber": obfuscated_number,
                "validTo": valid_to,
                "creditCardId": credit_card_id,
                "active": active,
            }
        )
        if card_type is not UNSET:
            field_dict["cardType"] = card_type
        if preferred is not UNSET:
            field_dict["preferred"] = preferred
        if invalid is not UNSET:
            field_dict["invalid"] = invalid
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
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
        if payment_provider is not UNSET:
            field_dict["paymentProvider"] = payment_provider
        if issuer is not UNSET:
            field_dict["issuer"] = issuer

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

        credit_card_id = d.pop("creditCardId")

        active = d.pop("active")

        _card_type = d.pop("cardType", UNSET)
        card_type: Union[Unset, CreditCardChangeCardType]
        if isinstance(_card_type, Unset):
            card_type = UNSET
        else:
            card_type = CreditCardChangeCardType(_card_type)

        preferred = d.pop("preferred", UNSET)

        invalid = d.pop("invalid", UNSET)

        customer_id = d.pop("customerId", UNSET)

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
        if isinstance(_created_by_type, Unset):
            created_by_type = UNSET
        else:
            created_by_type = ApiBaseCreatedByType(_created_by_type)

        changed_by = d.pop("changedBy", UNSET)

        _changed_by_type = d.pop("changedByType", UNSET)
        changed_by_type: Union[Unset, ApiBaseChangedByType]
        if isinstance(_changed_by_type, Unset):
            changed_by_type = UNSET
        else:
            changed_by_type = ApiBaseChangedByType(_changed_by_type)

        payment_provider = d.pop("paymentProvider", UNSET)

        issuer = d.pop("issuer", UNSET)

        credit_card = cls(
            owner=owner,
            provider_token=provider_token,
            obfuscated_number=obfuscated_number,
            valid_to=valid_to,
            credit_card_id=credit_card_id,
            active=active,
            card_type=card_type,
            preferred=preferred,
            invalid=invalid,
            customer_id=customer_id,
            created_date=created_date,
            changed_date=changed_date,
            created_by=created_by,
            created_by_type=created_by_type,
            changed_by=changed_by,
            changed_by_type=changed_by_type,
            payment_provider=payment_provider,
            issuer=issuer,
        )

        credit_card.additional_properties = d
        return credit_card

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
