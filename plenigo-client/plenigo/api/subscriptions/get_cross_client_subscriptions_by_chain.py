import logging
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_result_base import ErrorResultBase
from ...models.subscriptions import Subscriptions
from ...types import Response

log = logging.getLogger(__name__)


def _get_kwargs(
    chain_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/subscriptions/crossClient/chain/{chain_id}",
    }

    log.debug(_kwargs)

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResultBase, Subscriptions]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Subscriptions.from_dict(response.json())

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


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResultBase, Subscriptions]]:
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
    chain_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorResultBase, Subscriptions]]:
    """Get cross client subscription by chain

     Get all cross client subscriptions that belong to a specific subscription chain that is identified
    by the passed chain id.

    Args:
        chain_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResultBase, Subscriptions]]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chain_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorResultBase, Subscriptions]]:
    """Get cross client subscription by chain

     Get all cross client subscriptions that belong to a specific subscription chain that is identified
    by the passed chain id.

    Args:
        chain_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResultBase, Subscriptions]
    """

    return sync_detailed(
        chain_id=chain_id,
        client=client,
    ).parsed


@retry(
    retry=retry_if_exception_type(errors.RetryableError),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=30),
)
async def asyncio_detailed(
    chain_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorResultBase, Subscriptions]]:
    """Get cross client subscription by chain

     Get all cross client subscriptions that belong to a specific subscription chain that is identified
    by the passed chain id.

    Args:
        chain_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResultBase, Subscriptions]]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chain_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorResultBase, Subscriptions]]:
    """Get cross client subscription by chain

     Get all cross client subscriptions that belong to a specific subscription chain that is identified
    by the passed chain id.

    Args:
        chain_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResultBase, Subscriptions]
    """

    return (
        await asyncio_detailed(
            chain_id=chain_id,
            client=client,
        )
    ).parsed