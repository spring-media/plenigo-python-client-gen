import logging
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_result_base import ErrorResultBase
from ...models.get_customer_mark_customer_mark import GetCustomerMarkCustomerMark
from ...models.wbz_customer_mark import WbzCustomerMark
from ...types import Response

log = logging.getLogger(__name__)


def _get_kwargs(
    customer_id: str,
    customer_mark: GetCustomerMarkCustomerMark,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/customers/{customer_id}/marks/{customer_mark}",
    }

    log.debug(_kwargs)

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorResultBase, WbzCustomerMark]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = WbzCustomerMark.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ErrorResultBase.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.PAYMENT_REQUIRED:
        response_402 = cast(Any, None)
        return response_402
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorResultBase.from_dict(response.json())

        return response_404
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
) -> Response[Union[Any, ErrorResultBase, WbzCustomerMark]]:
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
    customer_id: str,
    customer_mark: GetCustomerMarkCustomerMark,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ErrorResultBase, WbzCustomerMark]]:
    """Get customer mark data

     Get the customer mark data.

    Args:
        customer_id (str):
        customer_mark (GetCustomerMarkCustomerMark):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResultBase, WbzCustomerMark]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        customer_mark=customer_mark,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_id: str,
    customer_mark: GetCustomerMarkCustomerMark,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ErrorResultBase, WbzCustomerMark]]:
    """Get customer mark data

     Get the customer mark data.

    Args:
        customer_id (str):
        customer_mark (GetCustomerMarkCustomerMark):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResultBase, WbzCustomerMark]
    """

    return sync_detailed(
        customer_id=customer_id,
        customer_mark=customer_mark,
        client=client,
    ).parsed


@retry(
    retry=retry_if_exception_type(errors.RetryableError),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=30),
)
async def asyncio_detailed(
    customer_id: str,
    customer_mark: GetCustomerMarkCustomerMark,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ErrorResultBase, WbzCustomerMark]]:
    """Get customer mark data

     Get the customer mark data.

    Args:
        customer_id (str):
        customer_mark (GetCustomerMarkCustomerMark):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResultBase, WbzCustomerMark]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        customer_mark=customer_mark,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_id: str,
    customer_mark: GetCustomerMarkCustomerMark,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ErrorResultBase, WbzCustomerMark]]:
    """Get customer mark data

     Get the customer mark data.

    Args:
        customer_id (str):
        customer_mark (GetCustomerMarkCustomerMark):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResultBase, WbzCustomerMark]
    """

    return (
        await asyncio_detailed(
            customer_id=customer_id,
            customer_mark=customer_mark,
            client=client,
        )
    ).parsed
