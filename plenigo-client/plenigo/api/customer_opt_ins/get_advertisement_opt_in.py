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

from ...models.customer_opt_in_creation import CustomerOptInCreation
from ...models.error_result_base import ErrorResultBase


def _get_kwargs(
    customer_opt_in_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/settings/advertisementOptIns/{customerOptInId}".format(
        client.api.value, customerOptInId=customer_opt_in_id
    )

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


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[CustomerOptInCreation, ErrorResultBase]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CustomerOptInCreation.from_dict(response.json())

        return response_200
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
) -> Response[Union[CustomerOptInCreation, ErrorResultBase]]:
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
    customer_opt_in_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[CustomerOptInCreation, ErrorResultBase]]:
    """Get advertisement opt in

     Get advertisement opt in that is identified by the passed advertisement opt in id.

    Args:
        customer_opt_in_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CustomerOptInCreation, ErrorResultBase]]
    """

    kwargs = _get_kwargs(
        customer_opt_in_id=customer_opt_in_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_opt_in_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[CustomerOptInCreation, ErrorResultBase]]:
    """Get advertisement opt in

     Get advertisement opt in that is identified by the passed advertisement opt in id.

    Args:
        customer_opt_in_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CustomerOptInCreation, ErrorResultBase]
    """

    return sync_detailed(
        customer_opt_in_id=customer_opt_in_id,
        client=client,
    ).parsed


@retry(
    retry=retry_if_exception_type(errors.RetryableError),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=30),
)
async def asyncio_detailed(
    customer_opt_in_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[CustomerOptInCreation, ErrorResultBase]]:
    """Get advertisement opt in

     Get advertisement opt in that is identified by the passed advertisement opt in id.

    Args:
        customer_opt_in_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CustomerOptInCreation, ErrorResultBase]]
    """

    kwargs = _get_kwargs(
        customer_opt_in_id=customer_opt_in_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_opt_in_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[CustomerOptInCreation, ErrorResultBase]]:
    """Get advertisement opt in

     Get advertisement opt in that is identified by the passed advertisement opt in id.

    Args:
        customer_opt_in_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CustomerOptInCreation, ErrorResultBase]
    """

    return (
        await asyncio_detailed(
            customer_opt_in_id=customer_opt_in_id,
            client=client,
        )
    ).parsed
