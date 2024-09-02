import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_base_changed_by_type import ApiBaseChangedByType
from ..models.api_base_created_by_type import ApiBaseCreatedByType
from ..models.credit_upload_item_type import CreditUploadItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreditUpload")


@_attrs_define
class CreditUpload:
    """
    Attributes:
        created_date (Union[None, Unset, datetime.datetime]): Time the object was created in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        changed_date (Union[None, Unset, datetime.datetime]): Time the object was changed in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        created_by (Union[Unset, str]): ID of who created the object
        created_by_type (Union[Unset, ApiBaseCreatedByType]): Type of creator
        changed_by (Union[Unset, str]): ID of who changed the object
        changed_by_type (Union[Unset, ApiBaseChangedByType]): Type of changer
        customer_id (Union[Unset, str]): id of the customer the credit usage should be accounted to
        unique_id (Union[Unset, str]): unique id of the wallet to use
        upload_date (Union[None, Unset, datetime.datetime]): date the upload was done with date-time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 2017-07-21T17:32:28Z
        credit_upload_id (Union[Unset, int]): unique id of the credit upload also used for pagination
        title (Union[Unset, str]): title of upload
        credits_added (Union[Unset, int]): amount of credits added
        item_type (Union[Unset, CreditUploadItemType]): type of this access right item
        item_id (Union[Unset, str]): the id this access right belongs to
    """

    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_by_type: Union[Unset, ApiBaseCreatedByType] = UNSET
    changed_by: Union[Unset, str] = UNSET
    changed_by_type: Union[Unset, ApiBaseChangedByType] = UNSET
    customer_id: Union[Unset, str] = UNSET
    unique_id: Union[Unset, str] = UNSET
    upload_date: Union[None, Unset, datetime.datetime] = UNSET
    credit_upload_id: Union[Unset, int] = UNSET
    title: Union[Unset, str] = UNSET
    credits_added: Union[Unset, int] = UNSET
    item_type: Union[Unset, CreditUploadItemType] = UNSET
    item_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

        customer_id = self.customer_id

        unique_id = self.unique_id

        upload_date: Union[None, Unset, str]
        if isinstance(self.upload_date, Unset) or self.upload_date is None:
            upload_date = UNSET
        elif isinstance(self.upload_date, datetime.datetime):
            upload_date = self.upload_date.isoformat()
        else:
            upload_date = self.upload_date

        credit_upload_id = self.credit_upload_id

        title = self.title

        credits_added = self.credits_added

        item_type: Union[Unset, str] = UNSET
        if not isinstance(self.item_type, Unset):
            item_type = self.item_type.value

        item_id = self.item_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if unique_id is not UNSET:
            field_dict["uniqueId"] = unique_id
        if upload_date is not UNSET:
            field_dict["uploadDate"] = upload_date
        if credit_upload_id is not UNSET:
            field_dict["creditUploadId"] = credit_upload_id
        if title is not UNSET:
            field_dict["title"] = title
        if credits_added is not UNSET:
            field_dict["creditsAdded"] = credits_added
        if item_type is not UNSET:
            field_dict["itemType"] = item_type
        if item_id is not UNSET:
            field_dict["itemId"] = item_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

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
        created_by_type: Union[Unset, ApiBaseCreatedByType]
        if isinstance(_created_by_type, Unset) or not _created_by_type:
            created_by_type = UNSET
        else:
            created_by_type = ApiBaseCreatedByType(_created_by_type)

        changed_by = d.pop("changedBy", UNSET)

        _changed_by_type = d.pop("changedByType", UNSET)
        changed_by_type: Union[Unset, ApiBaseChangedByType]
        if isinstance(_changed_by_type, Unset) or not _changed_by_type:
            changed_by_type = UNSET
        else:
            changed_by_type = ApiBaseChangedByType(_changed_by_type)

        customer_id = d.pop("customerId", UNSET)

        unique_id = d.pop("uniqueId", UNSET)

        def _parse_upload_date(data: object) -> Union[None, Unset, datetime.datetime]:
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
                upload_date_type_0 = isoparse(data)

                return upload_date_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        upload_date = _parse_upload_date(d.pop("uploadDate", UNSET))

        credit_upload_id = d.pop("creditUploadId", UNSET)

        title = d.pop("title", UNSET)

        credits_added = d.pop("creditsAdded", UNSET)

        _item_type = d.pop("itemType", UNSET)
        item_type: Union[Unset, CreditUploadItemType]
        if isinstance(_item_type, Unset) or not _item_type:
            item_type = UNSET
        else:
            item_type = CreditUploadItemType(_item_type)

        item_id = d.pop("itemId", UNSET)

        credit_upload = cls(
            created_date=created_date,
            changed_date=changed_date,
            created_by=created_by,
            created_by_type=created_by_type,
            changed_by=changed_by,
            changed_by_type=changed_by_type,
            customer_id=customer_id,
            unique_id=unique_id,
            upload_date=upload_date,
            credit_upload_id=credit_upload_id,
            title=title,
            credits_added=credits_added,
            item_type=item_type,
            item_id=item_id,
        )

        credit_upload.additional_properties = d
        return credit_upload

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
