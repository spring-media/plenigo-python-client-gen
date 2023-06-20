import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.download_download_type import DownloadDownloadType
from ..models.download_file_type import DownloadFileType
from ..models.download_published_by_type import DownloadPublishedByType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Download")


@attr.s(auto_attribs=True)
class Download:
    """
    Attributes:
        download_id (Union[Unset, int]): unique id of the download
        uploaded_date (Union[Unset, datetime.datetime]): date time the download was uploaded with date-time notation as
            defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>,
            for example, 2017-07-21T17:32:28Z
        download_type (Union[Unset, DownloadDownloadType]): download type to get downloads for
        file_type (Union[Unset, DownloadFileType]): file type of the download
        file_size (Union[Unset, int]): file size of the download
        file_name (Union[Unset, str]): file name of the download
        published_token (Union[Unset, bool]): published token for download
        published_end_date (Union[Unset, datetime.datetime]): date the publish of the download will end with date-time
            notation as defined by RFC 3339, section 5.6, for example, 2017-07-21T17:32:28Z
        published_by (Union[Unset, str]): id who published the download
        published_by_type (Union[Unset, DownloadPublishedByType]): type of published by
    """

    download_id: Union[Unset, int] = UNSET
    uploaded_date: Union[Unset, datetime.datetime] = UNSET
    download_type: Union[Unset, DownloadDownloadType] = UNSET
    file_type: Union[Unset, DownloadFileType] = UNSET
    file_size: Union[Unset, int] = UNSET
    file_name: Union[Unset, str] = UNSET
    published_token: Union[Unset, bool] = UNSET
    published_end_date: Union[Unset, datetime.datetime] = UNSET
    published_by: Union[Unset, str] = UNSET
    published_by_type: Union[Unset, DownloadPublishedByType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        download_id = self.download_id
        uploaded_date: Union[Unset, str] = UNSET
        if not isinstance(self.uploaded_date, Unset):
            uploaded_date = self.uploaded_date.isoformat()

        download_type: Union[Unset, str] = UNSET
        if not isinstance(self.download_type, Unset):
            download_type = self.download_type.value

        file_type: Union[Unset, str] = UNSET
        if not isinstance(self.file_type, Unset):
            file_type = self.file_type.value

        file_size = self.file_size
        file_name = self.file_name
        published_token = self.published_token
        published_end_date: Union[Unset, str] = UNSET
        if not isinstance(self.published_end_date, Unset):
            published_end_date = self.published_end_date.isoformat()

        published_by = self.published_by
        published_by_type: Union[Unset, str] = UNSET
        if not isinstance(self.published_by_type, Unset):
            published_by_type = self.published_by_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        download_id = d.pop("downloadId", UNSET)

        _uploaded_date = d.pop("uploadedDate", UNSET)
        uploaded_date: Union[Unset, datetime.datetime]
        if isinstance(_uploaded_date, Unset):
            uploaded_date = UNSET
        else:
            uploaded_date = isoparse(_uploaded_date)

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

        _published_end_date = d.pop("publishedEndDate", UNSET)
        published_end_date: Union[Unset, datetime.datetime]
        if isinstance(_published_end_date, Unset):
            published_end_date = UNSET
        else:
            published_end_date = isoparse(_published_end_date)

        published_by = d.pop("publishedBy", UNSET)

        _published_by_type = d.pop("publishedByType", UNSET)
        published_by_type: Union[Unset, DownloadPublishedByType]
        if isinstance(_published_by_type, Unset):
            published_by_type = UNSET
        else:
            published_by_type = DownloadPublishedByType(_published_by_type)

        download = cls(
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
