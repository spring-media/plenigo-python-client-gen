import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.access_right_item_data_item_type import AccessRightItemDataItemType
from ..models.user_type import UserType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access_right_item_data_access_right_data import AccessRightItemDataAccessRightData
    from ..models.access_right_item_data_data import AccessRightItemDataData


T = TypeVar("T", bound="AccessRightItemData")


@_attrs_define
class AccessRightItemData:
    """
    Attributes:
        access_right_unique_id (str): unique id of the access right this access right grants access to
        created_date (Union[None, Unset, datetime.datetime]): time the object was created with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        changed_date (Union[None, Unset, datetime.datetime]): time the object was changed with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        created_by (Union[Unset, str]): id who created the object
        created_by_type (Union[Unset, UserType]): type of user who performs the action
        changed_by (Union[Unset, str]): id who changed the object
        changed_by_type (Union[Unset, UserType]): type of user who performs the action
        life_time_start (Union[None, Unset, datetime.datetime]): date the access right will start with date-time
            notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339,
            section 5.6</a>, for example, 2017-07-21T17:32:28Z
        life_time_end (Union[None, Unset, datetime.datetime]): date the access right will end with date-time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 2017-07-21T17:32:28Z
        access_time_start (Union[None, Unset, datetime.datetime]): time the access right will start with time notation
            as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section
            5.6</a>, for example, 17:32:28
        access_time_end (Union[None, Unset, datetime.datetime]): time the access right will end with time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 17:32:28
        max_cache_date (Union[None, Unset, datetime.datetime]): max cache date with date-time notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-21T17:32:28Z
        data (Union[Unset, AccessRightItemDataData]): Key must be a string with a maximum length of 20 characters.
        blocked (Union[Unset, bool]): flag indicating if access is blocked
        product_id (Union[Unset, str]): id of the product bought
        plenigo_offer_id (Union[Unset, str]): if the product is based on a plenigo offer the plenigo offer id is
            provided here
        plenigo_product_id (Union[Unset, str]): if the product is based on a plenigo offer the plenigo product id is
            provided here - can be identically to the productId
        plenigo_step_id (Union[Unset, str]): if the product is based on a plenigo offer the plenigo step id is provided
            here
        item_type (Union[Unset, AccessRightItemDataItemType]): type of this access right item
        item_id (Union[Unset, str]): the id this access right belongs to
        access_right_data (Union[Unset, AccessRightItemDataAccessRightData]): Key must be a string with a maximum length
            of 30 characters.
    """

    access_right_unique_id: str
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_by_type: Union[Unset, UserType] = UNSET
    changed_by: Union[Unset, str] = UNSET
    changed_by_type: Union[Unset, UserType] = UNSET
    life_time_start: Union[None, Unset, datetime.datetime] = UNSET
    life_time_end: Union[None, Unset, datetime.datetime] = UNSET
    access_time_start: Union[None, Unset, datetime.datetime] = UNSET
    access_time_end: Union[None, Unset, datetime.datetime] = UNSET
    max_cache_date: Union[None, Unset, datetime.datetime] = UNSET
    data: Union[Unset, "AccessRightItemDataData"] = UNSET
    blocked: Union[Unset, bool] = UNSET
    product_id: Union[Unset, str] = UNSET
    plenigo_offer_id: Union[Unset, str] = UNSET
    plenigo_product_id: Union[Unset, str] = UNSET
    plenigo_step_id: Union[Unset, str] = UNSET
    item_type: Union[Unset, AccessRightItemDataItemType] = UNSET
    item_id: Union[Unset, str] = UNSET
    access_right_data: Union[Unset, "AccessRightItemDataAccessRightData"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access_right_unique_id = self.access_right_unique_id

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

        life_time_start: Union[None, Unset, str]
        if isinstance(self.life_time_start, Unset) or self.life_time_start is None:
            life_time_start = UNSET
        elif isinstance(self.life_time_start, datetime.datetime):
            life_time_start = self.life_time_start.isoformat()
        else:
            life_time_start = self.life_time_start

        life_time_end: Union[None, Unset, str]
        if isinstance(self.life_time_end, Unset) or self.life_time_end is None:
            life_time_end = UNSET
        elif isinstance(self.life_time_end, datetime.datetime):
            life_time_end = self.life_time_end.isoformat()
        else:
            life_time_end = self.life_time_end

        access_time_start: Union[None, Unset, str]
        if isinstance(self.access_time_start, Unset) or self.access_time_start is None:
            access_time_start = UNSET
        elif isinstance(self.access_time_start, datetime.datetime):
            access_time_start = self.access_time_start.isoformat()
        else:
            access_time_start = self.access_time_start

        access_time_end: Union[None, Unset, str]
        if isinstance(self.access_time_end, Unset) or self.access_time_end is None:
            access_time_end = UNSET
        elif isinstance(self.access_time_end, datetime.datetime):
            access_time_end = self.access_time_end.isoformat()
        else:
            access_time_end = self.access_time_end

        max_cache_date: Union[None, Unset, str]
        if isinstance(self.max_cache_date, Unset) or self.max_cache_date is None:
            max_cache_date = UNSET
        elif isinstance(self.max_cache_date, datetime.datetime):
            max_cache_date = self.max_cache_date.isoformat()
        else:
            max_cache_date = self.max_cache_date

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        blocked = self.blocked

        product_id = self.product_id

        plenigo_offer_id = self.plenigo_offer_id

        plenigo_product_id = self.plenigo_product_id

        plenigo_step_id = self.plenigo_step_id

        item_type: Union[Unset, str] = UNSET
        if not isinstance(self.item_type, Unset):
            item_type = self.item_type.value

        item_id = self.item_id

        access_right_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.access_right_data, Unset):
            access_right_data = self.access_right_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accessRightUniqueId": access_right_unique_id,
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
        if life_time_start is not UNSET:
            field_dict["lifeTimeStart"] = life_time_start
        if life_time_end is not UNSET:
            field_dict["lifeTimeEnd"] = life_time_end
        if access_time_start is not UNSET:
            field_dict["accessTimeStart"] = access_time_start
        if access_time_end is not UNSET:
            field_dict["accessTimeEnd"] = access_time_end
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
        access_right_unique_id = d.pop("accessRightUniqueId")

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
        created_by_type: Union[Unset, UserType]
        if isinstance(_created_by_type, Unset) or not _created_by_type:
            created_by_type = UNSET
        else:
            created_by_type = UserType(_created_by_type)

        changed_by = d.pop("changedBy", UNSET)

        _changed_by_type = d.pop("changedByType", UNSET)
        changed_by_type: Union[Unset, UserType]
        if isinstance(_changed_by_type, Unset) or not _changed_by_type:
            changed_by_type = UNSET
        else:
            changed_by_type = UserType(_changed_by_type)

        def _parse_life_time_start(data: object) -> Union[None, Unset, datetime.datetime]:
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
                life_time_start_type_0 = isoparse(data)

                return life_time_start_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        life_time_start = _parse_life_time_start(d.pop("lifeTimeStart", UNSET))

        def _parse_life_time_end(data: object) -> Union[None, Unset, datetime.datetime]:
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
                life_time_end_type_0 = isoparse(data)

                return life_time_end_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        life_time_end = _parse_life_time_end(d.pop("lifeTimeEnd", UNSET))

        def _parse_access_time_start(data: object) -> Union[None, Unset, datetime.datetime]:
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
                access_time_start_type_0 = isoparse(data)

                return access_time_start_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        access_time_start = _parse_access_time_start(d.pop("accessTimeStart", UNSET))

        def _parse_access_time_end(data: object) -> Union[None, Unset, datetime.datetime]:
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
                access_time_end_type_0 = isoparse(data)

                return access_time_end_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        access_time_end = _parse_access_time_end(d.pop("accessTimeEnd", UNSET))

        def _parse_max_cache_date(data: object) -> Union[None, Unset, datetime.datetime]:
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
                max_cache_date_type_0 = isoparse(data)

                return max_cache_date_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        max_cache_date = _parse_max_cache_date(d.pop("maxCacheDate", UNSET))

        _data = d.pop("data", UNSET)
        data: Union[Unset, AccessRightItemDataData]
        if isinstance(_data, Unset) or not _data:
            data = UNSET
        else:
            data = AccessRightItemDataData.from_dict(_data)

        blocked = d.pop("blocked", UNSET)

        product_id = d.pop("productId", UNSET)

        plenigo_offer_id = d.pop("plenigoOfferId", UNSET)

        plenigo_product_id = d.pop("plenigoProductId", UNSET)

        plenigo_step_id = d.pop("plenigoStepId", UNSET)

        _item_type = d.pop("itemType", UNSET)
        item_type: Union[Unset, AccessRightItemDataItemType]
        if isinstance(_item_type, Unset) or not _item_type:
            item_type = UNSET
        else:
            item_type = AccessRightItemDataItemType(_item_type)

        item_id = d.pop("itemId", UNSET)

        _access_right_data = d.pop("accessRightData", UNSET)
        access_right_data: Union[Unset, AccessRightItemDataAccessRightData]
        if isinstance(_access_right_data, Unset) or not _access_right_data:
            access_right_data = UNSET
        else:
            access_right_data = AccessRightItemDataAccessRightData.from_dict(_access_right_data)

        access_right_item_data = cls(
            access_right_unique_id=access_right_unique_id,
            created_date=created_date,
            changed_date=changed_date,
            created_by=created_by,
            created_by_type=created_by_type,
            changed_by=changed_by,
            changed_by_type=changed_by_type,
            life_time_start=life_time_start,
            life_time_end=life_time_end,
            access_time_start=access_time_start,
            access_time_end=access_time_end,
            max_cache_date=max_cache_date,
            data=data,
            blocked=blocked,
            product_id=product_id,
            plenigo_offer_id=plenigo_offer_id,
            plenigo_product_id=plenigo_product_id,
            plenigo_step_id=plenigo_step_id,
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
