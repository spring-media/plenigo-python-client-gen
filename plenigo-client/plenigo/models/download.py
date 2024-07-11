import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_base_changed_by_type import ApiBaseChangedByType
from ..models.api_base_created_by_type import ApiBaseCreatedByType
from ..models.download_download_type import DownloadDownloadType
from ..models.download_file_type import DownloadFileType
from ..models.download_published_by_type import DownloadPublishedByType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Download")


@_attrs_define
class Download:
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
        download_id (Union[Unset, int]): unique id of the download
        uploaded_date (Union[None, Unset, datetime.datetime]): date time the download was uploaded with date-time
            notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339,
            section 5.6</a>, for example, 2017-07-21T17:32:28Z
        download_type (Union[Unset, DownloadDownloadType]): download type to get downloads for
        file_type (Union[Unset, DownloadFileType]): file type of the download
        file_size (Union[Unset, int]): file size of the download
        file_name (Union[Unset, str]): file name of the download
        published_token (Union[Unset, str]): published token contains the token to identify the password via the
            download
        published_end_date (Union[None, Unset, datetime.datetime]): date the publish of the download will end with date-
            time notation as defined by RFC 3339, section 5.6, for example, 2017-07-21T17:32:28Z
        published_by (Union[Unset, str]): id who published the download
        published_by_type (Union[Unset, DownloadPublishedByType]): type of published by
    """

    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_by_type: Union[Unset, ApiBaseCreatedByType] = UNSET
    changed_by: Union[Unset, str] = UNSET
    changed_by_type: Union[Unset, ApiBaseChangedByType] = UNSET
    download_id: Union[Unset, int] = UNSET
    uploaded_date: Union[None, Unset, datetime.datetime] = UNSET
    download_type: Union[Unset, DownloadDownloadType] = UNSET
    file_type: Union[Unset, DownloadFileType] = UNSET
    file_size: Union[Unset, int] = UNSET
    file_name: Union[Unset, str] = UNSET
    published_token: Union[Unset, str] = UNSET
    published_end_date: Union[None, Unset, datetime.datetime] = UNSET
    published_by: Union[Unset, str] = UNSET
    published_by_type: Union[Unset, DownloadPublishedByType] = UNSET
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

        created_by = self.created_by

        created_by_type: Union[Unset, str] = UNSET
        if not isinstance(self.created_by_type, Unset):
            created_by_type = self.created_by_type.value

        changed_by = self.changed_by

        changed_by_type: Union[Unset, str] = UNSET
        if not isinstance(self.changed_by_type, Unset):
            changed_by_type = self.changed_by_type.value

        download_id = self.download_id

        uploaded_date: Union[None, Unset, str]
        if isinstance(self.uploaded_date, Unset):
            uploaded_date = UNSET
        elif isinstance(self.uploaded_date, datetime.datetime):
            uploaded_date = self.uploaded_date.isoformat()
        else:
            uploaded_date = self.uploaded_date

        download_type: Union[Unset, str] = UNSET
        if not isinstance(self.download_type, Unset):
            download_type = self.download_type.value

        file_type: Union[Unset, str] = UNSET
        if not isinstance(self.file_type, Unset):
            file_type = self.file_type.value

        file_size = self.file_size

        file_name = self.file_name

        published_token = self.published_token

        published_end_date: Union[None, Unset, str]
        if isinstance(self.published_end_date, Unset):
            published_end_date = UNSET
        elif isinstance(self.published_end_date, datetime.datetime):
            published_end_date = self.published_end_date.isoformat()
        else:
            published_end_date = self.published_end_date

        published_by = self.published_by

        published_by_type: Union[Unset, str] = UNSET
        if not isinstance(self.published_by_type, Unset):
            published_by_type = self.published_by_type.value

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
        if download_id is not UNSET:
            field_dict["downloadId"] = download_id
        if uploaded_date is not UNSET:
            field_dict["uploadedDate"] = uploaded_date
        if download_type is not UNSET:
            field_dict["downloadType"] = download_type
        if file_type is not UNSET:
            field_dict["fileType"] = file_type
        if file_size is not UNSET:
            field_dict["fileSize"] = file_size
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if published_token is not UNSET:
            field_dict["publishedToken"] = published_token
        if published_end_date is not UNSET:
            field_dict["publishedEndDate"] = published_end_date
        if published_by is not UNSET:
            field_dict["publishedBy"] = published_by
        if published_by_type is not UNSET:
            field_dict["publishedByType"] = published_by_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
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

        download_id = d.pop("downloadId", UNSET)

        def _parse_uploaded_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                uploaded_date_type_0 = isoparse(data)

                return uploaded_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        uploaded_date = _parse_uploaded_date(d.pop("uploadedDate", UNSET))

        _download_type = d.pop("downloadType", UNSET)
        download_type: Union[Unset, DownloadDownloadType]
        if isinstance(_download_type, Unset):
            download_type = UNSET
        else:
            download_type = DownloadDownloadType(_download_type)

        _file_type = d.pop("fileType", UNSET)
        file_type: Union[Unset, DownloadFileType]
        if isinstance(_file_type, Unset):
            file_type = UNSET
        else:
            file_type = DownloadFileType(_file_type)

        file_size = d.pop("fileSize", UNSET)

        file_name = d.pop("fileName", UNSET)

        published_token = d.pop("publishedToken", UNSET)

        def _parse_published_end_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                published_end_date_type_0 = isoparse(data)

                return published_end_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        published_end_date = _parse_published_end_date(d.pop("publishedEndDate", UNSET))

        published_by = d.pop("publishedBy", UNSET)

        _published_by_type = d.pop("publishedByType", UNSET)
        published_by_type: Union[Unset, DownloadPublishedByType]
        if isinstance(_published_by_type, Unset):
            published_by_type = UNSET
        else:
            published_by_type = DownloadPublishedByType(_published_by_type)

        download = cls(
            created_date=created_date,
            changed_date=changed_date,
            created_by=created_by,
            created_by_type=created_by_type,
            changed_by=changed_by,
            changed_by_type=changed_by_type,
            download_id=download_id,
            uploaded_date=uploaded_date,
            download_type=download_type,
            file_type=file_type,
            file_size=file_size,
            file_name=file_name,
            published_token=published_token,
            published_end_date=published_end_date,
            published_by=published_by,
            published_by_type=published_by_type,
        )

        download.additional_properties = d
        return download

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
