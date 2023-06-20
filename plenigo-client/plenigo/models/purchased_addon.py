import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.purchased_addon_addon_type import PurchasedAddonAddonType
from ..models.purchased_addon_delivery_condition import PurchasedAddonDeliveryCondition
from ..models.purchased_addon_status import PurchasedAddonStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.addon_tracking_data import AddonTrackingData


T = TypeVar("T", bound="PurchasedAddon")


@attr.s(auto_attribs=True)
class PurchasedAddon:
    """
    Attributes:
        purchased_addon_id (int): unique id of the purchased addon
        delivery_customer_id (str): id of the delivery customer
        addon_type (PurchasedAddonAddonType): type of the addon
        plenigo_addon_id (str): plenigo addon product id
        access_right_unique_id (str): unique id of the access right this order item grants access to
        order_id (int): unique id of the order in the context of a company
        order_item_position (int): position of the order item inside the order - creates a unique order item id in
            combination with the orderId
        status (PurchasedAddonStatus): status of the purchased addon
        delivery_condition (PurchasedAddonDeliveryCondition): delivery condition of the purchased addon
        delivery_date (Union[Unset, datetime.datetime]): date the delivery was done with date-time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 2017-07-21T17:32:28Z
        tracking_data (Union[Unset, AddonTrackingData]):
    """

    purchased_addon_id: int
    delivery_customer_id: str
    addon_type: PurchasedAddonAddonType
    plenigo_addon_id: str
    access_right_unique_id: str
    order_id: int
    order_item_position: int
    status: PurchasedAddonStatus
    delivery_condition: PurchasedAddonDeliveryCondition
    delivery_date: Union[Unset, datetime.datetime] = UNSET
    tracking_data: Union[Unset, "AddonTrackingData"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        purchased_addon_id = self.purchased_addon_id
        delivery_customer_id = self.delivery_customer_id
        addon_type = self.addon_type.value

        plenigo_addon_id = self.plenigo_addon_id
        access_right_unique_id = self.access_right_unique_id
        order_id = self.order_id
        order_item_position = self.order_item_position
        status = self.status.value

        delivery_condition = self.delivery_condition.value

        delivery_date: Union[Unset, str] = UNSET
        if not isinstance(self.delivery_date, Unset):
            delivery_date = self.delivery_date.isoformat()

        tracking_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tracking_data, Unset):
            tracking_data = self.tracking_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "purchasedAddonId": purchased_addon_id,
                "deliveryCustomerId": delivery_customer_id,
                "addonType": addon_type,
                "plenigoAddonId": plenigo_addon_id,
                "accessRightUniqueId": access_right_unique_id,
                "orderId": order_id,
                "orderItemPosition": order_item_position,
                "status": status,
                "deliveryCondition": delivery_condition,
            }
        )
        if delivery_date is not UNSET:
            field_dict["deliveryDate"] = delivery_date
        if tracking_data is not UNSET:
            field_dict["trackingData"] = tracking_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.addon_tracking_data import AddonTrackingData

        d = src_dict.copy()
        purchased_addon_id = d.pop("purchasedAddonId")

        delivery_customer_id = d.pop("deliveryCustomerId")

        addon_type = PurchasedAddonAddonType(d.pop("addonType"))

        plenigo_addon_id = d.pop("plenigoAddonId")

        access_right_unique_id = d.pop("accessRightUniqueId")

        order_id = d.pop("orderId")

        order_item_position = d.pop("orderItemPosition")

        status = PurchasedAddonStatus(d.pop("status"))

        delivery_condition = PurchasedAddonDeliveryCondition(d.pop("deliveryCondition"))

        _delivery_date = d.pop("deliveryDate", UNSET)
        delivery_date: Union[Unset, datetime.datetime]
        if isinstance(_delivery_date, Unset):
            delivery_date = UNSET
        else:
            delivery_date = isoparse(_delivery_date)

        _tracking_data = d.pop("trackingData", UNSET)
        tracking_data: Union[Unset, AddonTrackingData]
        if isinstance(_tracking_data, Unset):
            tracking_data = UNSET
        else:
            tracking_data = AddonTrackingData.from_dict(_tracking_data)

        purchased_addon = cls(
            purchased_addon_id=purchased_addon_id,
            delivery_customer_id=delivery_customer_id,
            addon_type=addon_type,
            plenigo_addon_id=plenigo_addon_id,
            access_right_unique_id=access_right_unique_id,
            order_id=order_id,
            order_item_position=order_item_position,
            status=status,
            delivery_condition=delivery_condition,
            delivery_date=delivery_date,
            tracking_data=tracking_data,
        )

        purchased_addon.additional_properties = d
        return purchased_addon

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
