from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer_cancellation_reason_translation import CustomerCancellationReasonTranslation


T = TypeVar("T", bound="CustomerCancellationReasonUpdate")


@attr.s(auto_attribs=True)
class CustomerCancellationReasonUpdate:
    """
    Attributes:
        internal_title (str): internal title of the cancellation reason
        translations (List['CustomerCancellationReasonTranslation']): translations associated with this cancellation
            reason
        active (Union[Unset, bool]): flag indicating if cancellation reason is currently active
        priority (Union[Unset, int]): priority of the cancellation reason
    """

    internal_title: str
    translations: List["CustomerCancellationReasonTranslation"]
    active: Union[Unset, bool] = UNSET
    priority: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        internal_title = self.internal_title
        translations = []
        for translations_item_data in self.translations:
            translations_item = translations_item_data.to_dict()

            translations.append(translations_item)

        active = self.active
        priority = self.priority

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "internalTitle": internal_title,
                "translations": translations,
            }
        )
        if active is not UNSET:
            field_dict["active"] = active
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.customer_cancellation_reason_translation import CustomerCancellationReasonTranslation

        d = src_dict.copy()
        internal_title = d.pop("internalTitle")

        translations = []
        _translations = d.pop("translations")
        for translations_item_data in _translations:
            translations_item = CustomerCancellationReasonTranslation.from_dict(translations_item_data)

            translations.append(translations_item)

        active = d.pop("active", UNSET)

        priority = d.pop("priority", UNSET)

        customer_cancellation_reason_update = cls(
            internal_title=internal_title,
            translations=translations,
            active=active,
            priority=priority,
        )

        customer_cancellation_reason_update.additional_properties = d
        return customer_cancellation_reason_update

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
