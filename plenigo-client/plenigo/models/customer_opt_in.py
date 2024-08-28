import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_base_changed_by_type import ApiBaseChangedByType
from ..models.api_base_created_by_type import ApiBaseCreatedByType
from ..models.customer_opt_in_creation_included_types_item import CustomerOptInCreationIncludedTypesItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer_opt_in_translation_base import CustomerOptInTranslationBase


T = TypeVar("T", bound="CustomerOptIn")


@_attrs_define
class CustomerOptIn:
    """
    Attributes:
        internal_title (str): internal title of the opt in
        unique_id (str): unique id to associate with the user after user has accepted opt in
        included_types (List[CustomerOptInCreationIncludedTypesItem]): types that are included with this opt-in
        translations (List['CustomerOptInTranslationBase']): translations associated with this opt in
        customer_opt_in_id (int): unique id of the customer opt in
        active (Union[Unset, bool]): flag indicating if opt in is currently active
        created_date (Union[None, Unset, datetime.datetime]): Time the object was created in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        changed_date (Union[None, Unset, datetime.datetime]): Time the object was changed in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        created_by (Union[Unset, str]): ID of who created the object
        created_by_type (Union[Unset, ApiBaseCreatedByType]): Type of creator
        changed_by (Union[Unset, str]): ID of who changed the object
        changed_by_type (Union[Unset, ApiBaseChangedByType]): Type of changer
        activation_time (Union[None, Unset, datetime.datetime]): time opt in was first activated with date-time notation
            as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section
            5.6</a>, for example, 2017-07-21T17:32:28Z
    """

    internal_title: str
    unique_id: str
    included_types: List[CustomerOptInCreationIncludedTypesItem]
    translations: List["CustomerOptInTranslationBase"]
    customer_opt_in_id: int
    active: Union[Unset, bool] = UNSET
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_by_type: Union[Unset, ApiBaseCreatedByType] = UNSET
    changed_by: Union[Unset, str] = UNSET
    changed_by_type: Union[Unset, ApiBaseChangedByType] = UNSET
    activation_time: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        internal_title = self.internal_title

        unique_id = self.unique_id

        included_types = []
        for included_types_item_data in self.included_types:
            included_types_item = included_types_item_data.value
            included_types.append(included_types_item)

        translations = []
        for translations_item_data in self.translations:
            translations_item = translations_item_data.to_dict()
            translations.append(translations_item)

        customer_opt_in_id = self.customer_opt_in_id

        active = self.active

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

        activation_time: Union[None, Unset, str]
        if isinstance(self.activation_time, Unset):
            activation_time = UNSET
        elif isinstance(self.activation_time, datetime.datetime):
            activation_time = self.activation_time.isoformat()
        else:
            activation_time = self.activation_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "internalTitle": internal_title,
                "uniqueId": unique_id,
                "includedTypes": included_types,
                "translations": translations,
                "customerOptInId": customer_opt_in_id,
            }
        )
        if active is not UNSET:
            field_dict["active"] = active
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
        if activation_time is not UNSET:
            field_dict["activationTime"] = activation_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.customer_opt_in_translation_base import CustomerOptInTranslationBase

        d = src_dict.copy()
        internal_title = d.pop("internalTitle")

        unique_id = d.pop("uniqueId")

        included_types = []
        _included_types = d.pop("includedTypes")
        for included_types_item_data in _included_types:
            included_types_item = CustomerOptInCreationIncludedTypesItem(included_types_item_data)

            included_types.append(included_types_item)

        translations = []
        _translations = d.pop("translations")
        for translations_item_data in _translations:
            translations_item = CustomerOptInTranslationBase.from_dict(translations_item_data)

            translations.append(translations_item)

        customer_opt_in_id = d.pop("customerOptInId")

        active = d.pop("active", UNSET)

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

        def _parse_activation_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                activation_time_type_0 = isoparse(data)

                return activation_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        activation_time = _parse_activation_time(d.pop("activationTime", UNSET))

        customer_opt_in = cls(
            internal_title=internal_title,
            unique_id=unique_id,
            included_types=included_types,
            translations=translations,
            customer_opt_in_id=customer_opt_in_id,
            active=active,
            created_date=created_date,
            changed_date=changed_date,
            created_by=created_by,
            created_by_type=created_by_type,
            changed_by=changed_by,
            changed_by_type=changed_by_type,
            activation_time=activation_time,
        )

        customer_opt_in.additional_properties = d
        return customer_opt_in

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
