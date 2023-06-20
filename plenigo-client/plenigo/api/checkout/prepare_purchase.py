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

from ...models.checkout_preparation import CheckoutPreparation
from ...models.checkout_preparation_result import CheckoutPreparationResult
from ...models.error_result_base import ErrorResultBase


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: CheckoutPreparation,
) -> Dict[str, Any]:
    url = "{}/checkout/preparePurchase".format(client.api.value)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    kwargs = {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }

    log.debug(kwargs)

    return kwargs


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[CheckoutPreparationResult, ErrorResultBase]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = CheckoutPreparationResult.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResultBase.from_dict(response.json())

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
    *, client: Client, response: httpx.Response
) -> Response[Union[CheckoutPreparationResult, ErrorResultBase]]:
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
    *,
    client: AuthenticatedClient,
    json_body: CheckoutPreparation,
) -> Response[Union[CheckoutPreparationResult, ErrorResultBase]]:
    """Prepare purchase

     Prepares everything for a purchase that a customer is supposed to do. The purchase order id returned
    is only valid a limited time so this method
    should be called in time before the customer is sent to the checkout.

    Args:
        json_body (CheckoutPreparation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CheckoutPreparationResult, ErrorResultBase]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: CheckoutPreparation,
) -> Optional[Union[CheckoutPreparationResult, ErrorResultBase]]:
    """Prepare purchase

     Prepares everything for a purchase that a customer is supposed to do. The purchase order id returned
    is only valid a limited time so this method
    should be called in time before the customer is sent to the checkout.

    Args:
        json_body (CheckoutPreparation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CheckoutPreparationResult, ErrorResultBase]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


@retry(
    retry=retry_if_exception_type(errors.RetryableError),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=30),
)
async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: CheckoutPreparation,
) -> Response[Union[CheckoutPreparationResult, ErrorResultBase]]:
    """Prepare purchase

     Prepares everything for a purchase that a customer is supposed to do. The purchase order id returned
    is only valid a limited time so this method
    should be called in time before the customer is sent to the checkout.

    Args:
        json_body (CheckoutPreparation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CheckoutPreparationResult, ErrorResultBase]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: CheckoutPreparation,
) -> Optional[Union[CheckoutPreparationResult, ErrorResultBase]]:
    """Prepare purchase

     Prepares everything for a purchase that a customer is supposed to do. The purchase order id returned
    is only valid a limited time so this method
    should be called in time before the customer is sent to the checkout.

    Args:
        json_body (CheckoutPreparation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CheckoutPreparationResult, ErrorResultBase]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
