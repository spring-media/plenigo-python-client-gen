from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.cross_selling_access_start import CrossSellingAccessStart
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cross_selling_translation import CrossSellingTranslation
    from ..models.product_tag_creation import ProductTagCreation


T = TypeVar("T", bound="CrossSelling")


@attr.s(auto_attribs=True)
class CrossSelling:
    """
    Attributes:
        cross_selling_id (int): unique id of the cross selling within a contract company
        internal_title (str): internal title
        translations (List['CrossSellingTranslation']): translations associated with this cross selling
        source_product_tags (List['ProductTagCreation']): tags associated as source for this cross selling
        target_product_tags (List['ProductTagCreation']): tags associated as target for this cross selling
        description (Union[Unset, str]): internal description of the cross selling
        access_start (Union[Unset, CrossSellingAccessStart]): indicates when the access to the new product should start
        optional (Union[Unset, bool]): flag indicating if cross selling can be skipped
    """

    cross_selling_id: int
    internal_title: str
    translations: List["CrossSellingTranslation"]
    source_product_tags: List["ProductTagCreation"]
    target_product_tags: List["ProductTagCreation"]
    description: Union[Unset, str] = UNSET
    access_start: Union[Unset, CrossSellingAccessStart] = UNSET
    optional: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cross_selling_id = self.cross_selling_id
        internal_title = self.internal_title
        translations = []
        for translations_item_data in self.translations:
            translations_item = translations_item_data.to_dict()

            translations.append(translations_item)

        source_product_tags = []
        for source_product_tags_item_data in self.source_product_tags:
            source_product_tags_item = source_product_tags_item_data.to_dict()

            source_product_tags.append(source_product_tags_item)

        target_product_tags = []
        for target_product_tags_item_data in self.target_product_tags:
            target_product_tags_item = target_product_tags_item_data.to_dict()

            target_product_tags.append(target_product_tags_item)

        description = self.description
        access_start: Union[Unset, str] = UNSET
        if not isinstance(self.access_start, Unset):
            access_start = self.access_start.value

        optional = self.optional

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "crossSellingId": cross_selling_id,
                "internalTitle": internal_title,
                "translations": translations,
                "sourceProductTags": source_product_tags,
                "targetProductTags": target_product_tags,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if access_start is not UNSET:
            field_dict["accessStart"] = access_start
        if optional is not UNSET:
            field_dict["optional"] = optional

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cross_selling_translation import CrossSellingTranslation
        from ..models.product_tag_creation import ProductTagCreation

        d = src_dict.copy()
        cross_selling_id = d.pop("crossSellingId")

        internal_title = d.pop("internalTitle")

        translations = []
        _translations = d.pop("translations")
        for translations_item_data in _translations:
            translations_item = CrossSellingTranslation.from_dict(translations_item_data)

            translations.append(translations_item)

        source_product_tags = []
        _source_product_tags = d.pop("sourceProductTags")
        for source_product_tags_item_data in _source_product_tags:
            source_product_tags_item = ProductTagCreation.from_dict(source_product_tags_item_data)

            source_product_tags.append(source_product_tags_item)

        target_product_tags = []
        _target_product_tags = d.pop("targetProductTags")
        for target_product_tags_item_data in _target_product_tags:
            target_product_tags_item = ProductTagCreation.from_dict(target_product_tags_item_data)

            target_product_tags.append(target_product_tags_item)

        description = d.pop("description", UNSET)

        _access_start = d.pop("accessStart", UNSET)
        access_start: Union[Unset, CrossSellingAccessStart]
        if isinstance(_access_start, Unset):
            access_start = UNSET
        else:
            access_start = CrossSellingAccessStart(_access_start)

        optional = d.pop("optional", UNSET)

        cross_selling = cls(
            cross_selling_id=cross_selling_id,
            internal_title=internal_title,
            translations=translations,
            source_product_tags=source_product_tags,
            target_product_tags=target_product_tags,
            description=description,
            access_start=access_start,
            optional=optional,
        )

        cross_selling.additional_properties = d
        return cross_selling

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
