from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wbz_customer_mark_base_data import WbzCustomerMarkBaseData


T = TypeVar("T", bound="WbzCustomerMarkBase")


@_attrs_define
class WbzCustomerMarkBase:
    """
    Attributes:
        dealer_group (str): wbz dealer group
        dealer_number (str): wbz dealer number
        agency_price (Union[Unset, float]): the agency price
        base_price (Union[Unset, float]): the base price
        exit_liability (Union[Unset, int]): exitLiability
        start_wkz_a (Union[Unset, float]): start WKZ-A price
        start_wkz_b (Union[Unset, float]): start WKZ-B price
        start_wkz_c (Union[Unset, float]): start WKZ-C price
        scale_wkz_a (Union[Unset, float]): scale WKZ-A price
        scale_wkz_b (Union[Unset, float]): scale WKZ-B price
        scale_wkz_c (Union[Unset, float]): scale WKZ-C price
        data (Union[Unset, WbzCustomerMarkBaseData]):
    """

    dealer_group: str
    dealer_number: str
    agency_price: Union[Unset, float] = UNSET
    base_price: Union[Unset, float] = UNSET
    exit_liability: Union[Unset, int] = UNSET
    start_wkz_a: Union[Unset, float] = UNSET
    start_wkz_b: Union[Unset, float] = UNSET
    start_wkz_c: Union[Unset, float] = UNSET
    scale_wkz_a: Union[Unset, float] = UNSET
    scale_wkz_b: Union[Unset, float] = UNSET
    scale_wkz_c: Union[Unset, float] = UNSET
    data: Union[Unset, "WbzCustomerMarkBaseData"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dealer_group = self.dealer_group

        dealer_number = self.dealer_number

        agency_price = self.agency_price

        base_price = self.base_price

        exit_liability = self.exit_liability

        start_wkz_a = self.start_wkz_a

        start_wkz_b = self.start_wkz_b

        start_wkz_c = self.start_wkz_c

        scale_wkz_a = self.scale_wkz_a

        scale_wkz_b = self.scale_wkz_b

        scale_wkz_c = self.scale_wkz_c

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dealerGroup": dealer_group,
                "dealerNumber": dealer_number,
            }
        )
        if agency_price is not UNSET:
            field_dict["agencyPrice"] = agency_price
        if base_price is not UNSET:
            field_dict["basePrice"] = base_price
        if exit_liability is not UNSET:
            field_dict["exitLiability"] = exit_liability
        if start_wkz_a is not UNSET:
            field_dict["startWkzA"] = start_wkz_a
        if start_wkz_b is not UNSET:
            field_dict["startWkzB"] = start_wkz_b
        if start_wkz_c is not UNSET:
            field_dict["startWkzC"] = start_wkz_c
        if scale_wkz_a is not UNSET:
            field_dict["scaleWkzA"] = scale_wkz_a
        if scale_wkz_b is not UNSET:
            field_dict["scaleWkzB"] = scale_wkz_b
        if scale_wkz_c is not UNSET:
            field_dict["scaleWkzC"] = scale_wkz_c
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wbz_customer_mark_base_data import WbzCustomerMarkBaseData

        d = src_dict.copy()
        dealer_group = d.pop("dealerGroup")

        dealer_number = d.pop("dealerNumber")

        agency_price = d.pop("agencyPrice", UNSET)

        base_price = d.pop("basePrice", UNSET)

        exit_liability = d.pop("exitLiability", UNSET)

        start_wkz_a = d.pop("startWkzA", UNSET)

        start_wkz_b = d.pop("startWkzB", UNSET)

        start_wkz_c = d.pop("startWkzC", UNSET)

        scale_wkz_a = d.pop("scaleWkzA", UNSET)

        scale_wkz_b = d.pop("scaleWkzB", UNSET)

        scale_wkz_c = d.pop("scaleWkzC", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, WbzCustomerMarkBaseData]
        if isinstance(_data, Unset) or not _data:
            data = UNSET
        else:
            data = WbzCustomerMarkBaseData.from_dict(_data)

        wbz_customer_mark_base = cls(
            dealer_group=dealer_group,
            dealer_number=dealer_number,
            agency_price=agency_price,
            base_price=base_price,
            exit_liability=exit_liability,
            start_wkz_a=start_wkz_a,
            start_wkz_b=start_wkz_b,
            start_wkz_c=start_wkz_c,
            scale_wkz_a=scale_wkz_a,
            scale_wkz_b=scale_wkz_b,
            scale_wkz_c=scale_wkz_c,
            data=data,
        )

        wbz_customer_mark_base.additional_properties = d
        return wbz_customer_mark_base

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
