import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_base_changed_by_type import ApiBaseChangedByType
from ..models.api_base_created_by_type import ApiBaseCreatedByType
from ..models.purchased_addon_addon_type import PurchasedAddonAddonType
from ..models.purchased_addon_delivery_condition import PurchasedAddonDeliveryCondition
from ..models.purchased_addon_status import PurchasedAddonStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.addon_tracking_data import AddonTrackingData


T = TypeVar("T", bound="PurchasedAddon")


@_attrs_define
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
        created_date (Union[None, Unset, datetime.datetime]): Time the object was created in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        changed_date (Union[None, Unset, datetime.datetime]): Time the object was changed in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        created_by (Union[Unset, str]): ID of who created the object
        created_by_type (Union[Unset, ApiBaseCreatedByType]): Type of creator
        changed_by (Union[Unset, str]): ID of who changed the object
        changed_by_type (Union[Unset, ApiBaseChangedByType]): Type of changer
        delivery_date (Union[None, Unset, datetime.datetime]): date the delivery was done with date-time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 2017-07-21T17:32:28Z
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
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_by_type: Union[Unset, ApiBaseCreatedByType] = UNSET
    changed_by: Union[Unset, str] = UNSET
    changed_by_type: Union[Unset, ApiBaseChangedByType] = UNSET
    delivery_date: Union[None, Unset, datetime.datetime] = UNSET
    tracking_data: Union[Unset, "AddonTrackingData"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

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

        created_date: Union[None, Unset, str]
        if isinstance(self.created_date, Unset):
            created_date = UNSET
        elif isinstance(self.created_date, datetime.datetime):
            created_date = self.created_date.isoformat()
        else:
            created_date = self.created_date

        changed_date: Union[None, Unset, str]
        if isinstance(self.changed_date, Unset):
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

        delivery_date: Union[None, Unset, str]
        if isinstance(self.delivery_date, Unset):
            delivery_date = UNSET
        elif isinstance(self.delivery_date, datetime.datetime):
            delivery_date = self.delivery_date.isoformat()
        else:
            delivery_date = self.delivery_date

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

        def _parse_created_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
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
            if isinstance(data, Unset):
                return data
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
        if isinstance(_created_by_type, Unset):
            created_by_type = UNSET
        else:
            created_by_type = ApiBaseCreatedByType(_created_by_type)

        changed_by = d.pop("changedBy", UNSET)

        _changed_by_type = d.pop("changedByType", UNSET)
        changed_by_type: Union[Unset, ApiBaseChangedByType]
        if isinstance(_changed_by_type, Unset):
            changed_by_type = UNSET
        else:
            changed_by_type = ApiBaseChangedByType(_changed_by_type)

        def _parse_delivery_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delivery_date_type_0 = isoparse(data)

                return delivery_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        delivery_date = _parse_delivery_date(d.pop("deliveryDate", UNSET))

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
            created_date=created_date,
            changed_date=changed_date,
            created_by=created_by,
            created_by_type=created_by_type,
            changed_by=changed_by,
            changed_by_type=changed_by_type,
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
