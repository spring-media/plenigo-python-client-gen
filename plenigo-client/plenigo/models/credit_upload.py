import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.credit_upload_item_type import CreditUploadItemType
from ..models.user_type import UserType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreditUpload")


@_attrs_define
class CreditUpload:
    """
    Attributes:
        customer_id (str): id of the customer the credit usage should be accounted to
        unique_id (str): unique id of the wallet to use
        upload_date (Union[None, datetime.datetime]): date the upload was done with date-time notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-21T17:32:28Z
        credit_upload_id (int): unique id of the credit upload also used for pagination
        title (str): title of upload
        credits_added (int): amount of credits added
        item_type (CreditUploadItemType): type of this access right item
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
        item_id (Union[Unset, str]): the id this access right belongs to
    """

    customer_id: str
    unique_id: str
    upload_date: Union[None, datetime.datetime]
    credit_upload_id: int
    title: str
    credits_added: int
    item_type: CreditUploadItemType
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_by_type: Union[Unset, UserType] = UNSET
    changed_by: Union[Unset, str] = UNSET
    changed_by_type: Union[Unset, UserType] = UNSET
    item_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer_id = self.customer_id

        unique_id = self.unique_id

        upload_date: Union[None, str]
        if isinstance(self.upload_date, datetime.datetime):
            upload_date = self.upload_date.isoformat()
        else:
            upload_date = self.upload_date

        credit_upload_id = self.credit_upload_id

        title = self.title

        credits_added = self.credits_added

        item_type = self.item_type.value

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

        item_id = self.item_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customerId": customer_id,
                "uniqueId": unique_id,
                "uploadDate": upload_date,
                "creditUploadId": credit_upload_id,
                "title": title,
                "creditsAdded": credits_added,
                "itemType": item_type,
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
        if item_id is not UNSET:
            field_dict["itemId"] = item_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        customer_id = d.pop("customerId")

        unique_id = d.pop("uniqueId")

        def _parse_upload_date(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data

            # Try to parse the data as datetime.datetime
            try:
                if not isinstance(data, str):
                    raise TypeError()
                upload_date_type_0 = isoparse(data)

                return upload_date_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, datetime.datetime], data)

        upload_date = _parse_upload_date(d.pop("uploadDate"))

        credit_upload_id = d.pop("creditUploadId")

        title = d.pop("title")

        credits_added = d.pop("creditsAdded")

        item_type = CreditUploadItemType(d.pop("itemType"))

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

        item_id = d.pop("itemId", UNSET)

        credit_upload = cls(
            customer_id=customer_id,
            unique_id=unique_id,
            upload_date=upload_date,
            credit_upload_id=credit_upload_id,
            title=title,
            credits_added=credits_added,
            item_type=item_type,
            created_date=created_date,
            changed_date=changed_date,
            created_by=created_by,
            created_by_type=created_by_type,
            changed_by=changed_by,
            changed_by_type=changed_by_type,
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
