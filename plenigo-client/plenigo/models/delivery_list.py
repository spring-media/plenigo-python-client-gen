import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.delivery_list_type import DeliveryListType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delivery_list_change_additional_data import DeliveryListChangeAdditionalData


T = TypeVar("T", bound="DeliveryList")


@_attrs_define
class DeliveryList:
    """
    Attributes:
        title (str): title of the delivery list
        file_name_part (str): file name part of the delivery list
        description (Union[Unset, str]): description of the delivery list
        check_reminder_receivers (Union[Unset, str]): comma separated list of email receivers for reminders if not
            enough delivery dates are inserted
        check_date_interval_weeks (Union[Unset, int]): interval in weeks to inform merchant that there are not enough
            delivery dates
        export_configuration_id (Union[Unset, int]): id of the export configuration that should be used with the
            delivery list
        goodwill_offer_id (Union[Unset, int]): id of the goodwill offer that should be used with the delivery list. The
            offer must be a single product with a zero price issue.
        enabled (Union[Unset, bool]): flag indicating if delivery list is enabled
        additional_data (Union[Unset, DeliveryListChangeAdditionalData]):
        created_date (Union[None, Unset, datetime.datetime]): time the object was created with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        changed_date (Union[None, Unset, datetime.datetime]): time the object was changed with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        type (Union[Unset, DeliveryListType]): type of the delivery list
        delivery_list_id (Union[Unset, int]): id of the delivery list the delivery date belongs to
    """

    title: str
    file_name_part: str
    description: Union[Unset, str] = UNSET
    check_reminder_receivers: Union[Unset, str] = UNSET
    check_date_interval_weeks: Union[Unset, int] = UNSET
    export_configuration_id: Union[Unset, int] = UNSET
    goodwill_offer_id: Union[Unset, int] = UNSET
    enabled: Union[Unset, bool] = UNSET
    additional_data: Union[Unset, "DeliveryListChangeAdditionalData"] = UNSET
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    type: Union[Unset, DeliveryListType] = UNSET
    delivery_list_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title

        file_name_part = self.file_name_part

        description = self.description

        check_reminder_receivers = self.check_reminder_receivers

        check_date_interval_weeks = self.check_date_interval_weeks

        export_configuration_id = self.export_configuration_id

        goodwill_offer_id = self.goodwill_offer_id

        enabled = self.enabled

        additional_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.additional_data, Unset):
            additional_data = self.additional_data.to_dict()

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

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        delivery_list_id = self.delivery_list_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "fileNamePart": file_name_part,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if check_reminder_receivers is not UNSET:
            field_dict["checkReminderReceivers"] = check_reminder_receivers
        if check_date_interval_weeks is not UNSET:
            field_dict["checkDateIntervalWeeks"] = check_date_interval_weeks
        if export_configuration_id is not UNSET:
            field_dict["exportConfigurationId"] = export_configuration_id
        if goodwill_offer_id is not UNSET:
            field_dict["goodwillOfferId"] = goodwill_offer_id
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if additional_data is not UNSET:
            field_dict["additionalData"] = additional_data
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if type is not UNSET:
            field_dict["type"] = type
        if delivery_list_id is not UNSET:
            field_dict["deliveryListId"] = delivery_list_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.delivery_list_change_additional_data import DeliveryListChangeAdditionalData

        d = src_dict.copy()
        title = d.pop("title")

        file_name_part = d.pop("fileNamePart")

        description = d.pop("description", UNSET)

        check_reminder_receivers = d.pop("checkReminderReceivers", UNSET)

        check_date_interval_weeks = d.pop("checkDateIntervalWeeks", UNSET)

        export_configuration_id = d.pop("exportConfigurationId", UNSET)

        goodwill_offer_id = d.pop("goodwillOfferId", UNSET)

        enabled = d.pop("enabled", UNSET)

        _additional_data = d.pop("additionalData", UNSET)
        additional_data: Union[Unset, DeliveryListChangeAdditionalData]
        if isinstance(_additional_data, Unset) or not _additional_data:
            additional_data = UNSET
        else:
            additional_data = DeliveryListChangeAdditionalData.from_dict(_additional_data)

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
                created_date_type_1 = isoparse(data)

                return created_date_type_1
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
                changed_date_type_1 = isoparse(data)

                return changed_date_type_1
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        changed_date = _parse_changed_date(d.pop("changedDate", UNSET))

        _type = d.pop("type", UNSET)
        type: Union[Unset, DeliveryListType]
        if isinstance(_type, Unset) or not _type:
            type = UNSET
        else:
            type = DeliveryListType(_type)

        delivery_list_id = d.pop("deliveryListId", UNSET)

        delivery_list = cls(
            title=title,
            file_name_part=file_name_part,
            description=description,
            check_reminder_receivers=check_reminder_receivers,
            check_date_interval_weeks=check_date_interval_weeks,
            export_configuration_id=export_configuration_id,
            goodwill_offer_id=goodwill_offer_id,
            enabled=enabled,
            additional_data=additional_data,
            created_date=created_date,
            changed_date=changed_date,
            type=type,
            delivery_list_id=delivery_list_id,
        )

        delivery_list.additional_properties = d
        return delivery_list

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
