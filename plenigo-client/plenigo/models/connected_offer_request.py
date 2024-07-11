from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectedOfferRequest")


@_attrs_define
class ConnectedOfferRequest:
    """
    Attributes:
        plenigo_connected_offer_id (str): id of the connected offer to sell
        connected_company_id (Union[Unset, str]): id of the connected company id
    """

    plenigo_connected_offer_id: str
    connected_company_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        plenigo_connected_offer_id = self.plenigo_connected_offer_id

        connected_company_id = self.connected_company_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "plenigoConnectedOfferId": plenigo_connected_offer_id,
            }
        )
        if connected_company_id is not UNSET:
            field_dict["connectedCompanyId"] = connected_company_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        plenigo_connected_offer_id = d.pop("plenigoConnectedOfferId")

        connected_company_id = d.pop("connectedCompanyId", UNSET)

        connected_offer_request = cls(
            plenigo_connected_offer_id=plenigo_connected_offer_id,
            connected_company_id=connected_company_id,
        )

        connected_offer_request.additional_properties = d
        return connected_offer_request

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
