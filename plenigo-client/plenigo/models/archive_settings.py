from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.archive_settings_archive_type import ArchiveSettingsArchiveType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ArchiveSettings")


@_attrs_define
class ArchiveSettings:
    """
    Attributes:
        archive_type (ArchiveSettingsArchiveType): archive type
        customer_text_tm_id (Union[Unset, int]): id of the customer text module to use
        successor_plenigo_offer_id (Union[Unset, str]): plenigo offer id of the successor
    """

    archive_type: ArchiveSettingsArchiveType
    customer_text_tm_id: Union[Unset, int] = UNSET
    successor_plenigo_offer_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        archive_type = self.archive_type.value

        customer_text_tm_id = self.customer_text_tm_id

        successor_plenigo_offer_id = self.successor_plenigo_offer_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "archiveType": archive_type,
            }
        )
        if customer_text_tm_id is not UNSET:
            field_dict["customerTextTmId"] = customer_text_tm_id
        if successor_plenigo_offer_id is not UNSET:
            field_dict["successorPlenigoOfferId"] = successor_plenigo_offer_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        archive_type = ArchiveSettingsArchiveType(d.pop("archiveType"))

        customer_text_tm_id = d.pop("customerTextTmId", UNSET)

        successor_plenigo_offer_id = d.pop("successorPlenigoOfferId", UNSET)

        archive_settings = cls(
            archive_type=archive_type,
            customer_text_tm_id=customer_text_tm_id,
            successor_plenigo_offer_id=successor_plenigo_offer_id,
        )

        archive_settings.additional_properties = d
        return archive_settings

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
