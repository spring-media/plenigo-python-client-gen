from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.next_step_next_step import NextStepNextStep
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.next_step_additional_information import NextStepAdditionalInformation


T = TypeVar("T", bound="NextStep")


@_attrs_define
class NextStep:
    """
    Attributes:
        token (str): The token to validate the step.
        company_id (str): Id of the company the process is running for.
        next_step (Union[Unset, NextStepNextStep]): The next step the process should go to.
        two_factor_bar_code_image (Union[Unset, str]): base64 encoded bar code image to show to the user if step is two
            factor verification
        verification_token (Union[Unset, str]): verification token sent to user via email if next step requires a
            verification
        additional_information (Union[Unset, NextStepAdditionalInformation]): additional information depending on the
            next step
    """

    token: str
    company_id: str
    next_step: Union[Unset, NextStepNextStep] = UNSET
    two_factor_bar_code_image: Union[Unset, str] = UNSET
    verification_token: Union[Unset, str] = UNSET
    additional_information: Union[Unset, "NextStepAdditionalInformation"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token = self.token

        company_id = self.company_id

        next_step: Union[Unset, str] = UNSET
        if not isinstance(self.next_step, Unset):
            next_step = self.next_step.value

        two_factor_bar_code_image = self.two_factor_bar_code_image

        verification_token = self.verification_token

        additional_information: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.additional_information, Unset):
            additional_information = self.additional_information.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
                "companyId": company_id,
            }
        )
        if next_step is not UNSET:
            field_dict["nextStep"] = next_step
        if two_factor_bar_code_image is not UNSET:
            field_dict["twoFactorBarCodeImage"] = two_factor_bar_code_image
        if verification_token is not UNSET:
            field_dict["verificationToken"] = verification_token
        if additional_information is not UNSET:
            field_dict["additionalInformation"] = additional_information

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.next_step_additional_information import NextStepAdditionalInformation

        d = src_dict.copy()
        token = d.pop("token")

        company_id = d.pop("companyId")

        _next_step = d.pop("nextStep", UNSET)
        next_step: Union[Unset, NextStepNextStep]
        if isinstance(_next_step, Unset):
            next_step = UNSET
        else:
            next_step = NextStepNextStep(_next_step)

        two_factor_bar_code_image = d.pop("twoFactorBarCodeImage", UNSET)

        verification_token = d.pop("verificationToken", UNSET)

        _additional_information = d.pop("additionalInformation", UNSET)
        additional_information: Union[Unset, NextStepAdditionalInformation]
        if isinstance(_additional_information, Unset):
            additional_information = UNSET
        else:
            additional_information = NextStepAdditionalInformation.from_dict(_additional_information)

        next_step = cls(
            token=token,
            company_id=company_id,
            next_step=next_step,
            two_factor_bar_code_image=two_factor_bar_code_image,
            verification_token=verification_token,
            additional_information=additional_information,
        )

        next_step.additional_properties = d
        return next_step

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
