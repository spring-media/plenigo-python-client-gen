import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.offer_base_allowed_payment_methods_item import OfferBaseAllowedPaymentMethodsItem
from ..models.offer_base_pdf_template_usage import OfferBasePdfTemplateUsage
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.offer_connected_company_settings import OfferConnectedCompanySettings
    from ..models.offer_partner_settings import OfferPartnerSettings
    from ..models.offer_translation import OfferTranslation


T = TypeVar("T", bound="OfferBase")


@attr.s(auto_attribs=True)
class OfferBase:
    """
    Attributes:
        internal_title (str): internal title of the product group
        translations (List['OfferTranslation']): translations associated with this product
        pause_able (Union[Unset, bool]): flag indicating if subscription is pause able
        invoice_address_mandatory (Union[Unset, bool]): flag indicating if invoice address must be provided by the
            customer
        delivery_address_mandatory (Union[Unset, bool]): flag indicating if delivery address must be provided by the
            customer
        multiple_purchases (Union[Unset, bool]): flag indicating if offer can be bought multiple times from the same
            customer
        misuse_rule_id (Union[Unset, int]): id of the misuse rule to apply
        delivery_list_id (Union[Unset, int]): id of the delivery list to use
        fixed_start_date (Union[Unset, None, datetime.date]): fixed date the offer starts with
        issues_in_past (Union[Unset, int]): amount of issues that the user can select in the past - cannot be selected
            with fixed start date
        issues_in_future (Union[Unset, int]): amount of issues that the user can select in the future - cannot be
            selected with fixed start date
        archived (Union[Unset, bool]): flag indicating if offer is archived
        allowed_payment_methods (Union[Unset, List[OfferBaseAllowedPaymentMethodsItem]]): additional constraints to the
            payment methods if some of the selected payment methods cannot be used for this offer - there can be no more
            payment methods than selected in the global payment settings section
        connected_company_settings (Union[Unset, OfferConnectedCompanySettings]):
        leaf_id (Union[Unset, int]): id of the tree leaf this offer should be associated with
        external_billing (Union[Unset, bool]): indicates if payments are handled by plenigo or an external system
        customer_cancellation_blocked (Union[Unset, bool]): indicates if a subscription cannot be cancelled by a
            customer
        corporate_account_users (Union[Unset, int]): count of allowed corporate account users
        corporate_account_invitation_url (Union[Unset, str]): corporate account invitation url
        bonus_id (Union[Unset, int]): id of the bonus associated with this offer
        managed_external (Union[Unset, bool]): flag indicating if offer is managed externally
        pdf_template_usage (Union[Unset, OfferBasePdfTemplateUsage]): contains the pdf template to use with this offer
        partner_settings (Union[Unset, None, OfferPartnerSettings]):
    """

    internal_title: str
    translations: List["OfferTranslation"]
    pause_able: Union[Unset, bool] = UNSET
    invoice_address_mandatory: Union[Unset, bool] = UNSET
    delivery_address_mandatory: Union[Unset, bool] = UNSET
    multiple_purchases: Union[Unset, bool] = UNSET
    misuse_rule_id: Union[Unset, int] = UNSET
    delivery_list_id: Union[Unset, int] = UNSET
    fixed_start_date: Union[Unset, None, datetime.date] = UNSET
    issues_in_past: Union[Unset, int] = UNSET
    issues_in_future: Union[Unset, int] = UNSET
    archived: Union[Unset, bool] = UNSET
    allowed_payment_methods: Union[Unset, List[OfferBaseAllowedPaymentMethodsItem]] = UNSET
    connected_company_settings: Union[Unset, "OfferConnectedCompanySettings"] = UNSET
    leaf_id: Union[Unset, int] = UNSET
    external_billing: Union[Unset, bool] = UNSET
    customer_cancellation_blocked: Union[Unset, bool] = UNSET
    corporate_account_users: Union[Unset, int] = UNSET
    corporate_account_invitation_url: Union[Unset, str] = UNSET
    bonus_id: Union[Unset, int] = UNSET
    managed_external: Union[Unset, bool] = UNSET
    pdf_template_usage: Union[Unset, OfferBasePdfTemplateUsage] = UNSET
    partner_settings: Union[Unset, None, "OfferPartnerSettings"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        internal_title = self.internal_title
        translations = []
        for translations_item_data in self.translations:
            translations_item = translations_item_data.to_dict()

            translations.append(translations_item)

        pause_able = self.pause_able
        invoice_address_mandatory = self.invoice_address_mandatory
        delivery_address_mandatory = self.delivery_address_mandatory
        multiple_purchases = self.multiple_purchases
        misuse_rule_id = self.misuse_rule_id
        delivery_list_id = self.delivery_list_id
        fixed_start_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.fixed_start_date, Unset):
            fixed_start_date = self.fixed_start_date.isoformat() if self.fixed_start_date else None

        issues_in_past = self.issues_in_past
        issues_in_future = self.issues_in_future
        archived = self.archived
        allowed_payment_methods: Union[Unset, List[str]] = UNSET
        if not isinstance(self.allowed_payment_methods, Unset):
            allowed_payment_methods = []
            for allowed_payment_methods_item_data in self.allowed_payment_methods:
                allowed_payment_methods_item = allowed_payment_methods_item_data.value

                allowed_payment_methods.append(allowed_payment_methods_item)

        connected_company_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.connected_company_settings, Unset):
            connected_company_settings = self.connected_company_settings.to_dict()

        leaf_id = self.leaf_id
        external_billing = self.external_billing
        customer_cancellation_blocked = self.customer_cancellation_blocked
        corporate_account_users = self.corporate_account_users
        corporate_account_invitation_url = self.corporate_account_invitation_url
        bonus_id = self.bonus_id
        managed_external = self.managed_external
        pdf_template_usage: Union[Unset, str] = UNSET
        if not isinstance(self.pdf_template_usage, Unset):
            pdf_template_usage = self.pdf_template_usage.value

        partner_settings: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.partner_settings, Unset):
            partner_settings = self.partner_settings.to_dict() if self.partner_settings else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "internalTitle": internal_title,
                "translations": translations,
            }
        )
        if pause_able is not UNSET:
            field_dict["pauseAble"] = pause_able
        if invoice_address_mandatory is not UNSET:
            field_dict["invoiceAddressMandatory"] = invoice_address_mandatory
        if delivery_address_mandatory is not UNSET:
            field_dict["deliveryAddressMandatory"] = delivery_address_mandatory
        if multiple_purchases is not UNSET:
            field_dict["multiplePurchases"] = multiple_purchases
        if misuse_rule_id is not UNSET:
            field_dict["misuseRuleId"] = misuse_rule_id
        if delivery_list_id is not UNSET:
            field_dict["deliveryListId"] = delivery_list_id
        if fixed_start_date is not UNSET:
            field_dict["fixedStartDate"] = fixed_start_date
        if issues_in_past is not UNSET:
            field_dict["issuesInPast"] = issues_in_past
        if issues_in_future is not UNSET:
            field_dict["issuesInFuture"] = issues_in_future
        if archived is not UNSET:
            field_dict["archived"] = archived
        if allowed_payment_methods is not UNSET:
            field_dict["allowedPaymentMethods"] = allowed_payment_methods
        if connected_company_settings is not UNSET:
            field_dict["connectedCompanySettings"] = connected_company_settings
        if leaf_id is not UNSET:
            field_dict["leafId"] = leaf_id
        if external_billing is not UNSET:
            field_dict["externalBilling"] = external_billing
        if customer_cancellation_blocked is not UNSET:
            field_dict["customerCancellationBlocked"] = customer_cancellation_blocked
        if corporate_account_users is not UNSET:
            field_dict["corporateAccountUsers"] = corporate_account_users
        if corporate_account_invitation_url is not UNSET:
            field_dict["corporateAccountInvitationUrl"] = corporate_account_invitation_url
        if bonus_id is not UNSET:
            field_dict["bonusId"] = bonus_id
        if managed_external is not UNSET:
            field_dict["managedExternal"] = managed_external
        if pdf_template_usage is not UNSET:
            field_dict["pdfTemplateUsage"] = pdf_template_usage
        if partner_settings is not UNSET:
            field_dict["partnerSettings"] = partner_settings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.offer_connected_company_settings import OfferConnectedCompanySettings
        from ..models.offer_partner_settings import OfferPartnerSettings
        from ..models.offer_translation import OfferTranslation

        d = src_dict.copy()
        internal_title = d.pop("internalTitle")

        translations = []
        _translations = d.pop("translations")
        for translations_item_data in _translations:
            translations_item = OfferTranslation.from_dict(translations_item_data)

            translations.append(translations_item)

        pause_able = d.pop("pauseAble", UNSET)

        invoice_address_mandatory = d.pop("invoiceAddressMandatory", UNSET)

        delivery_address_mandatory = d.pop("deliveryAddressMandatory", UNSET)

        multiple_purchases = d.pop("multiplePurchases", UNSET)

        misuse_rule_id = d.pop("misuseRuleId", UNSET)

        delivery_list_id = d.pop("deliveryListId", UNSET)

        _fixed_start_date = d.pop("fixedStartDate", UNSET)
        fixed_start_date: Union[Unset, None, datetime.date]
        if _fixed_start_date is None:
            fixed_start_date = None
        elif isinstance(_fixed_start_date, Unset):
            fixed_start_date = UNSET
        else:
            fixed_start_date = isoparse(_fixed_start_date).date()

        issues_in_past = d.pop("issuesInPast", UNSET)

        issues_in_future = d.pop("issuesInFuture", UNSET)

        archived = d.pop("archived", UNSET)

        allowed_payment_methods = []
        _allowed_payment_methods = d.pop("allowedPaymentMethods", UNSET)
        for allowed_payment_methods_item_data in _allowed_payment_methods or []:
            allowed_payment_methods_item = OfferBaseAllowedPaymentMethodsItem(allowed_payment_methods_item_data)

            allowed_payment_methods.append(allowed_payment_methods_item)

        _connected_company_settings = d.pop("connectedCompanySettings", UNSET)
        connected_company_settings: Union[Unset, OfferConnectedCompanySettings]
        if isinstance(_connected_company_settings, Unset):
            connected_company_settings = UNSET
        else:
            connected_company_settings = OfferConnectedCompanySettings.from_dict(_connected_company_settings)

        leaf_id = d.pop("leafId", UNSET)

        external_billing = d.pop("externalBilling", UNSET)

        customer_cancellation_blocked = d.pop("customerCancellationBlocked", UNSET)

        corporate_account_users = d.pop("corporateAccountUsers", UNSET)

        corporate_account_invitation_url = d.pop("corporateAccountInvitationUrl", UNSET)

        bonus_id = d.pop("bonusId", UNSET)

        managed_external = d.pop("managedExternal", UNSET)

        _pdf_template_usage = d.pop("pdfTemplateUsage", UNSET)
        pdf_template_usage: Union[Unset, OfferBasePdfTemplateUsage]
        if isinstance(_pdf_template_usage, Unset):
            pdf_template_usage = UNSET
        else:
            pdf_template_usage = OfferBasePdfTemplateUsage(_pdf_template_usage)

        _partner_settings = d.pop("partnerSettings", UNSET)
        partner_settings: Union[Unset, None, OfferPartnerSettings]
        if _partner_settings is None:
            partner_settings = None
        elif isinstance(_partner_settings, Unset):
            partner_settings = UNSET
        else:
            partner_settings = OfferPartnerSettings.from_dict(_partner_settings)

        offer_base = cls(
            internal_title=internal_title,
            translations=translations,
            pause_able=pause_able,
            invoice_address_mandatory=invoice_address_mandatory,
            delivery_address_mandatory=delivery_address_mandatory,
            multiple_purchases=multiple_purchases,
            misuse_rule_id=misuse_rule_id,
            delivery_list_id=delivery_list_id,
            fixed_start_date=fixed_start_date,
            issues_in_past=issues_in_past,
            issues_in_future=issues_in_future,
            archived=archived,
            allowed_payment_methods=allowed_payment_methods,
            connected_company_settings=connected_company_settings,
            leaf_id=leaf_id,
            external_billing=external_billing,
            customer_cancellation_blocked=customer_cancellation_blocked,
            corporate_account_users=corporate_account_users,
            corporate_account_invitation_url=corporate_account_invitation_url,
            bonus_id=bonus_id,
            managed_external=managed_external,
            pdf_template_usage=pdf_template_usage,
            partner_settings=partner_settings,
        )

        offer_base.additional_properties = d
        return offer_base

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
