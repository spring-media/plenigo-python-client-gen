from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.additional_order_data_data import AdditionalOrderDataData
    from ..models.utm import Utm


T = TypeVar("T", bound="AdditionalOrderData")


@attr.s(auto_attribs=True)
class AdditionalOrderData:
    """
    Attributes:
        affiliate_id (Union[Unset, str]): affiliate id associated
        partner_id (Union[Unset, str]): id of the partner
        source_id (Union[Unset, str]): id (e.g. URI) to identify source
        utm (Union[Unset, Utm]):
        data (Union[Unset, AdditionalOrderDataData]):
    """

    affiliate_id: Union[Unset, str] = UNSET
    partner_id: Union[Unset, str] = UNSET
    source_id: Union[Unset, str] = UNSET
    utm: Union[Unset, "Utm"] = UNSET
    data: Union[Unset, "AdditionalOrderDataData"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        affiliate_id = self.affiliate_id
        partner_id = self.partner_id
        source_id = self.source_id
        utm: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.utm, Unset):
            utm = self.utm.to_dict()

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affiliate_id is not UNSET:
            field_dict["affiliateId"] = affiliate_id
        if partner_id is not UNSET:
            field_dict["partnerId"] = partner_id
        if source_id is not UNSET:
            field_dict["sourceId"] = source_id
        if utm is not UNSET:
            field_dict["utm"] = utm
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.additional_order_data_data import AdditionalOrderDataData
        from ..models.utm import Utm

        d = src_dict.copy()
        affiliate_id = d.pop("affiliateId", UNSET)

        partner_id = d.pop("partnerId", UNSET)

        source_id = d.pop("sourceId", UNSET)

        _utm = d.pop("utm", UNSET)
        utm: Union[Unset, Utm]
        if isinstance(_utm, Unset):
            utm = UNSET
        else:
            utm = Utm.from_dict(_utm)

        _data = d.pop("data", UNSET)
        data: Union[Unset, AdditionalOrderDataData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = AdditionalOrderDataData.from_dict(_data)

        additional_order_data = cls(
            affiliate_id=affiliate_id,
            partner_id=partner_id,
            source_id=source_id,
            utm=utm,
            data=data,
        )

        additional_order_data.additional_properties = d
        return additional_order_data

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
