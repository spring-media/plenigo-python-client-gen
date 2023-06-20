import logging
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

log = logging.getLogger(__name__)

from typing import Dict, Optional, Union, cast

from ...models.error_result_base import ErrorResultBase
from ...models.success_status import SuccessStatus
from ...types import UNSET, Unset


def _get_kwargs(
    invoice_id: int,
    *,
    client: AuthenticatedClient,
    suppress_customer_mail: Union[Unset, None, bool] = UNSET,
    suppress_refund: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/invoices/{invoiceId}/cancel".format(client.api.value, invoiceId=invoice_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["suppressCustomerMail"] = suppress_customer_mail

    params["suppressRefund"] = suppress_refund

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    kwargs = {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }

    log.debug(kwargs)

    return kwargs


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, ErrorResultBase, SuccessStatus]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SuccessStatus.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.MULTI_STATUS:
        response_207 = cast(Any, None)
        return response_207
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ErrorResultBase.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorResultBase.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = ErrorResultBase.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ErrorResultBase.from_dict(response.json())

        return response_500

    if (response.status_code == HTTPStatus.BAD_GATEWAY) or (response.status_code == HTTPStatus.GATEWAY_TIMEOUT):
        raise errors.RetryableError

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, ErrorResultBase, SuccessStatus]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )  # type: ignore


@retry(
    retry=retry_if_exception_type(errors.RetryableError),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=30),
)
def sync_detailed(
    invoice_id: int,
    *,
    client: AuthenticatedClient,
    suppress_customer_mail: Union[Unset, None, bool] = UNSET,
    suppress_refund: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, ErrorResultBase, SuccessStatus]]:
    """Cancel invoice

     Cancel an invoice - only invoices of type INVOICE can be cancelled.

    Args:
        invoice_id (int):
        suppress_customer_mail (Union[Unset, None, bool]):
        suppress_refund (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResultBase, SuccessStatus]]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        client=client,
        suppress_customer_mail=suppress_customer_mail,
        suppress_refund=suppress_refund,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    invoice_id: int,
    *,
    client: AuthenticatedClient,
    suppress_customer_mail: Union[Unset, None, bool] = UNSET,
    suppress_refund: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, ErrorResultBase, SuccessStatus]]:
    """Cancel invoice

     Cancel an invoice - only invoices of type INVOICE can be cancelled.

    Args:
        invoice_id (int):
        suppress_customer_mail (Union[Unset, None, bool]):
        suppress_refund (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResultBase, SuccessStatus]
    """

    return sync_detailed(
        invoice_id=invoice_id,
        client=client,
        suppress_customer_mail=suppress_customer_mail,
        suppress_refund=suppress_refund,
    ).parsed


@retry(
    retry=retry_if_exception_type(errors.RetryableError),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=30),
)
async def asyncio_detailed(
    invoice_id: int,
    *,
    client: AuthenticatedClient,
    suppress_customer_mail: Union[Unset, None, bool] = UNSET,
    suppress_refund: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, ErrorResultBase, SuccessStatus]]:
    """Cancel invoice

     Cancel an invoice - only invoices of type INVOICE can be cancelled.

    Args:
        invoice_id (int):
        suppress_customer_mail (Union[Unset, None, bool]):
        suppress_refund (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResultBase, SuccessStatus]]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        client=client,
        suppress_customer_mail=suppress_customer_mail,
        suppress_refund=suppress_refund,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    invoice_id: int,
    *,
    client: AuthenticatedClient,
    suppress_customer_mail: Union[Unset, None, bool] = UNSET,
    suppress_refund: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, ErrorResultBase, SuccessStatus]]:
    """Cancel invoice

     Cancel an invoice - only invoices of type INVOICE can be cancelled.

    Args:
        invoice_id (int):
        suppress_customer_mail (Union[Unset, None, bool]):
        suppress_refund (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResultBase, SuccessStatus]
    """

    return (
        await asyncio_detailed(
            invoice_id=invoice_id,
            client=client,
            suppress_customer_mail=suppress_customer_mail,
            suppress_refund=suppress_refund,
        )
    ).parsed
