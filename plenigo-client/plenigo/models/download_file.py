from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.download_file_file_type import DownloadFileFileType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DownloadFile")


@_attrs_define
class DownloadFile:
    """
    Attributes:
        file_type (Union[Unset, DownloadFileFileType]): file type of the download
        file_name (Union[Unset, str]): file name of the download
        file (Union[Unset, str]): base64 string of the download
    """

    file_type: Union[Unset, DownloadFileFileType] = UNSET
    file_name: Union[Unset, str] = UNSET
    file: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        file_type: Union[Unset, str] = UNSET
        if not isinstance(self.file_type, Unset):
            file_type = self.file_type.value

        file_name = self.file_name

        file = self.file

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_type is not UNSET:
            field_dict["fileType"] = file_type
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if file is not UNSET:
            field_dict["file"] = file

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _file_type = d.pop("fileType", UNSET)
        file_type: Union[Unset, DownloadFileFileType]
        if isinstance(_file_type, Unset) or not _file_type:
            file_type = UNSET
        else:
            file_type = DownloadFileFileType(_file_type)

        file_name = d.pop("fileName", UNSET)

        file = d.pop("file", UNSET)

        download_file = cls(
            file_type=file_type,
            file_name=file_name,
            file=file,
        )

        download_file.additional_properties = d
        return download_file

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
