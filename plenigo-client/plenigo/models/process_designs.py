from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessDesigns")


@_attrs_define
class ProcessDesigns:
    """
    Attributes:
        checkout_logo (Union[Unset, str]): logo to show in the iframe
        background_color (Union[Unset, str]): background color for the iframe
        first_color (Union[Unset, str]): first color for the iframe
        second_color (Union[Unset, str]): second color for the iframe
        font (Union[Unset, str]): font for the iframe
        font_color (Union[Unset, str]): font color for the iframe
        link_color (Union[Unset, str]): link color for the iframe
        checkout_css (Union[Unset, str]): checkout css for the iframe
        checkout_java_script (Union[Unset, str]): checkout JavaScript for the iframe
    """

    checkout_logo: Union[Unset, str] = UNSET
    background_color: Union[Unset, str] = UNSET
    first_color: Union[Unset, str] = UNSET
    second_color: Union[Unset, str] = UNSET
    font: Union[Unset, str] = UNSET
    font_color: Union[Unset, str] = UNSET
    link_color: Union[Unset, str] = UNSET
    checkout_css: Union[Unset, str] = UNSET
    checkout_java_script: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        checkout_logo = self.checkout_logo

        background_color = self.background_color

        first_color = self.first_color

        second_color = self.second_color

        font = self.font

        font_color = self.font_color

        link_color = self.link_color

        checkout_css = self.checkout_css

        checkout_java_script = self.checkout_java_script

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if checkout_logo is not UNSET:
            field_dict["checkoutLogo"] = checkout_logo
        if background_color is not UNSET:
            field_dict["backgroundColor"] = background_color
        if first_color is not UNSET:
            field_dict["firstColor"] = first_color
        if second_color is not UNSET:
            field_dict["secondColor"] = second_color
        if font is not UNSET:
            field_dict["font"] = font
        if font_color is not UNSET:
            field_dict["fontColor"] = font_color
        if link_color is not UNSET:
            field_dict["linkColor"] = link_color
        if checkout_css is not UNSET:
            field_dict["checkoutCss"] = checkout_css
        if checkout_java_script is not UNSET:
            field_dict["checkoutJavaScript"] = checkout_java_script

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        checkout_logo = d.pop("checkoutLogo", UNSET)

        background_color = d.pop("backgroundColor", UNSET)

        first_color = d.pop("firstColor", UNSET)

        second_color = d.pop("secondColor", UNSET)

        font = d.pop("font", UNSET)

        font_color = d.pop("fontColor", UNSET)

        link_color = d.pop("linkColor", UNSET)

        checkout_css = d.pop("checkoutCss", UNSET)

        checkout_java_script = d.pop("checkoutJavaScript", UNSET)

        process_designs = cls(
            checkout_logo=checkout_logo,
            background_color=background_color,
            first_color=first_color,
            second_color=second_color,
            font=font,
            font_color=font_color,
            link_color=link_color,
            checkout_css=checkout_css,
            checkout_java_script=checkout_java_script,
        )

        process_designs.additional_properties = d
        return process_designs

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
