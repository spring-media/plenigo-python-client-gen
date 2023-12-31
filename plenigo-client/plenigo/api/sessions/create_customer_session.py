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

from ...models.customer_session_token import CustomerSessionToken
from ...models.error_result_base import ErrorResultBase
from ...models.logging_data import LoggingData
from ...models.session_limit_reached import SessionLimitReached


def _get_kwargs(
    customer_id: str,
    *,
    client: AuthenticatedClient,
    json_body: LoggingData,
) -> Dict[str, Any]:
    url = "{}/sessions/{customerId}".format(client.api.value, customerId=customer_id)

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
) -> Optional[Union[CustomerSessionToken, ErrorResultBase, SessionLimitReached]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SessionLimitReached.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = CustomerSessionToken.from_dict(response.json())

        return response_202
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResultBase.from_dict(response.json())

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
    *, client: Client, response: httpx.Response
) -> Response[Union[CustomerSessionToken, ErrorResultBase, SessionLimitReached]]:
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
    customer_id: str,
    *,
    client: AuthenticatedClient,
    json_body: LoggingData,
) -> Response[Union[CustomerSessionToken, ErrorResultBase, SessionLimitReached]]:
    """Create

     Creates a new customer session for the provided customer id. More information provided during the
    session creation process will lead to a better
    session protection and also helps the user to identify which session he wants to remove if multiple
    parallel log ins are allowed and the maximum
    active session limit is reached.

    Args:
        customer_id (str):
        json_body (LoggingData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CustomerSessionToken, ErrorResultBase, SessionLimitReached]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_id: str,
    *,
    client: AuthenticatedClient,
    json_body: LoggingData,
) -> Optional[Union[CustomerSessionToken, ErrorResultBase, SessionLimitReached]]:
    """Create

     Creates a new customer session for the provided customer id. More information provided during the
    session creation process will lead to a better
    session protection and also helps the user to identify which session he wants to remove if multiple
    parallel log ins are allowed and the maximum
    active session limit is reached.

    Args:
        customer_id (str):
        json_body (LoggingData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CustomerSessionToken, ErrorResultBase, SessionLimitReached]
    """

    return sync_detailed(
        customer_id=customer_id,
        client=client,
        json_body=json_body,
    ).parsed


@retry(
    retry=retry_if_exception_type(errors.RetryableError),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=30),
)
async def asyncio_detailed(
    customer_id: str,
    *,
    client: AuthenticatedClient,
    json_body: LoggingData,
) -> Response[Union[CustomerSessionToken, ErrorResultBase, SessionLimitReached]]:
    """Create

     Creates a new customer session for the provided customer id. More information provided during the
    session creation process will lead to a better
    session protection and also helps the user to identify which session he wants to remove if multiple
    parallel log ins are allowed and the maximum
    active session limit is reached.

    Args:
        customer_id (str):
        json_body (LoggingData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CustomerSessionToken, ErrorResultBase, SessionLimitReached]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_id: str,
    *,
    client: AuthenticatedClient,
    json_body: LoggingData,
) -> Optional[Union[CustomerSessionToken, ErrorResultBase, SessionLimitReached]]:
    """Create

     Creates a new customer session for the provided customer id. More information provided during the
    session creation process will lead to a better
    session protection and also helps the user to identify which session he wants to remove if multiple
    parallel log ins are allowed and the maximum
    active session limit is reached.

    Args:
        customer_id (str):
        json_body (LoggingData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CustomerSessionToken, ErrorResultBase, SessionLimitReached]
    """

    return (
        await asyncio_detailed(
            customer_id=customer_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
