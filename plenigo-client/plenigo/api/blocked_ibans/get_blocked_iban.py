import logging
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response

logger = logging.getLogger(__name__)

from ...models.blocked_iban import BlockedIban
from ...models.error_result import ErrorResult
from ...models.error_result_base import ErrorResultBase


def _get_kwargs(
    blocked_iban_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/settings/blockedIbans/{blocked_iban_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BlockedIban, ErrorResult, ErrorResultBase]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = BlockedIban.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResult.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ErrorResultBase.from_dict(response.json())

        return response_401
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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[BlockedIban, ErrorResult, ErrorResultBase]]:
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
    blocked_iban_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[BlockedIban, ErrorResult, ErrorResultBase]]:
    """Get

     Get blocked iban for a company.

    Args:
        blocked_iban_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BlockedIban, ErrorResult, ErrorResultBase]]
    """

    kwargs = _get_kwargs(
        blocked_iban_id=blocked_iban_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    blocked_iban_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[BlockedIban, ErrorResult, ErrorResultBase]]:
    """Get

     Get blocked iban for a company.

    Args:
        blocked_iban_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BlockedIban, ErrorResult, ErrorResultBase]
    """

    return sync_detailed(
        blocked_iban_id=blocked_iban_id,
        client=client,
    ).parsed


@retry(
    retry=retry_if_exception_type(errors.RetryableError),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=30),
)
async def asyncio_detailed(
    blocked_iban_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[BlockedIban, ErrorResult, ErrorResultBase]]:
    """Get

     Get blocked iban for a company.

    Args:
        blocked_iban_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BlockedIban, ErrorResult, ErrorResultBase]]
    """

    kwargs = _get_kwargs(
        blocked_iban_id=blocked_iban_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    blocked_iban_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[BlockedIban, ErrorResult, ErrorResultBase]]:
    """Get

     Get blocked iban for a company.

    Args:
        blocked_iban_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BlockedIban, ErrorResult, ErrorResultBase]
    """

    return (
        await asyncio_detailed(
            blocked_iban_id=blocked_iban_id,
            client=client,
        )
    ).parsed
