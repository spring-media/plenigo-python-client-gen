import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_base_changed_by_type import ApiBaseChangedByType
from ..models.api_base_created_by_type import ApiBaseCreatedByType
from ..models.credit_wallet_update_credit_validity_timespan import CreditWalletUpdateCreditValidityTimespan
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credit_wallet_translation import CreditWalletTranslation


T = TypeVar("T", bound="CreditWallet")


@_attrs_define
class CreditWallet:
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
        created_date (Union[None, Unset, datetime.datetime]): Time the object was created in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        changed_date (Union[None, Unset, datetime.datetime]): Time the object was changed in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        created_by (Union[Unset, str]): ID of who created the object
        created_by_type (Union[Unset, ApiBaseCreatedByType]): Type of creator
        changed_by (Union[Unset, str]): ID of who changed the object
        changed_by_type (Union[Unset, ApiBaseChangedByType]): Type of changer
        credit_wallet_id (Union[Unset, int]): unique id of a wallet within a contract company
    """

    internal_title: Union[Unset, str] = UNSET
    credit_count_invalidation: Union[Unset, bool] = UNSET
    credit_validity_time: Union[Unset, int] = UNSET
    credit_validity_timespan: Union[Unset, CreditWalletUpdateCreditValidityTimespan] = UNSET
    event_list_id: Union[Unset, int] = UNSET
    translations: Union[Unset, List["CreditWalletTranslation"]] = UNSET
    unique_id: Union[Unset, str] = UNSET
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_by_type: Union[Unset, ApiBaseCreatedByType] = UNSET
    changed_by: Union[Unset, str] = UNSET
    changed_by_type: Union[Unset, ApiBaseChangedByType] = UNSET
    credit_wallet_id: Union[Unset, int] = UNSET
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

        credit_wallet_id = self.credit_wallet_id

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
        if credit_wallet_id is not UNSET:
            field_dict["creditWalletId"] = credit_wallet_id

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

        credit_wallet_id = d.pop("creditWalletId", UNSET)

        credit_wallet = cls(
            internal_title=internal_title,
            credit_count_invalidation=credit_count_invalidation,
            credit_validity_time=credit_validity_time,
            credit_validity_timespan=credit_validity_timespan,
            event_list_id=event_list_id,
            translations=translations,
            unique_id=unique_id,
            created_date=created_date,
            changed_date=changed_date,
            created_by=created_by,
            created_by_type=created_by_type,
            changed_by=changed_by,
            changed_by_type=changed_by_type,
            credit_wallet_id=credit_wallet_id,
        )

        credit_wallet.additional_properties = d
        return credit_wallet

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
