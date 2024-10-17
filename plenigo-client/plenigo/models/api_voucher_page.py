from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_voucher import ApiVoucher


T = TypeVar("T", bound="ApiVoucherPage")


@_attrs_define
class ApiVoucherPage:
    """
    Attributes:
        starting_after (Union[Unset, int]): starting after element id
        size (Union[Unset, int]): size of elements of the page
        total_size (Union[Unset, int]): total of elements
        campaigns (Union[Unset, List['ApiVoucher']]):
    """

    starting_after: Union[Unset, int] = UNSET
    size: Union[Unset, int] = UNSET
    total_size: Union[Unset, int] = UNSET
    campaigns: Union[Unset, List["ApiVoucher"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        starting_after = self.starting_after

        size = self.size

        total_size = self.total_size

        campaigns: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.campaigns, Unset):
            campaigns = []
            for campaigns_item_data in self.campaigns:
                campaigns_item = campaigns_item_data.to_dict()
                campaigns.append(campaigns_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if starting_after is not UNSET:
            field_dict["startingAfter"] = starting_after
        if size is not UNSET:
            field_dict["size"] = size
        if total_size is not UNSET:
            field_dict["totalSize"] = total_size
        if campaigns is not UNSET:
            field_dict["campaigns"] = campaigns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_voucher import ApiVoucher

        d = src_dict.copy()
        starting_after = d.pop("startingAfter", UNSET)

        size = d.pop("size", UNSET)

        total_size = d.pop("totalSize", UNSET)

        campaigns = []
        _campaigns = d.pop("campaigns", UNSET)
        for campaigns_item_data in _campaigns or []:
            campaigns_item = ApiVoucher.from_dict(campaigns_item_data)

            campaigns.append(campaigns_item)

        api_voucher_page = cls(
            starting_after=starting_after,
            size=size,
            total_size=total_size,
            campaigns=campaigns,
        )

        api_voucher_page.additional_properties = d
        return api_voucher_page

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
