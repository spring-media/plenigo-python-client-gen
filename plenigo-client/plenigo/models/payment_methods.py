from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amazon_pay_account import AmazonPayAccount
    from ..models.bank_accounts import BankAccounts
    from ..models.credit_cards import CreditCards
    from ..models.i_deal_accounts import IDealAccounts
    from ..models.pay_pal_accounts import PayPalAccounts


T = TypeVar("T", bound="PaymentMethods")


@_attrs_define
class PaymentMethods:
    """
    Attributes:
        amazon_pay_accounts (Union[Unset, List['AmazonPayAccount']]):
        bank_accounts (Union[Unset, List['BankAccounts']]):
        credit_cards (Union[Unset, List['CreditCards']]):
        pay_pal_accounts (Union[Unset, List['PayPalAccounts']]):
        i_deal_accounts (Union[Unset, List['IDealAccounts']]):
    """

    amazon_pay_accounts: Union[Unset, List["AmazonPayAccount"]] = UNSET
    bank_accounts: Union[Unset, List["BankAccounts"]] = UNSET
    credit_cards: Union[Unset, List["CreditCards"]] = UNSET
    pay_pal_accounts: Union[Unset, List["PayPalAccounts"]] = UNSET
    i_deal_accounts: Union[Unset, List["IDealAccounts"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amazon_pay_accounts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.amazon_pay_accounts, Unset):
            amazon_pay_accounts = []
            for amazon_pay_accounts_item_data in self.amazon_pay_accounts:
                amazon_pay_accounts_item = amazon_pay_accounts_item_data.to_dict()
                amazon_pay_accounts.append(amazon_pay_accounts_item)

        bank_accounts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.bank_accounts, Unset):
            bank_accounts = []
            for bank_accounts_item_data in self.bank_accounts:
                bank_accounts_item = bank_accounts_item_data.to_dict()
                bank_accounts.append(bank_accounts_item)

        credit_cards: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.credit_cards, Unset):
            credit_cards = []
            for credit_cards_item_data in self.credit_cards:
                credit_cards_item = credit_cards_item_data.to_dict()
                credit_cards.append(credit_cards_item)

        pay_pal_accounts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.pay_pal_accounts, Unset):
            pay_pal_accounts = []
            for pay_pal_accounts_item_data in self.pay_pal_accounts:
                pay_pal_accounts_item = pay_pal_accounts_item_data.to_dict()
                pay_pal_accounts.append(pay_pal_accounts_item)

        i_deal_accounts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.i_deal_accounts, Unset):
            i_deal_accounts = []
            for i_deal_accounts_item_data in self.i_deal_accounts:
                i_deal_accounts_item = i_deal_accounts_item_data.to_dict()
                i_deal_accounts.append(i_deal_accounts_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amazon_pay_accounts is not UNSET:
            field_dict["amazonPayAccounts"] = amazon_pay_accounts
        if bank_accounts is not UNSET:
            field_dict["bankAccounts"] = bank_accounts
        if credit_cards is not UNSET:
            field_dict["creditCards"] = credit_cards
        if pay_pal_accounts is not UNSET:
            field_dict["payPalAccounts"] = pay_pal_accounts
        if i_deal_accounts is not UNSET:
            field_dict["iDealAccounts"] = i_deal_accounts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.amazon_pay_account import AmazonPayAccount
        from ..models.bank_accounts import BankAccounts
        from ..models.credit_cards import CreditCards
        from ..models.i_deal_accounts import IDealAccounts
        from ..models.pay_pal_accounts import PayPalAccounts

        d = src_dict.copy()
        amazon_pay_accounts = []
        _amazon_pay_accounts = d.pop("amazonPayAccounts", UNSET)
        for amazon_pay_accounts_item_data in _amazon_pay_accounts or []:
            amazon_pay_accounts_item = AmazonPayAccount.from_dict(amazon_pay_accounts_item_data)

            amazon_pay_accounts.append(amazon_pay_accounts_item)

        bank_accounts = []
        _bank_accounts = d.pop("bankAccounts", UNSET)
        for bank_accounts_item_data in _bank_accounts or []:
            bank_accounts_item = BankAccounts.from_dict(bank_accounts_item_data)

            bank_accounts.append(bank_accounts_item)

        credit_cards = []
        _credit_cards = d.pop("creditCards", UNSET)
        for credit_cards_item_data in _credit_cards or []:
            credit_cards_item = CreditCards.from_dict(credit_cards_item_data)

            credit_cards.append(credit_cards_item)

        pay_pal_accounts = []
        _pay_pal_accounts = d.pop("payPalAccounts", UNSET)
        for pay_pal_accounts_item_data in _pay_pal_accounts or []:
            pay_pal_accounts_item = PayPalAccounts.from_dict(pay_pal_accounts_item_data)

            pay_pal_accounts.append(pay_pal_accounts_item)

        i_deal_accounts = []
        _i_deal_accounts = d.pop("iDealAccounts", UNSET)
        for i_deal_accounts_item_data in _i_deal_accounts or []:
            i_deal_accounts_item = IDealAccounts.from_dict(i_deal_accounts_item_data)

            i_deal_accounts.append(i_deal_accounts_item)

        payment_methods = cls(
            amazon_pay_accounts=amazon_pay_accounts,
            bank_accounts=bank_accounts,
            credit_cards=credit_cards,
            pay_pal_accounts=pay_pal_accounts,
            i_deal_accounts=i_deal_accounts,
        )

        payment_methods.additional_properties = d
        return payment_methods

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
