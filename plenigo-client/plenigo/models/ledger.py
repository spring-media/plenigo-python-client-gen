import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_base_changed_by_type import ApiBaseChangedByType
from ..models.api_base_created_by_type import ApiBaseCreatedByType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ledger_creation_custom_accountings import LedgerCreationCustomAccountings


T = TypeVar("T", bound="Ledger")


@_attrs_define
class Ledger:
    """
    Attributes:
        title (str): Title of the ledger
        ledger_id (int): unique id of the ledger in the context of a company
        description (Union[Unset, str]): description of the ledger
        delivery_commitment_account (Union[Unset, str]): delivery commitment account of the ledger
        voucher_delivery_commitment_account (Union[Unset, str]): voucher delivery commitment account of the ledger
        revenue_account (Union[Unset, str]): revenue account of the ledger
        bank_account_amazon_pay (Union[Unset, str]): bank account for Amazon Pay of the ledger
        bank_account_apple_pay (Union[Unset, str]): bank account for Apple Pay of the ledger
        bank_account_billing (Union[Unset, str]): bank account for billing of the ledger
        bank_account_credit_card (Union[Unset, str]): bank account for credit card of the ledger
        bank_account_google_pay (Union[Unset, str]): bank account for Google Pay of the ledger
        bank_account_pay_pal (Union[Unset, str]): bank account for PayPal of the ledger
        bank_account_sepa (Union[Unset, str]): bank account for sepa of the ledger
        credit_loss_account (Union[Unset, str]): credit loss account of the ledger
        sales_tax (Union[Unset, str]): sales tax account of the ledger
        b_2_b_delivery_commitment_account (Union[Unset, str]): b2b delivery commitment account of the ledger
        b_2_b_voucher_delivery_commitment_account (Union[Unset, str]): b2b voucher delivery commitment account of the
            ledger
        b_2_b_revenue_account (Union[Unset, str]): b2b revenue account of the ledger
        b_2_b_bank_account_amazon_pay (Union[Unset, str]): b2b bank account for Amazon Pay of the ledger
        b_2_b_bank_account_apple_pay (Union[Unset, str]): b2b bank account for Apple Pay of the ledger
        b_2_b_bank_account_billing (Union[Unset, str]): b2b bank account for billing of the ledger
        b_2_b_bank_account_credit_card (Union[Unset, str]): b2b bank account for credit card of the ledger
        b_2_b_bank_account_google_pay (Union[Unset, str]): b2b bank account for Google Pay of the ledger
        b_2_b_bank_account_pay_pal (Union[Unset, str]): b2b bank account for PayPal of the ledger
        b_2_b_bank_account_sepa (Union[Unset, str]): b2b bank account for sepa of the ledger
        b_2_b_credit_loss_account (Union[Unset, str]): b2b credit loss account of the ledger
        b_2_b_sales_tax (Union[Unset, str]): b2b sales tax account of the ledger
        custom_accountings (Union[Unset, LedgerCreationCustomAccountings]): custom accountings of the ledger
        created_date (Union[None, Unset, datetime.datetime]): Time the object was created in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        changed_date (Union[None, Unset, datetime.datetime]): Time the object was changed in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        created_by (Union[Unset, str]): ID of who created the object
        created_by_type (Union[Unset, ApiBaseCreatedByType]): Type of creator
        changed_by (Union[Unset, str]): ID of who changed the object
        changed_by_type (Union[Unset, ApiBaseChangedByType]): Type of changer
    """

    title: str
    ledger_id: int
    description: Union[Unset, str] = UNSET
    delivery_commitment_account: Union[Unset, str] = UNSET
    voucher_delivery_commitment_account: Union[Unset, str] = UNSET
    revenue_account: Union[Unset, str] = UNSET
    bank_account_amazon_pay: Union[Unset, str] = UNSET
    bank_account_apple_pay: Union[Unset, str] = UNSET
    bank_account_billing: Union[Unset, str] = UNSET
    bank_account_credit_card: Union[Unset, str] = UNSET
    bank_account_google_pay: Union[Unset, str] = UNSET
    bank_account_pay_pal: Union[Unset, str] = UNSET
    bank_account_sepa: Union[Unset, str] = UNSET
    credit_loss_account: Union[Unset, str] = UNSET
    sales_tax: Union[Unset, str] = UNSET
    b_2_b_delivery_commitment_account: Union[Unset, str] = UNSET
    b_2_b_voucher_delivery_commitment_account: Union[Unset, str] = UNSET
    b_2_b_revenue_account: Union[Unset, str] = UNSET
    b_2_b_bank_account_amazon_pay: Union[Unset, str] = UNSET
    b_2_b_bank_account_apple_pay: Union[Unset, str] = UNSET
    b_2_b_bank_account_billing: Union[Unset, str] = UNSET
    b_2_b_bank_account_credit_card: Union[Unset, str] = UNSET
    b_2_b_bank_account_google_pay: Union[Unset, str] = UNSET
    b_2_b_bank_account_pay_pal: Union[Unset, str] = UNSET
    b_2_b_bank_account_sepa: Union[Unset, str] = UNSET
    b_2_b_credit_loss_account: Union[Unset, str] = UNSET
    b_2_b_sales_tax: Union[Unset, str] = UNSET
    custom_accountings: Union[Unset, "LedgerCreationCustomAccountings"] = UNSET
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_by_type: Union[Unset, ApiBaseCreatedByType] = UNSET
    changed_by: Union[Unset, str] = UNSET
    changed_by_type: Union[Unset, ApiBaseChangedByType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title

        ledger_id = self.ledger_id

        description = self.description

        delivery_commitment_account = self.delivery_commitment_account

        voucher_delivery_commitment_account = self.voucher_delivery_commitment_account

        revenue_account = self.revenue_account

        bank_account_amazon_pay = self.bank_account_amazon_pay

        bank_account_apple_pay = self.bank_account_apple_pay

        bank_account_billing = self.bank_account_billing

        bank_account_credit_card = self.bank_account_credit_card

        bank_account_google_pay = self.bank_account_google_pay

        bank_account_pay_pal = self.bank_account_pay_pal

        bank_account_sepa = self.bank_account_sepa

        credit_loss_account = self.credit_loss_account

        sales_tax = self.sales_tax

        b_2_b_delivery_commitment_account = self.b_2_b_delivery_commitment_account

        b_2_b_voucher_delivery_commitment_account = self.b_2_b_voucher_delivery_commitment_account

        b_2_b_revenue_account = self.b_2_b_revenue_account

        b_2_b_bank_account_amazon_pay = self.b_2_b_bank_account_amazon_pay

        b_2_b_bank_account_apple_pay = self.b_2_b_bank_account_apple_pay

        b_2_b_bank_account_billing = self.b_2_b_bank_account_billing

        b_2_b_bank_account_credit_card = self.b_2_b_bank_account_credit_card

        b_2_b_bank_account_google_pay = self.b_2_b_bank_account_google_pay

        b_2_b_bank_account_pay_pal = self.b_2_b_bank_account_pay_pal

        b_2_b_bank_account_sepa = self.b_2_b_bank_account_sepa

        b_2_b_credit_loss_account = self.b_2_b_credit_loss_account

        b_2_b_sales_tax = self.b_2_b_sales_tax

        custom_accountings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom_accountings, Unset):
            custom_accountings = self.custom_accountings.to_dict()

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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "ledgerId": ledger_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if delivery_commitment_account is not UNSET:
            field_dict["deliveryCommitmentAccount"] = delivery_commitment_account
        if voucher_delivery_commitment_account is not UNSET:
            field_dict["voucherDeliveryCommitmentAccount"] = voucher_delivery_commitment_account
        if revenue_account is not UNSET:
            field_dict["revenueAccount"] = revenue_account
        if bank_account_amazon_pay is not UNSET:
            field_dict["bankAccountAmazonPay"] = bank_account_amazon_pay
        if bank_account_apple_pay is not UNSET:
            field_dict["bankAccountApplePay"] = bank_account_apple_pay
        if bank_account_billing is not UNSET:
            field_dict["bankAccountBilling"] = bank_account_billing
        if bank_account_credit_card is not UNSET:
            field_dict["bankAccountCreditCard"] = bank_account_credit_card
        if bank_account_google_pay is not UNSET:
            field_dict["bankAccountGooglePay"] = bank_account_google_pay
        if bank_account_pay_pal is not UNSET:
            field_dict["bankAccountPayPal"] = bank_account_pay_pal
        if bank_account_sepa is not UNSET:
            field_dict["bankAccountSepa"] = bank_account_sepa
        if credit_loss_account is not UNSET:
            field_dict["creditLossAccount"] = credit_loss_account
        if sales_tax is not UNSET:
            field_dict["salesTax"] = sales_tax
        if b_2_b_delivery_commitment_account is not UNSET:
            field_dict["b2bDeliveryCommitmentAccount"] = b_2_b_delivery_commitment_account
        if b_2_b_voucher_delivery_commitment_account is not UNSET:
            field_dict["b2bVoucherDeliveryCommitmentAccount"] = b_2_b_voucher_delivery_commitment_account
        if b_2_b_revenue_account is not UNSET:
            field_dict["b2bRevenueAccount"] = b_2_b_revenue_account
        if b_2_b_bank_account_amazon_pay is not UNSET:
            field_dict["b2bBankAccountAmazonPay"] = b_2_b_bank_account_amazon_pay
        if b_2_b_bank_account_apple_pay is not UNSET:
            field_dict["b2bBankAccountApplePay"] = b_2_b_bank_account_apple_pay
        if b_2_b_bank_account_billing is not UNSET:
            field_dict["b2bBankAccountBilling"] = b_2_b_bank_account_billing
        if b_2_b_bank_account_credit_card is not UNSET:
            field_dict["b2bBankAccountCreditCard"] = b_2_b_bank_account_credit_card
        if b_2_b_bank_account_google_pay is not UNSET:
            field_dict["b2bBankAccountGooglePay"] = b_2_b_bank_account_google_pay
        if b_2_b_bank_account_pay_pal is not UNSET:
            field_dict["b2bBankAccountPayPal"] = b_2_b_bank_account_pay_pal
        if b_2_b_bank_account_sepa is not UNSET:
            field_dict["b2bBankAccountSepa"] = b_2_b_bank_account_sepa
        if b_2_b_credit_loss_account is not UNSET:
            field_dict["b2bCreditLossAccount"] = b_2_b_credit_loss_account
        if b_2_b_sales_tax is not UNSET:
            field_dict["b2bSalesTax"] = b_2_b_sales_tax
        if custom_accountings is not UNSET:
            field_dict["customAccountings"] = custom_accountings
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ledger_creation_custom_accountings import LedgerCreationCustomAccountings

        d = src_dict.copy()
        title = d.pop("title")

        ledger_id = d.pop("ledgerId")

        description = d.pop("description", UNSET)

        delivery_commitment_account = d.pop("deliveryCommitmentAccount", UNSET)

        voucher_delivery_commitment_account = d.pop("voucherDeliveryCommitmentAccount", UNSET)

        revenue_account = d.pop("revenueAccount", UNSET)

        bank_account_amazon_pay = d.pop("bankAccountAmazonPay", UNSET)

        bank_account_apple_pay = d.pop("bankAccountApplePay", UNSET)

        bank_account_billing = d.pop("bankAccountBilling", UNSET)

        bank_account_credit_card = d.pop("bankAccountCreditCard", UNSET)

        bank_account_google_pay = d.pop("bankAccountGooglePay", UNSET)

        bank_account_pay_pal = d.pop("bankAccountPayPal", UNSET)

        bank_account_sepa = d.pop("bankAccountSepa", UNSET)

        credit_loss_account = d.pop("creditLossAccount", UNSET)

        sales_tax = d.pop("salesTax", UNSET)

        b_2_b_delivery_commitment_account = d.pop("b2bDeliveryCommitmentAccount", UNSET)

        b_2_b_voucher_delivery_commitment_account = d.pop("b2bVoucherDeliveryCommitmentAccount", UNSET)

        b_2_b_revenue_account = d.pop("b2bRevenueAccount", UNSET)

        b_2_b_bank_account_amazon_pay = d.pop("b2bBankAccountAmazonPay", UNSET)

        b_2_b_bank_account_apple_pay = d.pop("b2bBankAccountApplePay", UNSET)

        b_2_b_bank_account_billing = d.pop("b2bBankAccountBilling", UNSET)

        b_2_b_bank_account_credit_card = d.pop("b2bBankAccountCreditCard", UNSET)

        b_2_b_bank_account_google_pay = d.pop("b2bBankAccountGooglePay", UNSET)

        b_2_b_bank_account_pay_pal = d.pop("b2bBankAccountPayPal", UNSET)

        b_2_b_bank_account_sepa = d.pop("b2bBankAccountSepa", UNSET)

        b_2_b_credit_loss_account = d.pop("b2bCreditLossAccount", UNSET)

        b_2_b_sales_tax = d.pop("b2bSalesTax", UNSET)

        _custom_accountings = d.pop("customAccountings", UNSET)
        custom_accountings: Union[Unset, LedgerCreationCustomAccountings]
        if isinstance(_custom_accountings, Unset) or not _custom_accountings:
            custom_accountings = UNSET
        else:
            custom_accountings = LedgerCreationCustomAccountings.from_dict(_custom_accountings)

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
        created_by_type: Union[Unset, ApiBaseCreatedByType]
        if isinstance(_created_by_type, Unset) or not _created_by_type:
            created_by_type = UNSET
        else:
            created_by_type = ApiBaseCreatedByType(_created_by_type)

        changed_by = d.pop("changedBy", UNSET)

        _changed_by_type = d.pop("changedByType", UNSET)
        changed_by_type: Union[Unset, ApiBaseChangedByType]
        if isinstance(_changed_by_type, Unset) or not _changed_by_type:
            changed_by_type = UNSET
        else:
            changed_by_type = ApiBaseChangedByType(_changed_by_type)

        ledger = cls(
            title=title,
            ledger_id=ledger_id,
            description=description,
            delivery_commitment_account=delivery_commitment_account,
            voucher_delivery_commitment_account=voucher_delivery_commitment_account,
            revenue_account=revenue_account,
            bank_account_amazon_pay=bank_account_amazon_pay,
            bank_account_apple_pay=bank_account_apple_pay,
            bank_account_billing=bank_account_billing,
            bank_account_credit_card=bank_account_credit_card,
            bank_account_google_pay=bank_account_google_pay,
            bank_account_pay_pal=bank_account_pay_pal,
            bank_account_sepa=bank_account_sepa,
            credit_loss_account=credit_loss_account,
            sales_tax=sales_tax,
            b_2_b_delivery_commitment_account=b_2_b_delivery_commitment_account,
            b_2_b_voucher_delivery_commitment_account=b_2_b_voucher_delivery_commitment_account,
            b_2_b_revenue_account=b_2_b_revenue_account,
            b_2_b_bank_account_amazon_pay=b_2_b_bank_account_amazon_pay,
            b_2_b_bank_account_apple_pay=b_2_b_bank_account_apple_pay,
            b_2_b_bank_account_billing=b_2_b_bank_account_billing,
            b_2_b_bank_account_credit_card=b_2_b_bank_account_credit_card,
            b_2_b_bank_account_google_pay=b_2_b_bank_account_google_pay,
            b_2_b_bank_account_pay_pal=b_2_b_bank_account_pay_pal,
            b_2_b_bank_account_sepa=b_2_b_bank_account_sepa,
            b_2_b_credit_loss_account=b_2_b_credit_loss_account,
            b_2_b_sales_tax=b_2_b_sales_tax,
            custom_accountings=custom_accountings,
            created_date=created_date,
            changed_date=changed_date,
            created_by=created_by,
            created_by_type=created_by_type,
            changed_by=changed_by,
            changed_by_type=changed_by_type,
        )

        ledger.additional_properties = d
        return ledger

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
