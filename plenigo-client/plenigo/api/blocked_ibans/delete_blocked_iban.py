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

from ...models.error_result_base import ErrorResultBase
from ...models.success_status import SuccessStatus


def _get_kwargs(
    blocked_iban_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/settings/blockedIbans/{blockedIbanId}".format(client.api.value, blockedIbanId=blocked_iban_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    kwargs = {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }

    log.debug(kwargs)

    return kwargs


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[ErrorResultBase, SuccessStatus]]:
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = SuccessStatus.from_dict(response.json())

        return response_202
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResultBase.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ErrorResultBase.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ErrorResultBase.from_dict(response.json())

        return response_500

    if (response.status_code == HTTPStatus.BAD_GATEWAY) or (response.status_code == HTTPStatus.GATEWAY_TIMEOUT):
        raise errors.RetryableError

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[ErrorResultBase, SuccessStatus]]:
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
    blocked_iban_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorResultBase, SuccessStatus]]:
    """Delete a blocked iban

     Delete a blocked iban for a company.

    Args:
        blocked_iban_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResultBase, SuccessStatus]]
    """

    kwargs = _get_kwargs(
        blocked_iban_id=blocked_iban_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    blocked_iban_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorResultBase, SuccessStatus]]:
    """Delete a blocked iban

     Delete a blocked iban for a company.

    Args:
        blocked_iban_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResultBase, SuccessStatus]
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
) -> Response[Union[ErrorResultBase, SuccessStatus]]:
    """Delete a blocked iban

     Delete a blocked iban for a company.

    Args:
        blocked_iban_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResultBase, SuccessStatus]]
    """

    kwargs = _get_kwargs(
        blocked_iban_id=blocked_iban_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    blocked_iban_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorResultBase, SuccessStatus]]:
    """Delete a blocked iban

     Delete a blocked iban for a company.

    Args:
        blocked_iban_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResultBase, SuccessStatus]
    """

    return (
        await asyncio_detailed(
            blocked_iban_id=blocked_iban_id,
            client=client,
        )
    ).parsed
