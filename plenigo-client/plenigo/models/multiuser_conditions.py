from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.multiuser_conditions_multiuser_payment_variant import MultiuserConditionsMultiuserPaymentVariant
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.full_price_user_segment import FullPriceUserSegment
    from ..models.graduated_price_per_user_segment import GraduatedPricePerUserSegment
    from ..models.price_per_user_segment import PricePerUserSegment


T = TypeVar("T", bound="MultiuserConditions")


@_attrs_define
class MultiuserConditions:
    """
    Attributes:
        multiuser_basic_fee_price_issue_id (int): price issue id of the basic fee
        multiuser_payment_variant (Union[Unset, MultiuserConditionsMultiuserPaymentVariant]): multiuser payment variant
            Example: COMPLETE.
        max_number_of_users (Union[Unset, int]): maximum number of users
        price_per_user_segments (Union[Unset, list['PricePerUserSegment']]): array of price per user segments. (It is
            required if multiuserPaymentVariant is USER_BASED)
        graduated_price_per_user_segments (Union[Unset, list['GraduatedPricePerUserSegment']]): array of graduated price
            per user segments. (It is required if multiuserPaymentVariant is USER_BASED_GRADUATED)
        full_price_user_segment (Union[Unset, list['FullPriceUserSegment']]): array of full price user segments. (It is
            required if multiuserPaymentVariant is FULL_PACKAGE)
    """

    multiuser_basic_fee_price_issue_id: int
    multiuser_payment_variant: Union[Unset, MultiuserConditionsMultiuserPaymentVariant] = UNSET
    max_number_of_users: Union[Unset, int] = UNSET
    price_per_user_segments: Union[Unset, list["PricePerUserSegment"]] = UNSET
    graduated_price_per_user_segments: Union[Unset, list["GraduatedPricePerUserSegment"]] = UNSET
    full_price_user_segment: Union[Unset, list["FullPriceUserSegment"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        multiuser_basic_fee_price_issue_id = self.multiuser_basic_fee_price_issue_id

        multiuser_payment_variant: Union[Unset, str] = UNSET
        if not isinstance(self.multiuser_payment_variant, Unset):
            multiuser_payment_variant = self.multiuser_payment_variant.value

        max_number_of_users = self.max_number_of_users

        price_per_user_segments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.price_per_user_segments, Unset):
            price_per_user_segments = []
            for price_per_user_segments_item_data in self.price_per_user_segments:
                price_per_user_segments_item = price_per_user_segments_item_data.to_dict()
                price_per_user_segments.append(price_per_user_segments_item)

        graduated_price_per_user_segments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.graduated_price_per_user_segments, Unset):
            graduated_price_per_user_segments = []
            for graduated_price_per_user_segments_item_data in self.graduated_price_per_user_segments:
                graduated_price_per_user_segments_item = graduated_price_per_user_segments_item_data.to_dict()
                graduated_price_per_user_segments.append(graduated_price_per_user_segments_item)

        full_price_user_segment: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.full_price_user_segment, Unset):
            full_price_user_segment = []
            for full_price_user_segment_item_data in self.full_price_user_segment:
                full_price_user_segment_item = full_price_user_segment_item_data.to_dict()
                full_price_user_segment.append(full_price_user_segment_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "multiuserBasicFeePriceIssueId": multiuser_basic_fee_price_issue_id,
            }
        )
        if multiuser_payment_variant is not UNSET:
            field_dict["multiuserPaymentVariant"] = multiuser_payment_variant
        if max_number_of_users is not UNSET:
            field_dict["maxNumberOfUsers"] = max_number_of_users
        if price_per_user_segments is not UNSET:
            field_dict["pricePerUserSegments"] = price_per_user_segments
        if graduated_price_per_user_segments is not UNSET:
            field_dict["graduatedPricePerUserSegments"] = graduated_price_per_user_segments
        if full_price_user_segment is not UNSET:
            field_dict["fullPriceUserSegment"] = full_price_user_segment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.full_price_user_segment import FullPriceUserSegment
        from ..models.graduated_price_per_user_segment import GraduatedPricePerUserSegment
        from ..models.price_per_user_segment import PricePerUserSegment

        d = src_dict.copy()
        multiuser_basic_fee_price_issue_id = d.pop("multiuserBasicFeePriceIssueId")

        _multiuser_payment_variant = d.pop("multiuserPaymentVariant", UNSET)
        multiuser_payment_variant: Union[Unset, MultiuserConditionsMultiuserPaymentVariant]
        if isinstance(_multiuser_payment_variant, Unset) or not _multiuser_payment_variant:
            multiuser_payment_variant = UNSET
        else:
            multiuser_payment_variant = MultiuserConditionsMultiuserPaymentVariant(_multiuser_payment_variant)

        max_number_of_users = d.pop("maxNumberOfUsers", UNSET)

        price_per_user_segments = []
        _price_per_user_segments = d.pop("pricePerUserSegments", UNSET)
        for price_per_user_segments_item_data in _price_per_user_segments or []:
            price_per_user_segments_item = PricePerUserSegment.from_dict(price_per_user_segments_item_data)

            price_per_user_segments.append(price_per_user_segments_item)

        graduated_price_per_user_segments = []
        _graduated_price_per_user_segments = d.pop("graduatedPricePerUserSegments", UNSET)
        for graduated_price_per_user_segments_item_data in _graduated_price_per_user_segments or []:
            graduated_price_per_user_segments_item = GraduatedPricePerUserSegment.from_dict(
                graduated_price_per_user_segments_item_data
            )

            graduated_price_per_user_segments.append(graduated_price_per_user_segments_item)

        full_price_user_segment = []
        _full_price_user_segment = d.pop("fullPriceUserSegment", UNSET)
        for full_price_user_segment_item_data in _full_price_user_segment or []:
            full_price_user_segment_item = FullPriceUserSegment.from_dict(full_price_user_segment_item_data)

            full_price_user_segment.append(full_price_user_segment_item)

        multiuser_conditions = cls(
            multiuser_basic_fee_price_issue_id=multiuser_basic_fee_price_issue_id,
            multiuser_payment_variant=multiuser_payment_variant,
            max_number_of_users=max_number_of_users,
            price_per_user_segments=price_per_user_segments,
            graduated_price_per_user_segments=graduated_price_per_user_segments,
            full_price_user_segment=full_price_user_segment,
        )

        multiuser_conditions.additional_properties = d
        return multiuser_conditions

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
