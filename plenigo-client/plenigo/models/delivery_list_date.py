import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_base_changed_by_type import ApiBaseChangedByType
from ..models.api_base_created_by_type import ApiBaseCreatedByType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delivery_list_dates_creation_additional_data import DeliveryListDatesCreationAdditionalData


T = TypeVar("T", bound="DeliveryListDate")


@_attrs_define
class DeliveryListDate:
    """
    Attributes:
        title (str): title of the delivery list date
        publishing_date (Union[None, datetime.datetime]): date the item associated with the delivery list is published
        cost_center (Union[Unset, str]): Cost center of the delivery date
        purchase_number (Union[Unset, str]): Purchase number to use
        delivery_date (Union[None, Unset, datetime.datetime]): date the delivery list should be created at with full-
            date notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339,
            section 5.6</a>, for example, 2017-07-21
        redelivery_date (Union[None, Unset, datetime.datetime]): date the redelivery list should be created at with
            full-date notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC
            3339, section 5.6</a>, for example, 2017-07-21
        additional_data (Union[Unset, DeliveryListDatesCreationAdditionalData]):
        translations (Union[Unset, Any]): translations for the end user
        delivery_list_date_id (Union[Unset, int]): id of the delivery date
        created_date (Union[None, Unset, datetime.datetime]): Time the object was created in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        changed_date (Union[None, Unset, datetime.datetime]): Time the object was changed in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        created_by (Union[Unset, str]): ID of who created the object
        created_by_type (Union[Unset, ApiBaseCreatedByType]): Type of creator
        changed_by (Union[Unset, str]): ID of who changed the object
        changed_by_type (Union[Unset, ApiBaseChangedByType]): Type of changer
        delivery_list_created_at (Union[None, Unset, datetime.datetime]): creation date of the delivery list with full-
            date notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339,
            section 5.6</a>, for example, 2017-07-21
        redelivery_list_created_at (Union[None, Unset, datetime.datetime]): creation date of the redelivery list with
            full-date notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC
            3339, section 5.6</a>, for example, 2017-07-21
    """

    title: str
    publishing_date: Union[None, datetime.datetime]
    cost_center: Union[Unset, str] = UNSET
    purchase_number: Union[Unset, str] = UNSET
    delivery_date: Union[None, Unset, datetime.datetime] = UNSET
    redelivery_date: Union[None, Unset, datetime.datetime] = UNSET
    additional_data: Union[Unset, "DeliveryListDatesCreationAdditionalData"] = UNSET
    translations: Union[Unset, Any] = UNSET
    delivery_list_date_id: Union[Unset, int] = UNSET
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_by_type: Union[Unset, ApiBaseCreatedByType] = UNSET
    changed_by: Union[Unset, str] = UNSET
    changed_by_type: Union[Unset, ApiBaseChangedByType] = UNSET
    delivery_list_created_at: Union[None, Unset, datetime.datetime] = UNSET
    redelivery_list_created_at: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title

        publishing_date: Union[None, str]
        if isinstance(self.publishing_date, datetime.datetime):
            publishing_date = self.publishing_date.isoformat()
        else:
            publishing_date = self.publishing_date

        cost_center = self.cost_center

        purchase_number = self.purchase_number

        delivery_date: Union[None, Unset, str]
        if isinstance(self.delivery_date, Unset):
            delivery_date = UNSET
        elif isinstance(self.delivery_date, datetime.datetime):
            delivery_date = self.delivery_date.isoformat()
        else:
            delivery_date = self.delivery_date

        redelivery_date: Union[None, Unset, str]
        if isinstance(self.redelivery_date, Unset):
            redelivery_date = UNSET
        elif isinstance(self.redelivery_date, datetime.datetime):
            redelivery_date = self.redelivery_date.isoformat()
        else:
            redelivery_date = self.redelivery_date

        additional_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.additional_data, Unset):
            additional_data = self.additional_data.to_dict()

        translations = self.translations

        delivery_list_date_id = self.delivery_list_date_id

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

        delivery_list_created_at: Union[None, Unset, str]
        if isinstance(self.delivery_list_created_at, Unset):
            delivery_list_created_at = UNSET
        elif isinstance(self.delivery_list_created_at, datetime.datetime):
            delivery_list_created_at = self.delivery_list_created_at.isoformat()
        else:
            delivery_list_created_at = self.delivery_list_created_at

        redelivery_list_created_at: Union[None, Unset, str]
        if isinstance(self.redelivery_list_created_at, Unset):
            redelivery_list_created_at = UNSET
        elif isinstance(self.redelivery_list_created_at, datetime.datetime):
            redelivery_list_created_at = self.redelivery_list_created_at.isoformat()
        else:
            redelivery_list_created_at = self.redelivery_list_created_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "publishingDate": publishing_date,
            }
        )
        if cost_center is not UNSET:
            field_dict["costCenter"] = cost_center
        if purchase_number is not UNSET:
            field_dict["purchaseNumber"] = purchase_number
        if delivery_date is not UNSET:
            field_dict["deliveryDate"] = delivery_date
        if redelivery_date is not UNSET:
            field_dict["redeliveryDate"] = redelivery_date
        if additional_data is not UNSET:
            field_dict["additionalData"] = additional_data
        if translations is not UNSET:
            field_dict["translations"] = translations
        if delivery_list_date_id is not UNSET:
            field_dict["deliveryListDateId"] = delivery_list_date_id
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
        if delivery_list_created_at is not UNSET:
            field_dict["deliveryListCreatedAt"] = delivery_list_created_at
        if redelivery_list_created_at is not UNSET:
            field_dict["redeliveryListCreatedAt"] = redelivery_list_created_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.delivery_list_dates_creation_additional_data import DeliveryListDatesCreationAdditionalData

        d = src_dict.copy()
        title = d.pop("title")

        def _parse_publishing_date(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                publishing_date_type_0 = isoparse(data)

                return publishing_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        publishing_date = _parse_publishing_date(d.pop("publishingDate"))

        cost_center = d.pop("costCenter", UNSET)

        purchase_number = d.pop("purchaseNumber", UNSET)

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

        def _parse_redelivery_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                redelivery_date_type_0 = isoparse(data)

                return redelivery_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        redelivery_date = _parse_redelivery_date(d.pop("redeliveryDate", UNSET))

        _additional_data = d.pop("additionalData", UNSET)
        additional_data: Union[Unset, DeliveryListDatesCreationAdditionalData]
        if isinstance(_additional_data, Unset):
            additional_data = UNSET
        else:
            additional_data = DeliveryListDatesCreationAdditionalData.from_dict(_additional_data)

        translations = d.pop("translations", UNSET)

        delivery_list_date_id = d.pop("deliveryListDateId", UNSET)

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

        def _parse_delivery_list_created_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delivery_list_created_at_type_0 = isoparse(data)

                return delivery_list_created_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        delivery_list_created_at = _parse_delivery_list_created_at(d.pop("deliveryListCreatedAt", UNSET))

        def _parse_redelivery_list_created_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                redelivery_list_created_at_type_0 = isoparse(data)

                return redelivery_list_created_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        redelivery_list_created_at = _parse_redelivery_list_created_at(d.pop("redeliveryListCreatedAt", UNSET))

        delivery_list_date = cls(
            title=title,
            publishing_date=publishing_date,
            cost_center=cost_center,
            purchase_number=purchase_number,
            delivery_date=delivery_date,
            redelivery_date=redelivery_date,
            additional_data=additional_data,
            translations=translations,
            delivery_list_date_id=delivery_list_date_id,
            created_date=created_date,
            changed_date=changed_date,
            created_by=created_by,
            created_by_type=created_by_type,
            changed_by=changed_by,
            changed_by_type=changed_by_type,
            delivery_list_created_at=delivery_list_created_at,
            redelivery_list_created_at=redelivery_list_created_at,
        )

        delivery_list_date.additional_properties = d
        return delivery_list_date

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
