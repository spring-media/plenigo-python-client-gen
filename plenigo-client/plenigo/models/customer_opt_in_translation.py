from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomerOptInTranslation")


@attr.s(auto_attribs=True)
class CustomerOptInTranslation:
    """
    Attributes:
        language (str): two letter language code according to <a
            href="https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes" target="_blank">ISO 639-1</a> - every language code
            can only be used once per translation
        sso_text (str): text shown during log in, registration, etc.
        checkout_text (str): text shown during checkout
        preferred (Union[Unset, bool]): flag indicating if language is preferred
    """

    language: str
    sso_text: str
    checkout_text: str
    preferred: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        language = self.language
        sso_text = self.sso_text
        checkout_text = self.checkout_text
        preferred = self.preferred

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "language": language,
                "ssoText": sso_text,
                "checkoutText": checkout_text,
            }
        )
        if preferred is not UNSET:
            field_dict["preferred"] = preferred

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        language = d.pop("language")

        sso_text = d.pop("ssoText")

        checkout_text = d.pop("checkoutText")

        preferred = d.pop("preferred", UNSET)

        customer_opt_in_translation = cls(
            language=language,
            sso_text=sso_text,
            checkout_text=checkout_text,
            preferred=preferred,
        )

        customer_opt_in_translation.additional_properties = d
        return customer_opt_in_translation

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
