import datetime
import logging
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.address_base import AddressBase
from ...models.error_result import ErrorResult
from ...models.error_result_base import ErrorResultBase
from ...models.future_address import FutureAddress
from ...types import UNSET, Response, Unset

log = logging.getLogger(__name__)


def _get_kwargs(
    address_id: int,
    date: datetime.date,
    *,
    body: AddressBase,
    override_validation: Union[Unset, bool] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["overrideValidation"] = override_validation

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/addresses/{address_id}/futureAddresses/{date}",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers

    log.debug(_kwargs)

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResult, ErrorResultBase, FutureAddress]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = FutureAddress.from_dict(response.json())

        return response_201
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

    if (response.status_code == HTTPStatus.BAD_GATEWAY) or (response.status_code == HTTPStatus.GATEWAY_TIMEOUT):
        raise errors.RetryableError

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResult, ErrorResultBase, FutureAddress]]:
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
    address_id: int,
    date: datetime.date,
    *,
    client: AuthenticatedClient,
    body: AddressBase,
    override_validation: Union[Unset, bool] = UNSET,
) -> Response[Union[ErrorResult, ErrorResultBase, FutureAddress]]:
    """Create future address

     Create a new future address with the data provided. A address can only have two future addresses

    Args:
        address_id (int):
        date (datetime.date):
        override_validation (Union[Unset, bool]):
        body (AddressBase):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResult, ErrorResultBase, FutureAddress]]
    """

    kwargs = _get_kwargs(
        address_id=address_id,
        date=date,
        body=body,
        override_validation=override_validation,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    address_id: int,
    date: datetime.date,
    *,
    client: AuthenticatedClient,
    body: AddressBase,
    override_validation: Union[Unset, bool] = UNSET,
) -> Optional[Union[ErrorResult, ErrorResultBase, FutureAddress]]:
    """Create future address

     Create a new future address with the data provided. A address can only have two future addresses

    Args:
        address_id (int):
        date (datetime.date):
        override_validation (Union[Unset, bool]):
        body (AddressBase):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResult, ErrorResultBase, FutureAddress]
    """

    return sync_detailed(
        address_id=address_id,
        date=date,
        client=client,
        body=body,
        override_validation=override_validation,
    ).parsed


@retry(
    retry=retry_if_exception_type(errors.RetryableError),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=30),
)
async def asyncio_detailed(
    address_id: int,
    date: datetime.date,
    *,
    client: AuthenticatedClient,
    body: AddressBase,
    override_validation: Union[Unset, bool] = UNSET,
) -> Response[Union[ErrorResult, ErrorResultBase, FutureAddress]]:
    """Create future address

     Create a new future address with the data provided. A address can only have two future addresses

    Args:
        address_id (int):
        date (datetime.date):
        override_validation (Union[Unset, bool]):
        body (AddressBase):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResult, ErrorResultBase, FutureAddress]]
    """

    kwargs = _get_kwargs(
        address_id=address_id,
        date=date,
        body=body,
        override_validation=override_validation,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    address_id: int,
    date: datetime.date,
    *,
    client: AuthenticatedClient,
    body: AddressBase,
    override_validation: Union[Unset, bool] = UNSET,
) -> Optional[Union[ErrorResult, ErrorResultBase, FutureAddress]]:
    """Create future address

     Create a new future address with the data provided. A address can only have two future addresses

    Args:
        address_id (int):
        date (datetime.date):
        override_validation (Union[Unset, bool]):
        body (AddressBase):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResult, ErrorResultBase, FutureAddress]
    """

    return (
        await asyncio_detailed(
            address_id=address_id,
            date=date,
            client=client,
            body=body,
            override_validation=override_validation,
        )
    ).parsed
