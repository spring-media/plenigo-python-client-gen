import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.subscription_item_status import SubscriptionItemStatus
from ..models.tax_type import TaxType
from ..models.user_type import UserType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriptionItem")


@_attrs_define
class SubscriptionItem:
    """
    Attributes:
        subscription_item_id (int): unique id of the subscription item in the context of a company
        product_id (str): id of the product bought
        title (str): product title presented to the customer
        price (float): price of the subscription
        discount_percentage (int): discount offered to the subscription
        quantity (int): quantity of purchased entities
        created_date (Union[None, Unset, datetime.datetime]): time the object was created with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        changed_date (Union[None, Unset, datetime.datetime]): time the object was changed with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        created_by (Union[Unset, str]): id who created the object
        created_by_type (Union[Unset, UserType]): type of user who performs the action
        changed_by (Union[Unset, str]): id who changed the object
        changed_by_type (Union[Unset, UserType]): type of user who performs the action
        plenigo_product_id (Union[Unset, str]): if the product is based on a plenigo offer the plenigo product id is
            provided here - can be identically to the productId
        plenigo_step_id (Union[Unset, str]): if the product is based on a plenigo offer the plenigo step id is provided
            here
        access_right_unique_id (Union[Unset, str]): unique id of the access right this subscription item grants access
            to
        internal_title (Union[Unset, str]): if the product is based on a plenigo offer the product title for internal
            usage is provided here
        tax_type (Union[Unset, TaxType]): unique identification of the tax type the product represents
        package_title (Union[Unset, str]): if subscription item is correlated to another subscription item in a way that
            both items are presented as one (bundle) this field contains the correlation title
        package_id (Union[Unset, str]): if subscription item is correlated to another subscription item in a way that
            both items are presented as one (bundle) this field contains the correlation id - the id is only unique within a
            subscription
        package_cancellation_locked (Union[Unset, bool]): flag indicating if package elements can only be cancelled
            together
        price_issue_id (Union[Unset, int]): id of the price issue the subscription item's price is based on
        credit_count (Union[Unset, int]): available credit count to use
        credit_wallet_unique_id (Union[Unset, str]): the credit wallet unique id
        status (Union[Unset, SubscriptionItemStatus]): current status of the subscription item
        cost_center (Union[Unset, str]): cost center associated with this subscription item
        purchase_number (Union[Unset, str]): purchase number associated with this subscription item
    """

    subscription_item_id: int
    product_id: str
    title: str
    price: float
    discount_percentage: int
    quantity: int
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_by_type: Union[Unset, UserType] = UNSET
    changed_by: Union[Unset, str] = UNSET
    changed_by_type: Union[Unset, UserType] = UNSET
    plenigo_product_id: Union[Unset, str] = UNSET
    plenigo_step_id: Union[Unset, str] = UNSET
    access_right_unique_id: Union[Unset, str] = UNSET
    internal_title: Union[Unset, str] = UNSET
    tax_type: Union[Unset, TaxType] = UNSET
    package_title: Union[Unset, str] = UNSET
    package_id: Union[Unset, str] = UNSET
    package_cancellation_locked: Union[Unset, bool] = UNSET
    price_issue_id: Union[Unset, int] = UNSET
    credit_count: Union[Unset, int] = UNSET
    credit_wallet_unique_id: Union[Unset, str] = UNSET
    status: Union[Unset, SubscriptionItemStatus] = UNSET
    cost_center: Union[Unset, str] = UNSET
    purchase_number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subscription_item_id = self.subscription_item_id

        product_id = self.product_id

        title = self.title

        price = self.price

        discount_percentage = self.discount_percentage

        quantity = self.quantity

        created_date: Union[None, Unset, str]
        if isinstance(self.created_date, Unset) or self.created_date is None:
            created_date = UNSET
        elif isinstance(self.created_date, datetime.datetime):
            created_date = self.created_date.isoformat()
        else:
            created_date = self.created_date

        changed_date: Union[None, Unset, str]
        if isinstance(self.changed_date, Unset) or self.changed_date is None:
            changed_date = UNSET
        elif isinstance(self.changed_date, datetime.datetime):
            changed_date = self.changed_date.isoformat()
        else:
            changed_date = self.changed_date

        created_by = self.created_by

        created_by_type: Union[Unset, str] = UNSET
        if not isinstance(self.created_by_type, Unset):
            created_by_type = self.created_by_type.value

        changed_by = self.changed_by

        changed_by_type: Union[Unset, str] = UNSET
        if not isinstance(self.changed_by_type, Unset):
            changed_by_type = self.changed_by_type.value

        plenigo_product_id = self.plenigo_product_id

        plenigo_step_id = self.plenigo_step_id

        access_right_unique_id = self.access_right_unique_id

        internal_title = self.internal_title

        tax_type: Union[Unset, str] = UNSET
        if not isinstance(self.tax_type, Unset):
            tax_type = self.tax_type.value

        package_title = self.package_title

        package_id = self.package_id

        package_cancellation_locked = self.package_cancellation_locked

        price_issue_id = self.price_issue_id

        credit_count = self.credit_count

        credit_wallet_unique_id = self.credit_wallet_unique_id

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        cost_center = self.cost_center

        purchase_number = self.purchase_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subscriptionItemId": subscription_item_id,
                "productId": product_id,
                "title": title,
                "price": price,
                "discountPercentage": discount_percentage,
                "quantity": quantity,
            }
        )
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_by_type is not UNSET:
            field_dict["createdByType"] = created_by_type
        if changed_by is not UNSET:
            field_dict["changedBy"] = changed_by
        if changed_by_type is not UNSET:
            field_dict["changedByType"] = changed_by_type
        if plenigo_product_id is not UNSET:
            field_dict["plenigoProductId"] = plenigo_product_id
        if plenigo_step_id is not UNSET:
            field_dict["plenigoStepId"] = plenigo_step_id
        if access_right_unique_id is not UNSET:
            field_dict["accessRightUniqueId"] = access_right_unique_id
        if internal_title is not UNSET:
            field_dict["internalTitle"] = internal_title
        if tax_type is not UNSET:
            field_dict["taxType"] = tax_type
        if package_title is not UNSET:
            field_dict["packageTitle"] = package_title
        if package_id is not UNSET:
            field_dict["packageId"] = package_id
        if package_cancellation_locked is not UNSET:
            field_dict["packageCancellationLocked"] = package_cancellation_locked
        if price_issue_id is not UNSET:
            field_dict["priceIssueId"] = price_issue_id
        if credit_count is not UNSET:
            field_dict["creditCount"] = credit_count
        if credit_wallet_unique_id is not UNSET:
            field_dict["creditWalletUniqueId"] = credit_wallet_unique_id
        if status is not UNSET:
            field_dict["status"] = status
        if cost_center is not UNSET:
            field_dict["costCenter"] = cost_center
        if purchase_number is not UNSET:
            field_dict["purchaseNumber"] = purchase_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subscription_item_id = d.pop("subscriptionItemId")

        product_id = d.pop("productId")

        title = d.pop("title")

        price = d.pop("price")

        discount_percentage = d.pop("discountPercentage")

        quantity = d.pop("quantity")

        def _parse_created_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data

            if data is None:
                return data

            if isinstance(data, Unset):
                return data

            # Try to parse the data as datetime.datetime
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_date_type_0 = isoparse(data)

                return created_date_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        created_date = _parse_created_date(d.pop("createdDate", UNSET))

        def _parse_changed_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data

            if data is None:
                return data

            if isinstance(data, Unset):
                return data

            # Try to parse the data as datetime.datetime
            try:
                if not isinstance(data, str):
                    raise TypeError()
                changed_date_type_0 = isoparse(data)

                return changed_date_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        changed_date = _parse_changed_date(d.pop("changedDate", UNSET))

        created_by = d.pop("createdBy", UNSET)

        _created_by_type = d.pop("createdByType", UNSET)
        created_by_type: Union[Unset, UserType]
        if isinstance(_created_by_type, Unset) or not _created_by_type:
            created_by_type = UNSET
        else:
            created_by_type = UserType(_created_by_type)

        changed_by = d.pop("changedBy", UNSET)

        _changed_by_type = d.pop("changedByType", UNSET)
        changed_by_type: Union[Unset, UserType]
        if isinstance(_changed_by_type, Unset) or not _changed_by_type:
            changed_by_type = UNSET
        else:
            changed_by_type = UserType(_changed_by_type)

        plenigo_product_id = d.pop("plenigoProductId", UNSET)

        plenigo_step_id = d.pop("plenigoStepId", UNSET)

        access_right_unique_id = d.pop("accessRightUniqueId", UNSET)

        internal_title = d.pop("internalTitle", UNSET)

        _tax_type = d.pop("taxType", UNSET)
        tax_type: Union[Unset, TaxType]
        if isinstance(_tax_type, Unset) or not _tax_type:
            tax_type = UNSET
        else:
            tax_type = TaxType(_tax_type)

        package_title = d.pop("packageTitle", UNSET)

        package_id = d.pop("packageId", UNSET)

        package_cancellation_locked = d.pop("packageCancellationLocked", UNSET)

        price_issue_id = d.pop("priceIssueId", UNSET)

        credit_count = d.pop("creditCount", UNSET)

        credit_wallet_unique_id = d.pop("creditWalletUniqueId", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, SubscriptionItemStatus]
        if isinstance(_status, Unset) or not _status:
            status = UNSET
        else:
            status = SubscriptionItemStatus(_status)

        cost_center = d.pop("costCenter", UNSET)

        purchase_number = d.pop("purchaseNumber", UNSET)

        subscription_item = cls(
            subscription_item_id=subscription_item_id,
            product_id=product_id,
            title=title,
            price=price,
            discount_percentage=discount_percentage,
            quantity=quantity,
            created_date=created_date,
            changed_date=changed_date,
            created_by=created_by,
            created_by_type=created_by_type,
            changed_by=changed_by,
            changed_by_type=changed_by_type,
            plenigo_product_id=plenigo_product_id,
            plenigo_step_id=plenigo_step_id,
            access_right_unique_id=access_right_unique_id,
            internal_title=internal_title,
            tax_type=tax_type,
            package_title=package_title,
            package_id=package_id,
            package_cancellation_locked=package_cancellation_locked,
            price_issue_id=price_issue_id,
            credit_count=credit_count,
            credit_wallet_unique_id=credit_wallet_unique_id,
            status=status,
            cost_center=cost_center,
            purchase_number=purchase_number,
        )

        subscription_item.additional_properties = d
        return subscription_item

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
