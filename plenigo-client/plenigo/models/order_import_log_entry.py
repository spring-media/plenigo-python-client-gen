import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_import_log_entry_error_detail import OrderImportLogEntryErrorDetail


T = TypeVar("T", bound="OrderImportLogEntry")


@_attrs_define
class OrderImportLogEntry:
    """
    Attributes:
        created_date (Union[None, Unset, datetime.datetime]): Time the object was created in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        changed_date (Union[None, Unset, datetime.datetime]): Time the object was changed in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        order_import_log_entry_id (Union[Unset, int]): unique id of the order import log entry
        external_system_id (Union[Unset, str]): external system id of the order import
        plenigo_offer_id (Union[Unset, str]): unique id of the offer within a company
        purchase_order_indicator (Union[Unset, str]): purchase order indicator to set
        success (Union[Unset, bool]): success state of the order import
        order_id (Union[Unset, int]): unique id of the order if success is true which was created by this import
        error_reason (Union[Unset, str]): reason for failure if success is false
        error_detail (Union[Unset, OrderImportLogEntryErrorDetail]): string or json object with error details
    """

    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    order_import_log_entry_id: Union[Unset, int] = UNSET
    external_system_id: Union[Unset, str] = UNSET
    plenigo_offer_id: Union[Unset, str] = UNSET
    purchase_order_indicator: Union[Unset, str] = UNSET
    success: Union[Unset, bool] = UNSET
    order_id: Union[Unset, int] = UNSET
    error_reason: Union[Unset, str] = UNSET
    error_detail: Union[Unset, "OrderImportLogEntryErrorDetail"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

        order_import_log_entry_id = self.order_import_log_entry_id

        external_system_id = self.external_system_id

        plenigo_offer_id = self.plenigo_offer_id

        purchase_order_indicator = self.purchase_order_indicator

        success = self.success

        order_id = self.order_id

        error_reason = self.error_reason

        error_detail: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.error_detail, Unset):
            error_detail = self.error_detail.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if order_import_log_entry_id is not UNSET:
            field_dict["orderImportLogEntryId"] = order_import_log_entry_id
        if external_system_id is not UNSET:
            field_dict["externalSystemId"] = external_system_id
        if plenigo_offer_id is not UNSET:
            field_dict["plenigoOfferId"] = plenigo_offer_id
        if purchase_order_indicator is not UNSET:
            field_dict["purchaseOrderIndicator"] = purchase_order_indicator
        if success is not UNSET:
            field_dict["success"] = success
        if order_id is not UNSET:
            field_dict["orderId"] = order_id
        if error_reason is not UNSET:
            field_dict["errorReason"] = error_reason
        if error_detail is not UNSET:
            field_dict["errorDetail"] = error_detail

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order_import_log_entry_error_detail import OrderImportLogEntryErrorDetail

        d = src_dict.copy()

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

        order_import_log_entry_id = d.pop("orderImportLogEntryId", UNSET)

        external_system_id = d.pop("externalSystemId", UNSET)

        plenigo_offer_id = d.pop("plenigoOfferId", UNSET)

        purchase_order_indicator = d.pop("purchaseOrderIndicator", UNSET)

        success = d.pop("success", UNSET)

        order_id = d.pop("orderId", UNSET)

        error_reason = d.pop("errorReason", UNSET)

        _error_detail = d.pop("errorDetail", UNSET)
        error_detail: Union[Unset, OrderImportLogEntryErrorDetail]
        if isinstance(_error_detail, Unset) or not _error_detail:
            error_detail = UNSET
        else:
            error_detail = OrderImportLogEntryErrorDetail.from_dict(_error_detail)

        order_import_log_entry = cls(
            created_date=created_date,
            changed_date=changed_date,
            order_import_log_entry_id=order_import_log_entry_id,
            external_system_id=external_system_id,
            plenigo_offer_id=plenigo_offer_id,
            purchase_order_indicator=purchase_order_indicator,
            success=success,
            order_id=order_id,
            error_reason=error_reason,
            error_detail=error_detail,
        )

        order_import_log_entry.additional_properties = d
        return order_import_log_entry

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
