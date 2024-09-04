import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_base_changed_by_type import ApiBaseChangedByType
from ..models.api_base_created_by_type import ApiBaseCreatedByType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wbz_customer_mark_base_data import WbzCustomerMarkBaseData


T = TypeVar("T", bound="WbzCustomerMark")


@_attrs_define
class WbzCustomerMark:
    """
    Attributes:
        dealer_group (str): wbz dealer group
        dealer_number (str): wbz dealer number
        created_date (Union[None, Unset, datetime.datetime]): Time the object was created in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        changed_date (Union[None, Unset, datetime.datetime]): Time the object was changed in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        created_by (Union[Unset, str]): ID of who created the object
        created_by_type (Union[Unset, ApiBaseCreatedByType]): Type of creator
        changed_by (Union[Unset, str]): ID of who changed the object
        changed_by_type (Union[Unset, ApiBaseChangedByType]): Type of changer
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
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_by_type: Union[Unset, ApiBaseCreatedByType] = UNSET
    changed_by: Union[Unset, str] = UNSET
    changed_by_type: Union[Unset, ApiBaseChangedByType] = UNSET
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

        created_date: Union[None, Unset, str]
        if isinstance(self.created_date, Unset) or self.created_date is None:
            created_date = UNSET
        elif isinstance(self.created_date, datetime.datetime):
            created_date = self.created_date.isoformat()
        else:
            created_date = self.created_date

        changed_date: Union[None, Unset, str]
        if isinstance(self.changed_date, Unset) or self.changed_date is None:
            changed_date = UNSET
        elif isinstance(self.changed_date, datetime.datetime):
            changed_date = self.changed_date.isoformat()
        else:
            changed_date = self.changed_date

        created_by = self.created_by

        created_by_type: Union[Unset, str] = UNSET
        if not isinstance(self.created_by_type, Unset):
            created_by_type = self.created_by_type.value

        changed_by = self.changed_by

        changed_by_type: Union[Unset, str] = UNSET
        if not isinstance(self.changed_by_type, Unset):
            changed_by_type = self.changed_by_type.value

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
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_by_type is not UNSET:
            field_dict["createdByType"] = created_by_type
        if changed_by is not UNSET:
            field_dict["changedBy"] = changed_by
        if changed_by_type is not UNSET:
            field_dict["changedByType"] = changed_by_type
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

        def _parse_created_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data

            if data is None:
                return data

            if isinstance(data, Unset):
                return data

            # Try to parse the data as datetime.datetime
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_date_type_0 = isoparse(data)

                return created_date_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        created_date = _parse_created_date(d.pop("createdDate", UNSET))

        def _parse_changed_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data

            if data is None:
                return data

            if isinstance(data, Unset):
                return data

            # Try to parse the data as datetime.datetime
            try:
                if not isinstance(data, str):
                    raise TypeError()
                changed_date_type_0 = isoparse(data)

                return changed_date_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        changed_date = _parse_changed_date(d.pop("changedDate", UNSET))

        created_by = d.pop("createdBy", UNSET)

        _created_by_type = d.pop("createdByType", UNSET)
        created_by_type: Union[Unset, ApiBaseCreatedByType]
        if isinstance(_created_by_type, Unset) or not _created_by_type:
            created_by_type = UNSET
        else:
            created_by_type = ApiBaseCreatedByType(_created_by_type)

        changed_by = d.pop("changedBy", UNSET)

        _changed_by_type = d.pop("changedByType", UNSET)
        changed_by_type: Union[Unset, ApiBaseChangedByType]
        if isinstance(_changed_by_type, Unset) or not _changed_by_type:
            changed_by_type = UNSET
        else:
            changed_by_type = ApiBaseChangedByType(_changed_by_type)

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

        wbz_customer_mark = cls(
            dealer_group=dealer_group,
            dealer_number=dealer_number,
            created_date=created_date,
            changed_date=changed_date,
            created_by=created_by,
            created_by_type=created_by_type,
            changed_by=changed_by,
            changed_by_type=changed_by_type,
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

        wbz_customer_mark.additional_properties = d
        return wbz_customer_mark

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
