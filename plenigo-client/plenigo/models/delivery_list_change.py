from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delivery_list_change_additional_data import DeliveryListChangeAdditionalData


T = TypeVar("T", bound="DeliveryListChange")


@attr.s(auto_attribs=True)
class DeliveryListChange:
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
        enabled (Union[Unset, bool]): flag indicating if delivery list is enabled
        additional_data (Union[Unset, DeliveryListChangeAdditionalData]):
    """

    title: str
    file_name_part: str
    description: Union[Unset, str] = UNSET
    check_reminder_receivers: Union[Unset, str] = UNSET
    check_date_interval_weeks: Union[Unset, int] = UNSET
    export_configuration_id: Union[Unset, int] = UNSET
    enabled: Union[Unset, bool] = UNSET
    additional_data: Union[Unset, "DeliveryListChangeAdditionalData"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        file_name_part = self.file_name_part
        description = self.description
        check_reminder_receivers = self.check_reminder_receivers
        check_date_interval_weeks = self.check_date_interval_weeks
        export_configuration_id = self.export_configuration_id
        enabled = self.enabled
        additional_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.additional_data, Unset):
            additional_data = self.additional_data.to_dict()

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
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if additional_data is not UNSET:
            field_dict["additionalData"] = additional_data

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

        enabled = d.pop("enabled", UNSET)

        _additional_data = d.pop("additionalData", UNSET)
        additional_data: Union[Unset, DeliveryListChangeAdditionalData]
        if isinstance(_additional_data, Unset):
            additional_data = UNSET
        else:
            additional_data = DeliveryListChangeAdditionalData.from_dict(_additional_data)

        delivery_list_change = cls(
            title=title,
            file_name_part=file_name_part,
            description=description,
            check_reminder_receivers=check_reminder_receivers,
            check_date_interval_weeks=check_date_interval_weeks,
            export_configuration_id=export_configuration_id,
            enabled=enabled,
            additional_data=additional_data,
        )

        delivery_list_change.additional_properties = d
        return delivery_list_change

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
