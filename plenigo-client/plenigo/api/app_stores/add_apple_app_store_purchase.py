import logging
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_store_purchase_list import AppStorePurchaseList
from ...models.apple_app_store_purchase_addition import AppleAppStorePurchaseAddition
from ...models.error_result import ErrorResult
from ...models.error_result_base import ErrorResultBase
from ...types import Response

log = logging.getLogger(__name__)


def _get_kwargs(
    *,
    body: AppleAppStorePurchaseAddition,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/appStores/appleAppStore",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers

    log.debug(_kwargs)

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AppStorePurchaseList, ErrorResult, ErrorResultBase]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = AppStorePurchaseList.from_dict(response.json())

        return response_201
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
) -> Response[Union[AppStorePurchaseList, ErrorResult, ErrorResultBase]]:
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
    body: AppleAppStorePurchaseAddition,
) -> Response[Union[AppStorePurchaseList, ErrorResult, ErrorResultBase]]:
    """Add Apple purchase

     Add an Apple app store purchase to the plenigo system and retrieve a token for further processing.

    Args:
        body (AppleAppStorePurchaseAddition):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AppStorePurchaseList, ErrorResult, ErrorResultBase]]
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
    body: AppleAppStorePurchaseAddition,
) -> Optional[Union[AppStorePurchaseList, ErrorResult, ErrorResultBase]]:
    """Add Apple purchase

     Add an Apple app store purchase to the plenigo system and retrieve a token for further processing.

    Args:
        body (AppleAppStorePurchaseAddition):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AppStorePurchaseList, ErrorResult, ErrorResultBase]
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
    body: AppleAppStorePurchaseAddition,
) -> Response[Union[AppStorePurchaseList, ErrorResult, ErrorResultBase]]:
    """Add Apple purchase

     Add an Apple app store purchase to the plenigo system and retrieve a token for further processing.

    Args:
        body (AppleAppStorePurchaseAddition):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AppStorePurchaseList, ErrorResult, ErrorResultBase]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AppleAppStorePurchaseAddition,
) -> Optional[Union[AppStorePurchaseList, ErrorResult, ErrorResultBase]]:
    """Add Apple purchase

     Add an Apple app store purchase to the plenigo system and retrieve a token for further processing.

    Args:
        body (AppleAppStorePurchaseAddition):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AppStorePurchaseList, ErrorResult, ErrorResultBase]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
