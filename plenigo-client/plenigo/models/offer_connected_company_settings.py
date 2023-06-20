from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.offer_connection_info import OfferConnectionInfo


T = TypeVar("T", bound="OfferConnectedCompanySettings")


@attr.s(auto_attribs=True)
class OfferConnectedCompanySettings:
    """
    Attributes:
        connection_info (Union[Unset, List['OfferConnectionInfo']]): connected company settings
    """

    connection_info: Union[Unset, List["OfferConnectionInfo"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_info: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.connection_info, Unset):
            connection_info = []
            for connection_info_item_data in self.connection_info:
                connection_info_item = connection_info_item_data.to_dict()

                connection_info.append(connection_info_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connection_info is not UNSET:
            field_dict["connectionInfo"] = connection_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.offer_connection_info import OfferConnectionInfo

        d = src_dict.copy()
        connection_info = []
        _connection_info = d.pop("connectionInfo", UNSET)
        for connection_info_item_data in _connection_info or []:
            connection_info_item = OfferConnectionInfo.from_dict(connection_info_item_data)

            connection_info.append(connection_info_item)

        offer_connected_company_settings = cls(
            connection_info=connection_info,
        )

        offer_connected_company_settings.additional_properties = d
        return offer_connected_company_settings

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
