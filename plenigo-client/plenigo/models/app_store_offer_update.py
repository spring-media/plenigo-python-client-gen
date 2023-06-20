from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppStoreOfferUpdate")


@attr.s(auto_attribs=True)
class AppStoreOfferUpdate:
    """
    Attributes:
        internal_title (str): internal title of the app store offer
        product_id (str): unique id of the product as defined by the app store in use - the kind of product is not
            important (subscription vs. purchase)
        access_right_id (int): id of the access right associated with this offer
        description (Union[Unset, str]): description of the app store offer
        fallback (Union[Unset, bool]): flag indicating if product should be used as fallback if no offer for a given
            product id can be found
    """

    internal_title: str
    product_id: str
    access_right_id: int
    description: Union[Unset, str] = UNSET
    fallback: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        internal_title = self.internal_title
        product_id = self.product_id
        access_right_id = self.access_right_id
        description = self.description
        fallback = self.fallback

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "internalTitle": internal_title,
                "productId": product_id,
                "accessRightId": access_right_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if fallback is not UNSET:
            field_dict["fallback"] = fallback

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        internal_title = d.pop("internalTitle")

        product_id = d.pop("productId")

        access_right_id = d.pop("accessRightId")

        description = d.pop("description", UNSET)

        fallback = d.pop("fallback", UNSET)

        app_store_offer_update = cls(
            internal_title=internal_title,
            product_id=product_id,
            access_right_id=access_right_id,
            description=description,
            fallback=fallback,
        )

        app_store_offer_update.additional_properties = d
        return app_store_offer_update

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
