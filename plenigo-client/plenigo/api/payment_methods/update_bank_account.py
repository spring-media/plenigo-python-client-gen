import logging
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bank_account import BankAccount
from ...models.bank_account_change import BankAccountChange
from ...models.error_result import ErrorResult
from ...models.error_result_base import ErrorResultBase
from ...types import Response

log = logging.getLogger(__name__)


def _get_kwargs(
    bank_account_id: int,
    *,
    body: BankAccountChange,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/paymentMethods/bankAccounts/{bank_account_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers

    log.debug(_kwargs)

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BankAccount, ErrorResult, ErrorResultBase]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = BankAccount.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResult.from_dict(response.json())

        return response_400
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
    if response.status_code == HTTPStatus.BAD_GATEWAY:
        response_502 = ErrorResultBase.from_dict(response.json())

        return response_502
    if response.status_code == HTTPStatus.GATEWAY_TIMEOUT:
        response_504 = ErrorResultBase.from_dict(response.json())

        return response_504

    if (response.status_code == HTTPStatus.BAD_GATEWAY) or (response.status_code == HTTPStatus.GATEWAY_TIMEOUT):
        raise errors.RetryableError

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[BankAccount, ErrorResult, ErrorResultBase]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@retry(
    retry=retry_if_exception_type(errors.RetryableError),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=30),
)
def sync_detailed(
    bank_account_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: BankAccountChange,
) -> Response[Union[BankAccount, ErrorResult, ErrorResultBase]]:
    """Update bank account entity

     Update a bank account that is identified by the passed bank account id with the data provided.

    Args:
        bank_account_id (int):
        body (BankAccountChange):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BankAccount, ErrorResult, ErrorResultBase]]
    """

    kwargs = _get_kwargs(
        bank_account_id=bank_account_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bank_account_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: BankAccountChange,
) -> Optional[Union[BankAccount, ErrorResult, ErrorResultBase]]:
    """Update bank account entity

     Update a bank account that is identified by the passed bank account id with the data provided.

    Args:
        bank_account_id (int):
        body (BankAccountChange):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BankAccount, ErrorResult, ErrorResultBase]
    """

    return sync_detailed(
        bank_account_id=bank_account_id,
        client=client,
        body=body,
    ).parsed


@retry(
    retry=retry_if_exception_type(errors.RetryableError),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=30),
)
async def asyncio_detailed(
    bank_account_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: BankAccountChange,
) -> Response[Union[BankAccount, ErrorResult, ErrorResultBase]]:
    """Update bank account entity

     Update a bank account that is identified by the passed bank account id with the data provided.

    Args:
        bank_account_id (int):
        body (BankAccountChange):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BankAccount, ErrorResult, ErrorResultBase]]
    """

    kwargs = _get_kwargs(
        bank_account_id=bank_account_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bank_account_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: BankAccountChange,
) -> Optional[Union[BankAccount, ErrorResult, ErrorResultBase]]:
    """Update bank account entity

     Update a bank account that is identified by the passed bank account id with the data provided.

    Args:
        bank_account_id (int):
        body (BankAccountChange):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BankAccount, ErrorResult, ErrorResultBase]
    """

    return (
        await asyncio_detailed(
            bank_account_id=bank_account_id,
            client=client,
            body=body,
        )
    ).parsed
