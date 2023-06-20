import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.credit_upload_item_type import CreditUploadItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreditUpload")


@attr.s(auto_attribs=True)
class CreditUpload:
    """
    Attributes:
        customer_id (Union[Unset, str]): id of the customer the credit usage should be accounted to
        unique_id (Union[Unset, str]): unique id of the wallet to use
        upload_date (Union[Unset, datetime.datetime]): date the upload was done with date-time notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-21T17:32:28Z
        credit_upload_id (Union[Unset, int]): unique id of the credit upload also used for pagination
        title (Union[Unset, str]): title of upload
        credits_added (Union[Unset, int]): amount of credits added
        item_type (Union[Unset, CreditUploadItemType]): type of this access right item
        item_id (Union[Unset, str]): the id this access right belongs to
    """

    customer_id: Union[Unset, str] = UNSET
    unique_id: Union[Unset, str] = UNSET
    upload_date: Union[Unset, datetime.datetime] = UNSET
    credit_upload_id: Union[Unset, int] = UNSET
    title: Union[Unset, str] = UNSET
    credits_added: Union[Unset, int] = UNSET
    item_type: Union[Unset, CreditUploadItemType] = UNSET
    item_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer_id = self.customer_id
        unique_id = self.unique_id
        upload_date: Union[Unset, str] = UNSET
        if not isinstance(self.upload_date, Unset):
            upload_date = self.upload_date.isoformat()

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
        customer_id = d.pop("customerId", UNSET)

        unique_id = d.pop("uniqueId", UNSET)

        _upload_date = d.pop("uploadDate", UNSET)
        upload_date: Union[Unset, datetime.datetime]
        if isinstance(_upload_date, Unset):
            upload_date = UNSET
        else:
            upload_date = isoparse(_upload_date)

        credit_upload_id = d.pop("creditUploadId", UNSET)

        title = d.pop("title", UNSET)

        credits_added = d.pop("creditsAdded", UNSET)

        _item_type = d.pop("itemType", UNSET)
        item_type: Union[Unset, CreditUploadItemType]
        if isinstance(_item_type, Unset):
            item_type = UNSET
        else:
            item_type = CreditUploadItemType(_item_type)

        item_id = d.pop("itemId", UNSET)

        credit_upload = cls(
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
