from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.credit_wallet_update_credit_validity_timespan import CreditWalletUpdateCreditValidityTimespan
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credit_wallet_translation import CreditWalletTranslation


T = TypeVar("T", bound="CreditWalletCreation")


@_attrs_define
class CreditWalletCreation:
    """
    Attributes:
        internal_title (Union[Unset, str]): internal title of the wallet
        credit_count_invalidation (Union[Unset, bool]): flag indicating if credit counts will be invalidated after a
            time if no active subscription is associated
        credit_validity_time (Union[Unset, int]): time credits are invalidated if credit count invalidation is active
        credit_validity_timespan (Union[Unset, CreditWalletUpdateCreditValidityTimespan]): time credit validity timespan
        event_list_id (Union[Unset, int]): id of the associated event list
        translations (Union[Unset, List['CreditWalletTranslation']]): translations associated with this customer wallet
        unique_id (Union[Unset, str]): unique id of the wallet for identification
    """

    internal_title: Union[Unset, str] = UNSET
    credit_count_invalidation: Union[Unset, bool] = UNSET
    credit_validity_time: Union[Unset, int] = UNSET
    credit_validity_timespan: Union[Unset, CreditWalletUpdateCreditValidityTimespan] = UNSET
    event_list_id: Union[Unset, int] = UNSET
    translations: Union[Unset, List["CreditWalletTranslation"]] = UNSET
    unique_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        internal_title = self.internal_title

        credit_count_invalidation = self.credit_count_invalidation

        credit_validity_time = self.credit_validity_time

        credit_validity_timespan: Union[Unset, str] = UNSET
        if not isinstance(self.credit_validity_timespan, Unset):
            credit_validity_timespan = self.credit_validity_timespan.value

        event_list_id = self.event_list_id

        translations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.translations, Unset):
            translations = []
            for translations_item_data in self.translations:
                translations_item = translations_item_data.to_dict()
                translations.append(translations_item)

        unique_id = self.unique_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if internal_title is not UNSET:
            field_dict["internalTitle"] = internal_title
        if credit_count_invalidation is not UNSET:
            field_dict["creditCountInvalidation"] = credit_count_invalidation
        if credit_validity_time is not UNSET:
            field_dict["creditValidityTime"] = credit_validity_time
        if credit_validity_timespan is not UNSET:
            field_dict["creditValidityTimespan"] = credit_validity_timespan
        if event_list_id is not UNSET:
            field_dict["eventListId"] = event_list_id
        if translations is not UNSET:
            field_dict["translations"] = translations
        if unique_id is not UNSET:
            field_dict["uniqueId"] = unique_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.credit_wallet_translation import CreditWalletTranslation

        d = src_dict.copy()
        internal_title = d.pop("internalTitle", UNSET)

        credit_count_invalidation = d.pop("creditCountInvalidation", UNSET)

        credit_validity_time = d.pop("creditValidityTime", UNSET)

        _credit_validity_timespan = d.pop("creditValidityTimespan", UNSET)
        credit_validity_timespan: Union[Unset, CreditWalletUpdateCreditValidityTimespan]
        if isinstance(_credit_validity_timespan, Unset) or not _credit_validity_timespan:
            credit_validity_timespan = UNSET
        else:
            credit_validity_timespan = CreditWalletUpdateCreditValidityTimespan(_credit_validity_timespan)

        event_list_id = d.pop("eventListId", UNSET)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = CreditWalletTranslation.from_dict(translations_item_data)

            translations.append(translations_item)

        unique_id = d.pop("uniqueId", UNSET)

        credit_wallet_creation = cls(
            internal_title=internal_title,
            credit_count_invalidation=credit_count_invalidation,
            credit_validity_time=credit_validity_time,
            credit_validity_timespan=credit_validity_timespan,
            event_list_id=event_list_id,
            translations=translations,
            unique_id=unique_id,
        )

        credit_wallet_creation.additional_properties = d
        return credit_wallet_creation

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
