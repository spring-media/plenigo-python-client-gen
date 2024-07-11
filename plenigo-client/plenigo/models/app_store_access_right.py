from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_store_access_right_additional_data import AppStoreAccessRightAdditionalData


T = TypeVar("T", bound="AppStoreAccessRight")


@_attrs_define
class AppStoreAccessRight:
    """
    Attributes:
        unique_id (Union[Unset, str]): access right unique id that will be associated with this app store purchase after
            association
        additional_data (Union[Unset, AppStoreAccessRightAdditionalData]):
    """

    unique_id: Union[Unset, str] = UNSET
    additional_data: Union[Unset, "AppStoreAccessRightAdditionalData"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unique_id = self.unique_id

        additional_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.additional_data, Unset):
            additional_data = self.additional_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unique_id is not UNSET:
            field_dict["uniqueId"] = unique_id
        if additional_data is not UNSET:
            field_dict["additionalData"] = additional_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.app_store_access_right_additional_data import AppStoreAccessRightAdditionalData

        d = src_dict.copy()
        unique_id = d.pop("uniqueId", UNSET)

        _additional_data = d.pop("additionalData", UNSET)
        additional_data: Union[Unset, AppStoreAccessRightAdditionalData]
        if isinstance(_additional_data, Unset):
            additional_data = UNSET
        else:
            additional_data = AppStoreAccessRightAdditionalData.from_dict(_additional_data)

        app_store_access_right = cls(
            unique_id=unique_id,
            additional_data=additional_data,
        )

        app_store_access_right.additional_properties = d
        return app_store_access_right

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
