import logging
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response

log = logging.getLogger(__name__)

from typing import Dict

from ...models.bank_account_change import BankAccountChange
from ...models.error_result_base import ErrorResultBase


def _get_kwargs(
    bank_account_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/paymentMethods/bankAccounts/{bankAccountId}".format(client.api.value, bankAccountId=bank_account_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    kwargs = {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }

    log.debug(kwargs)

    return kwargs


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[BankAccountChange, ErrorResultBase]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = BankAccountChange.from_dict(response.json())

        return response_200
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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[BankAccountChange, ErrorResultBase]]:
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
    bank_account_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[BankAccountChange, ErrorResultBase]]:
    """Get a bank account entity

     Get bank account that is identified by the passed bank account id.

    Args:
        bank_account_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BankAccountChange, ErrorResultBase]]
    """

    kwargs = _get_kwargs(
        bank_account_id=bank_account_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bank_account_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[BankAccountChange, ErrorResultBase]]:
    """Get a bank account entity

     Get bank account that is identified by the passed bank account id.

    Args:
        bank_account_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BankAccountChange, ErrorResultBase]
    """

    return sync_detailed(
        bank_account_id=bank_account_id,
        client=client,
    ).parsed


@retry(
    retry=retry_if_exception_type(errors.RetryableError),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=30),
)
async def asyncio_detailed(
    bank_account_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[BankAccountChange, ErrorResultBase]]:
    """Get a bank account entity

     Get bank account that is identified by the passed bank account id.

    Args:
        bank_account_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BankAccountChange, ErrorResultBase]]
    """

    kwargs = _get_kwargs(
        bank_account_id=bank_account_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bank_account_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[BankAccountChange, ErrorResultBase]]:
    """Get a bank account entity

     Get bank account that is identified by the passed bank account id.

    Args:
        bank_account_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BankAccountChange, ErrorResultBase]
    """

    return (
        await asyncio_detailed(
            bank_account_id=bank_account_id,
            client=client,
        )
    ).parsed
