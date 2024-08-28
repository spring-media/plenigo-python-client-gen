from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.logging_data import LoggingData
    from ..models.step_token import StepToken


T = TypeVar("T", bound="CustomerData")


@_attrs_define
class CustomerData:
    """
    Attributes:
        step_token (Union[Unset, StepToken]):
        username (Union[Unset, str]): username of the new customer
        first_name (Union[Unset, str]): first name of the new customer
        last_name (Union[Unset, str]): last name of the new customer
        logging_data (Union[Unset, LoggingData]):
    """

    step_token: Union[Unset, "StepToken"] = UNSET
    username: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    logging_data: Union[Unset, "LoggingData"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        step_token: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.step_token, Unset):
            step_token = self.step_token.to_dict()

        username = self.username

        first_name = self.first_name

        last_name = self.last_name

        logging_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.logging_data, Unset):
            logging_data = self.logging_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if step_token is not UNSET:
            field_dict["stepToken"] = step_token
        if username is not UNSET:
            field_dict["username"] = username
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if logging_data is not UNSET:
            field_dict["loggingData"] = logging_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.logging_data import LoggingData
        from ..models.step_token import StepToken

        d = src_dict.copy()
        _step_token = d.pop("stepToken", UNSET)
        step_token: Union[Unset, StepToken]
        if isinstance(_step_token, Unset) or not _step_token:
            step_token = UNSET
        else:
            step_token = StepToken.from_dict(_step_token)

        username = d.pop("username", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        _logging_data = d.pop("loggingData", UNSET)
        logging_data: Union[Unset, LoggingData]
        if isinstance(_logging_data, Unset) or not _logging_data:
            logging_data = UNSET
        else:
            logging_data = LoggingData.from_dict(_logging_data)

        customer_data = cls(
            step_token=step_token,
            username=username,
            first_name=first_name,
            last_name=last_name,
            logging_data=logging_data,
        )

        customer_data.additional_properties = d
        return customer_data

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
