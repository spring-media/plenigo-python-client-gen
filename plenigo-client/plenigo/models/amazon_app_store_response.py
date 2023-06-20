from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AmazonAppStoreResponse")


@attr.s(auto_attribs=True)
class AmazonAppStoreResponse:
    """
    Attributes:
        receipt_id (Union[Unset, str]): unique identifier for the purchase
        product_type (Union[Unset, str]): type of product purchased - valid product types are CONSUMABLE, SUBSCRIPTION,
            and ENTITLED
        product_id (Union[Unset, str]): SKU that you defined for this item in your app
        purchase_date (Union[Unset, int]): date of the purchase, stored as the number of milliseconds since the epoch
        renewal_date (Union[Unset, int]): date that a subscription purchase needs to be renewed
        cancel_date (Union[Unset, int]): date the purchase was cancelled, or the subscription expired
        test_transaction (Union[Unset, bool]): indicates whether this purchase was made as a part of Amazon’s publishing
            and testing process
        beta_product (Union[Unset, bool]): indicates whether the product purchased is a Live App Testing product
        parent_product_id (Union[Unset, str]): reserved for future use
        quantity (Union[Unset, int]): quantity purchased
        term (Union[Unset, str]): duration that a subscription IAP will remain valid (the term starts on the date of
            purchase)
        term_sku (Union[Unset, str]): unique SKU that corresponds to the subscription term
    """

    receipt_id: Union[Unset, str] = UNSET
    product_type: Union[Unset, str] = UNSET
    product_id: Union[Unset, str] = UNSET
    purchase_date: Union[Unset, int] = UNSET
    renewal_date: Union[Unset, int] = UNSET
    cancel_date: Union[Unset, int] = UNSET
    test_transaction: Union[Unset, bool] = UNSET
    beta_product: Union[Unset, bool] = UNSET
    parent_product_id: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    term: Union[Unset, str] = UNSET
    term_sku: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        receipt_id = self.receipt_id
        product_type = self.product_type
        product_id = self.product_id
        purchase_date = self.purchase_date
        renewal_date = self.renewal_date
        cancel_date = self.cancel_date
        test_transaction = self.test_transaction
        beta_product = self.beta_product
        parent_product_id = self.parent_product_id
        quantity = self.quantity
        term = self.term
        term_sku = self.term_sku

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if receipt_id is not UNSET:
            field_dict["receiptID"] = receipt_id
        if product_type is not UNSET:
            field_dict["productType"] = product_type
        if product_id is not UNSET:
            field_dict["productID"] = product_id
        if purchase_date is not UNSET:
            field_dict["purchaseDate"] = purchase_date
        if renewal_date is not UNSET:
            field_dict["renewalDate"] = renewal_date
        if cancel_date is not UNSET:
            field_dict["cancelDate"] = cancel_date
        if test_transaction is not UNSET:
            field_dict["testTransaction"] = test_transaction
        if beta_product is not UNSET:
            field_dict["betaProduct"] = beta_product
        if parent_product_id is not UNSET:
            field_dict["parentProductID"] = parent_product_id
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if term is not UNSET:
            field_dict["term"] = term
        if term_sku is not UNSET:
            field_dict["termSku"] = term_sku

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        receipt_id = d.pop("receiptID", UNSET)

        product_type = d.pop("productType", UNSET)

        product_id = d.pop("productID", UNSET)

        purchase_date = d.pop("purchaseDate", UNSET)

        renewal_date = d.pop("renewalDate", UNSET)

        cancel_date = d.pop("cancelDate", UNSET)

        test_transaction = d.pop("testTransaction", UNSET)

        beta_product = d.pop("betaProduct", UNSET)

        parent_product_id = d.pop("parentProductID", UNSET)

        quantity = d.pop("quantity", UNSET)

        term = d.pop("term", UNSET)

        term_sku = d.pop("termSku", UNSET)

        amazon_app_store_response = cls(
            receipt_id=receipt_id,
            product_type=product_type,
            product_id=product_id,
            purchase_date=purchase_date,
            renewal_date=renewal_date,
            cancel_date=cancel_date,
            test_transaction=test_transaction,
            beta_product=beta_product,
            parent_product_id=parent_product_id,
            quantity=quantity,
            term=term,
            term_sku=term_sku,
        )

        amazon_app_store_response.additional_properties = d
        return amazon_app_store_response

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
