import logging
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.address import Address
from ...models.address_creation import AddressCreation
from ...models.error_result import ErrorResult
from ...models.error_result_base import ErrorResultBase
from ...types import Response

log = logging.getLogger(__name__)


def _get_kwargs(
    *,
    body: AddressCreation,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/addresses/validate",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers

    log.debug(_kwargs)

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Address, Any, ErrorResult, ErrorResultBase]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Address.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResult.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ErrorResultBase.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.PAYMENT_REQUIRED:
        response_402 = cast(Any, None)
        return response_402
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
) -> Response[Union[Address, Any, ErrorResult, ErrorResultBase]]:
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
) -> Response[Union[Address, Any, ErrorResult, ErrorResultBase]]:
    r"""Validate address data

     <span style=\"color:red\">**Important note: The use of these API endpoints is a chargeable service
    provided by plenigo GmbH. The billing is done according to the current price
           list, which you can find in the settings section of your plenigo account. The billing is done
    with the monthly invoice.**</span>
    Validates the address with the data provided.

    Args:
        body (AddressCreation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Address, Any, ErrorResult, ErrorResultBase]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: AddressCreation,
) -> Optional[Union[Address, Any, ErrorResult, ErrorResultBase]]:
    r"""Validate address data

     <span style=\"color:red\">**Important note: The use of these API endpoints is a chargeable service
    provided by plenigo GmbH. The billing is done according to the current price
           list, which you can find in the settings section of your plenigo account. The billing is done
    with the monthly invoice.**</span>
    Validates the address with the data provided.

    Args:
        body (AddressCreation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Address, Any, ErrorResult, ErrorResultBase]
    """

    return sync_detailed(
        client=client,
        body=body,
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
) -> Response[Union[Address, Any, ErrorResult, ErrorResultBase]]:
    r"""Validate address data

     <span style=\"color:red\">**Important note: The use of these API endpoints is a chargeable service
    provided by plenigo GmbH. The billing is done according to the current price
           list, which you can find in the settings section of your plenigo account. The billing is done
    with the monthly invoice.**</span>
    Validates the address with the data provided.

    Args:
        body (AddressCreation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Address, Any, ErrorResult, ErrorResultBase]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AddressCreation,
) -> Optional[Union[Address, Any, ErrorResult, ErrorResultBase]]:
    r"""Validate address data

     <span style=\"color:red\">**Important note: The use of these API endpoints is a chargeable service
    provided by plenigo GmbH. The billing is done according to the current price
           list, which you can find in the settings section of your plenigo account. The billing is done
    with the monthly invoice.**</span>
    Validates the address with the data provided.

    Args:
        body (AddressCreation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Address, Any, ErrorResult, ErrorResultBase]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
