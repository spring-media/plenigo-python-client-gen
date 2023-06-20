from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Utm")


@attr.s(auto_attribs=True)
class Utm:
    """
    Attributes:
        source (Union[Unset, str]): identify the source of the traffic
        medium (Union[Unset, str]): identify the medium the link was used on
        campaign (Union[Unset, str]): identify a strategic campaign (e.g. product launch, new feature, partnership,
            etc.) or specific promotion (e.g. a sale, a giveaway, etc.)
        term (Union[Unset, str]): suggested for paid search to identify keywords for your ad
        content (Union[Unset, str]): suggested for additional details for A/B testing and content-targeted ads
    """

    source: Union[Unset, str] = UNSET
    medium: Union[Unset, str] = UNSET
    campaign: Union[Unset, str] = UNSET
    term: Union[Unset, str] = UNSET
    content: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source = self.source
        medium = self.medium
        campaign = self.campaign
        term = self.term
        content = self.content

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source is not UNSET:
            field_dict["source"] = source
        if medium is not UNSET:
            field_dict["medium"] = medium
        if campaign is not UNSET:
            field_dict["campaign"] = campaign
        if term is not UNSET:
            field_dict["term"] = term
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        source = d.pop("source", UNSET)

        medium = d.pop("medium", UNSET)

        campaign = d.pop("campaign", UNSET)

        term = d.pop("term", UNSET)

        content = d.pop("content", UNSET)

        utm = cls(
            source=source,
            medium=medium,
            campaign=campaign,
            term=term,
            content=content,
        )

        utm.additional_properties = d
        return utm

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
