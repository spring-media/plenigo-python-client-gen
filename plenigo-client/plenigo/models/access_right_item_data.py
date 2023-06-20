import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.access_right_item_data_item_type import AccessRightItemDataItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access_right_item_data_access_right_data import AccessRightItemDataAccessRightData
    from ..models.access_right_item_data_data import AccessRightItemDataData


T = TypeVar("T", bound="AccessRightItemData")


@attr.s(auto_attribs=True)
class AccessRightItemData:
    """
    Attributes:
        life_time_start (Union[Unset, None, datetime.datetime]): date the access right will start with date-time
            notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339,
            section 5.6</a>, for example, 2017-07-21T17:32:28Z
        life_time_end (Union[Unset, None, datetime.datetime]): date the access right will end with date-time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 2017-07-21T17:32:28Z
        access_time_start (Union[Unset, None, datetime.datetime]): time the access right will start with time notation
            as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section
            5.6</a>, for example, 17:32:28
        access_time_end (Union[Unset, None, datetime.datetime]): time the access right will end with time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 17:32:28
        pause_time_start (Union[Unset, None, datetime.datetime]): start date the access right will paused with date-time
            notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339,
            section 5.6</a>, for example, 2017-07-21T17:32:28Z
        pause_time_end (Union[Unset, None, datetime.datetime]): end date the access right pause end with date-time
            notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339,
            section 5.6</a>, for example, 2017-07-21T17:32:28Z
        max_cache_date (Union[Unset, None, datetime.datetime]): max cache date with date-time notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-21T17:32:28Z
        data (Union[Unset, None, AccessRightItemDataData]):
        blocked (Union[Unset, bool]): flag indicating if access is blocked
        product_id (Union[Unset, str]): id of the product bought
        plenigo_offer_id (Union[Unset, str]): if the product is based on a plenigo offer the plenigo offer id is
            provided here
        plenigo_product_id (Union[Unset, str]): if the product is based on a plenigo offer the plenigo product id is
            provided here - can be identically to the productId
        plenigo_step_id (Union[Unset, str]): if the product is based on a plenigo offer the plenigo step id is provided
            here
        access_right_unique_id (Union[Unset, str]): unique id of the access right this access right grants access to
        item_type (Union[Unset, AccessRightItemDataItemType]): type of this access right item
        item_id (Union[Unset, str]): the id this access right belongs to
        access_right_data (Union[Unset, AccessRightItemDataAccessRightData]):
    """

    life_time_start: Union[Unset, None, datetime.datetime] = UNSET
    life_time_end: Union[Unset, None, datetime.datetime] = UNSET
    access_time_start: Union[Unset, None, datetime.datetime] = UNSET
    access_time_end: Union[Unset, None, datetime.datetime] = UNSET
    pause_time_start: Union[Unset, None, datetime.datetime] = UNSET
    pause_time_end: Union[Unset, None, datetime.datetime] = UNSET
    max_cache_date: Union[Unset, None, datetime.datetime] = UNSET
    data: Union[Unset, None, "AccessRightItemDataData"] = UNSET
    blocked: Union[Unset, bool] = UNSET
    product_id: Union[Unset, str] = UNSET
    plenigo_offer_id: Union[Unset, str] = UNSET
    plenigo_product_id: Union[Unset, str] = UNSET
    plenigo_step_id: Union[Unset, str] = UNSET
    access_right_unique_id: Union[Unset, str] = UNSET
    item_type: Union[Unset, AccessRightItemDataItemType] = UNSET
    item_id: Union[Unset, str] = UNSET
    access_right_data: Union[Unset, "AccessRightItemDataAccessRightData"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        life_time_start: Union[Unset, None, str] = UNSET
        if not isinstance(self.life_time_start, Unset):
            life_time_start = self.life_time_start.isoformat() if self.life_time_start else None

        life_time_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.life_time_end, Unset):
            life_time_end = self.life_time_end.isoformat() if self.life_time_end else None

        access_time_start: Union[Unset, None, str] = UNSET
        if not isinstance(self.access_time_start, Unset):
            access_time_start = self.access_time_start.isoformat() if self.access_time_start else None

        access_time_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.access_time_end, Unset):
            access_time_end = self.access_time_end.isoformat() if self.access_time_end else None

        pause_time_start: Union[Unset, None, str] = UNSET
        if not isinstance(self.pause_time_start, Unset):
            pause_time_start = self.pause_time_start.isoformat() if self.pause_time_start else None

        pause_time_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.pause_time_end, Unset):
            pause_time_end = self.pause_time_end.isoformat() if self.pause_time_end else None

        max_cache_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.max_cache_date, Unset):
            max_cache_date = self.max_cache_date.isoformat() if self.max_cache_date else None

        data: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict() if self.data else None

        blocked = self.blocked
        product_id = self.product_id
        plenigo_offer_id = self.plenigo_offer_id
        plenigo_product_id = self.plenigo_product_id
        plenigo_step_id = self.plenigo_step_id
        access_right_unique_id = self.access_right_unique_id
        item_type: Union[Unset, str] = UNSET
        if not isinstance(self.item_type, Unset):
            item_type = self.item_type.value

        item_id = self.item_id
        access_right_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.access_right_data, Unset):
            access_right_data = self.access_right_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if life_time_start is not UNSET:
            field_dict["lifeTimeStart"] = life_time_start
        if life_time_end is not UNSET:
            field_dict["lifeTimeEnd"] = life_time_end
        if access_time_start is not UNSET:
            field_dict["accessTimeStart"] = access_time_start
        if access_time_end is not UNSET:
            field_dict["accessTimeEnd"] = access_time_end
        if pause_time_start is not UNSET:
            field_dict["pauseTimeStart"] = pause_time_start
        if pause_time_end is not UNSET:
            field_dict["pauseTimeEnd"] = pause_time_end
        if max_cache_date is not UNSET:
            field_dict["maxCacheDate"] = max_cache_date
        if data is not UNSET:
            field_dict["data"] = data
        if blocked is not UNSET:
            field_dict["blocked"] = blocked
        if product_id is not UNSET:
            field_dict["productId"] = product_id
        if plenigo_offer_id is not UNSET:
            field_dict["plenigoOfferId"] = plenigo_offer_id
        if plenigo_product_id is not UNSET:
            field_dict["plenigoProductId"] = plenigo_product_id
        if plenigo_step_id is not UNSET:
            field_dict["plenigoStepId"] = plenigo_step_id
        if access_right_unique_id is not UNSET:
            field_dict["accessRightUniqueId"] = access_right_unique_id
        if item_type is not UNSET:
            field_dict["itemType"] = item_type
        if item_id is not UNSET:
            field_dict["itemId"] = item_id
        if access_right_data is not UNSET:
            field_dict["accessRightData"] = access_right_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.access_right_item_data_access_right_data import AccessRightItemDataAccessRightData
        from ..models.access_right_item_data_data import AccessRightItemDataData

        d = src_dict.copy()
        _life_time_start = d.pop("lifeTimeStart", UNSET)
        life_time_start: Union[Unset, None, datetime.datetime]
        if _life_time_start is None:
            life_time_start = None
        elif isinstance(_life_time_start, Unset):
            life_time_start = UNSET
        else:
            life_time_start = isoparse(_life_time_start)

        _life_time_end = d.pop("lifeTimeEnd", UNSET)
        life_time_end: Union[Unset, None, datetime.datetime]
        if _life_time_end is None:
            life_time_end = None
        elif isinstance(_life_time_end, Unset):
            life_time_end = UNSET
        else:
            life_time_end = isoparse(_life_time_end)

        _access_time_start = d.pop("accessTimeStart", UNSET)
        access_time_start: Union[Unset, None, datetime.datetime]
        if _access_time_start is None:
            access_time_start = None
        elif isinstance(_access_time_start, Unset):
            access_time_start = UNSET
        else:
            access_time_start = isoparse(_access_time_start)

        _access_time_end = d.pop("accessTimeEnd", UNSET)
        access_time_end: Union[Unset, None, datetime.datetime]
        if _access_time_end is None:
            access_time_end = None
        elif isinstance(_access_time_end, Unset):
            access_time_end = UNSET
        else:
            access_time_end = isoparse(_access_time_end)

        _pause_time_start = d.pop("pauseTimeStart", UNSET)
        pause_time_start: Union[Unset, None, datetime.datetime]
        if _pause_time_start is None:
            pause_time_start = None
        elif isinstance(_pause_time_start, Unset):
            pause_time_start = UNSET
        else:
            pause_time_start = isoparse(_pause_time_start)

        _pause_time_end = d.pop("pauseTimeEnd", UNSET)
        pause_time_end: Union[Unset, None, datetime.datetime]
        if _pause_time_end is None:
            pause_time_end = None
        elif isinstance(_pause_time_end, Unset):
            pause_time_end = UNSET
        else:
            pause_time_end = isoparse(_pause_time_end)

        _max_cache_date = d.pop("maxCacheDate", UNSET)
        max_cache_date: Union[Unset, None, datetime.datetime]
        if _max_cache_date is None:
            max_cache_date = None
        elif isinstance(_max_cache_date, Unset):
            max_cache_date = UNSET
        else:
            max_cache_date = isoparse(_max_cache_date)

        _data = d.pop("data", UNSET)
        data: Union[Unset, None, AccessRightItemDataData]
        if _data is None:
            data = None
        elif isinstance(_data, Unset):
            data = UNSET
        else:
            data = AccessRightItemDataData.from_dict(_data)

        blocked = d.pop("blocked", UNSET)

        product_id = d.pop("productId", UNSET)

        plenigo_offer_id = d.pop("plenigoOfferId", UNSET)

        plenigo_product_id = d.pop("plenigoProductId", UNSET)

        plenigo_step_id = d.pop("plenigoStepId", UNSET)

        access_right_unique_id = d.pop("accessRightUniqueId", UNSET)

        _item_type = d.pop("itemType", UNSET)
        item_type: Union[Unset, AccessRightItemDataItemType]
        if isinstance(_item_type, Unset):
            item_type = UNSET
        else:
            item_type = AccessRightItemDataItemType(_item_type)

        item_id = d.pop("itemId", UNSET)

        _access_right_data = d.pop("accessRightData", UNSET)
        access_right_data: Union[Unset, AccessRightItemDataAccessRightData]
        if isinstance(_access_right_data, Unset):
            access_right_data = UNSET
        else:
            access_right_data = AccessRightItemDataAccessRightData.from_dict(_access_right_data)

        access_right_item_data = cls(
            life_time_start=life_time_start,
            life_time_end=life_time_end,
            access_time_start=access_time_start,
            access_time_end=access_time_end,
            pause_time_start=pause_time_start,
            pause_time_end=pause_time_end,
            max_cache_date=max_cache_date,
            data=data,
            blocked=blocked,
            product_id=product_id,
            plenigo_offer_id=plenigo_offer_id,
            plenigo_product_id=plenigo_product_id,
            plenigo_step_id=plenigo_step_id,
            access_right_unique_id=access_right_unique_id,
            item_type=item_type,
            item_id=item_id,
            access_right_data=access_right_data,
        )

        access_right_item_data.additional_properties = d
        return access_right_item_data

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
