from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_base_date import ApiBaseDate


T = TypeVar("T", bound="ConnectedCompanyOffers")


@_attrs_define
class ConnectedCompanyOffers:
    """
    Attributes:
        company_id (str): unique id of the source company
        company_name (str): name of the source company id
        offers (Union[Unset, List['ApiBaseDate']]): offers that are shared by the company
    """

    company_id: str
    company_name: str
    offers: Union[Unset, List["ApiBaseDate"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        company_id = self.company_id

        company_name = self.company_name

        offers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.offers, Unset):
            offers = []
            for offers_item_data in self.offers:
                offers_item = offers_item_data.to_dict()
                offers.append(offers_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companyId": company_id,
                "companyName": company_name,
            }
        )
        if offers is not UNSET:
            field_dict["offers"] = offers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_base_date import ApiBaseDate

        d = src_dict.copy()
        company_id = d.pop("companyId")

        company_name = d.pop("companyName")

        offers = []
        _offers = d.pop("offers", UNSET)
        for offers_item_data in _offers or []:
            offers_item = ApiBaseDate.from_dict(offers_item_data)

            offers.append(offers_item)

        connected_company_offers = cls(
            company_id=company_id,
            company_name=company_name,
            offers=offers,
        )

        connected_company_offers.additional_properties = d
        return connected_company_offers

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
