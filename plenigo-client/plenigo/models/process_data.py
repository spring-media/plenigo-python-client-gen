from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_base_date import ApiBaseDate
    from ..models.process_designs import ProcessDesigns


T = TypeVar("T", bound="ProcessData")


@_attrs_define
class ProcessData:
    """
    Attributes:
        designs (Union[Unset, ProcessDesigns]):
        settings (Union[Unset, ApiBaseDate]):
    """

    designs: Union[Unset, "ProcessDesigns"] = UNSET
    settings: Union[Unset, "ApiBaseDate"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        designs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.designs, Unset):
            designs = self.designs.to_dict()

        settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if designs is not UNSET:
            field_dict["designs"] = designs
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_base_date import ApiBaseDate
        from ..models.process_designs import ProcessDesigns

        d = src_dict.copy()
        _designs = d.pop("designs", UNSET)
        designs: Union[Unset, ProcessDesigns]
        if isinstance(_designs, Unset) or not _designs:
            designs = UNSET
        else:
            designs = ProcessDesigns.from_dict(_designs)

        _settings = d.pop("settings", UNSET)
        settings: Union[Unset, ApiBaseDate]
        if isinstance(_settings, Unset) or not _settings:
            settings = UNSET
        else:
            settings = ApiBaseDate.from_dict(_settings)

        process_data = cls(
            designs=designs,
            settings=settings,
        )

        process_data.additional_properties = d
        return process_data

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
