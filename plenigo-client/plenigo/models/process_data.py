from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.process_designs import ProcessDesigns
    from ..models.process_settings import ProcessSettings


T = TypeVar("T", bound="ProcessData")


@attr.s(auto_attribs=True)
class ProcessData:
    """
    Attributes:
        designs (Union[Unset, ProcessDesigns]):
        settings (Union[Unset, ProcessSettings]):
    """

    designs: Union[Unset, "ProcessDesigns"] = UNSET
    settings: Union[Unset, "ProcessSettings"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

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
        from ..models.process_designs import ProcessDesigns
        from ..models.process_settings import ProcessSettings

        d = src_dict.copy()
        _designs = d.pop("designs", UNSET)
        designs: Union[Unset, ProcessDesigns]
        if isinstance(_designs, Unset):
            designs = UNSET
        else:
            designs = ProcessDesigns.from_dict(_designs)

        _settings = d.pop("settings", UNSET)
        settings: Union[Unset, ProcessSettings]
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = ProcessSettings.from_dict(_settings)

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
