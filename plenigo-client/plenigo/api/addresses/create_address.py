import logging
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

logger = logging.getLogger(__name__)

from ...models.address import Address
from ...models.address_creation import AddressCreation
from ...models.error_result import ErrorResult
from ...models.error_result_base import ErrorResultBase
from ...types import Unset


def _get_kwargs(
    *,
    body: AddressCreation,
    override_validation: Union[Unset, bool] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["overrideValidation"] = override_validation

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/addresses",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Address, ErrorResult, ErrorResultBase]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = Address.from_dict(response.json())

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
) -> Response[Union[Address, ErrorResult, ErrorResultBase]]:
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
    *,
    client: AuthenticatedClient,
    body: AddressCreation,
    override_validation: Union[Unset, bool] = UNSET,
) -> Response[Union[Address, ErrorResult, ErrorResultBase]]:
    """Create address

     Create a new address with the data provided.

    Args:
        override_validation (Union[Unset, bool]):
        body (AddressCreation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Address, ErrorResult, ErrorResultBase]]
    """

    kwargs = _get_kwargs(
        body=body,
        override_validation=override_validation,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: AddressCreation,
    override_validation: Union[Unset, bool] = UNSET,
) -> Optional[Union[Address, ErrorResult, ErrorResultBase]]:
    """Create address

     Create a new address with the data provided.

    Args:
        override_validation (Union[Unset, bool]):
        body (AddressCreation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Address, ErrorResult, ErrorResultBase]
    """

    return sync_detailed(
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
    *,
    client: AuthenticatedClient,
    body: AddressCreation,
    override_validation: Union[Unset, bool] = UNSET,
) -> Response[Union[Address, ErrorResult, ErrorResultBase]]:
    """Create address

     Create a new address with the data provided.

    Args:
        override_validation (Union[Unset, bool]):
        body (AddressCreation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Address, ErrorResult, ErrorResultBase]]
    """

    kwargs = _get_kwargs(
        body=body,
        override_validation=override_validation,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AddressCreation,
    override_validation: Union[Unset, bool] = UNSET,
) -> Optional[Union[Address, ErrorResult, ErrorResultBase]]:
    """Create address

     Create a new address with the data provided.

    Args:
        override_validation (Union[Unset, bool]):
        body (AddressCreation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Address, ErrorResult, ErrorResultBase]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            override_validation=override_validation,
        )
    ).parsed
