from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GooglePlayProductPurchase")


@_attrs_define
class GooglePlayProductPurchase:
    """
    Attributes:
        acknowledgement_state (Union[Unset, str]): acknowledgement state of the inapp product
        consumption_state (Union[Unset, str]): consumption state of the inapp product
        developer_payload (Union[Unset, str]): developer-specified string that contains supplemental information about
            an order
        kind (Union[Unset, str]): kind represents a subscriptionPurchase object in the androidpublisher service
        order_id (Union[Unset, str]): order id associated with the purchase of the inapp product
        purchase_state (Union[Unset, str]): purchase state of the order
        purchase_time_millis (Union[Unset, str]): time the product was purchased, in milliseconds since the epoch (Jan
            1, 1970)
        purchase_type (Union[Unset, str]): type of purchase of the inapp product
    """

    acknowledgement_state: Union[Unset, str] = UNSET
    consumption_state: Union[Unset, str] = UNSET
    developer_payload: Union[Unset, str] = UNSET
    kind: Union[Unset, str] = UNSET
    order_id: Union[Unset, str] = UNSET
    purchase_state: Union[Unset, str] = UNSET
    purchase_time_millis: Union[Unset, str] = UNSET
    purchase_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        acknowledgement_state = self.acknowledgement_state

        consumption_state = self.consumption_state

        developer_payload = self.developer_payload

        kind = self.kind

        order_id = self.order_id

        purchase_state = self.purchase_state

        purchase_time_millis = self.purchase_time_millis

        purchase_type = self.purchase_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if acknowledgement_state is not UNSET:
            field_dict["acknowledgementState"] = acknowledgement_state
        if consumption_state is not UNSET:
            field_dict["consumptionState"] = consumption_state
        if developer_payload is not UNSET:
            field_dict["developerPayload"] = developer_payload
        if kind is not UNSET:
            field_dict["kind"] = kind
        if order_id is not UNSET:
            field_dict["orderId"] = order_id
        if purchase_state is not UNSET:
            field_dict["purchaseState"] = purchase_state
        if purchase_time_millis is not UNSET:
            field_dict["purchaseTimeMillis"] = purchase_time_millis
        if purchase_type is not UNSET:
            field_dict["purchaseType"] = purchase_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        acknowledgement_state = d.pop("acknowledgementState", UNSET)

        consumption_state = d.pop("consumptionState", UNSET)

        developer_payload = d.pop("developerPayload", UNSET)

        kind = d.pop("kind", UNSET)

        order_id = d.pop("orderId", UNSET)

        purchase_state = d.pop("purchaseState", UNSET)

        purchase_time_millis = d.pop("purchaseTimeMillis", UNSET)

        purchase_type = d.pop("purchaseType", UNSET)

        google_play_product_purchase = cls(
            acknowledgement_state=acknowledgement_state,
            consumption_state=consumption_state,
            developer_payload=developer_payload,
            kind=kind,
            order_id=order_id,
            purchase_state=purchase_state,
            purchase_time_millis=purchase_time_millis,
            purchase_type=purchase_type,
        )

        google_play_product_purchase.additional_properties = d
        return google_play_product_purchase

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
