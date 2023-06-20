import logging
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

log = logging.getLogger(__name__)

from typing import Dict, Optional, Union

from ...models.error_result_base import ErrorResultBase
from ...models.subscription import Subscription
from ...models.subscription_pause_at import SubscriptionPauseAt
from ...types import UNSET, Unset


def _get_kwargs(
    subscription_id: int,
    *,
    client: AuthenticatedClient,
    json_body: SubscriptionPauseAt,
    send_mail: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/subscriptions/{subscriptionId}/pause".format(client.api.value, subscriptionId=subscription_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["sendMail"] = send_mail

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    kwargs = {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
        "params": params,
    }

    log.debug(kwargs)

    return kwargs


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[ErrorResultBase, Subscription]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Subscription.from_dict(response.json())

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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[ErrorResultBase, Subscription]]:
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
    subscription_id: int,
    *,
    client: AuthenticatedClient,
    json_body: SubscriptionPauseAt,
    send_mail: Union[Unset, None, bool] = UNSET,
) -> Response[Union[ErrorResultBase, Subscription]]:
    """Pause subscription

     Pause a subscription during the given time range. Only subscriptions with the same accounting period
    and term can be paused.

    Args:
        subscription_id (int):
        send_mail (Union[Unset, None, bool]):
        json_body (SubscriptionPauseAt):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResultBase, Subscription]]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        client=client,
        json_body=json_body,
        send_mail=send_mail,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    subscription_id: int,
    *,
    client: AuthenticatedClient,
    json_body: SubscriptionPauseAt,
    send_mail: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[ErrorResultBase, Subscription]]:
    """Pause subscription

     Pause a subscription during the given time range. Only subscriptions with the same accounting period
    and term can be paused.

    Args:
        subscription_id (int):
        send_mail (Union[Unset, None, bool]):
        json_body (SubscriptionPauseAt):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResultBase, Subscription]
    """

    return sync_detailed(
        subscription_id=subscription_id,
        client=client,
        json_body=json_body,
        send_mail=send_mail,
    ).parsed


@retry(
    retry=retry_if_exception_type(errors.RetryableError),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=30),
)
async def asyncio_detailed(
    subscription_id: int,
    *,
    client: AuthenticatedClient,
    json_body: SubscriptionPauseAt,
    send_mail: Union[Unset, None, bool] = UNSET,
) -> Response[Union[ErrorResultBase, Subscription]]:
    """Pause subscription

     Pause a subscription during the given time range. Only subscriptions with the same accounting period
    and term can be paused.

    Args:
        subscription_id (int):
        send_mail (Union[Unset, None, bool]):
        json_body (SubscriptionPauseAt):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResultBase, Subscription]]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        client=client,
        json_body=json_body,
        send_mail=send_mail,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    subscription_id: int,
    *,
    client: AuthenticatedClient,
    json_body: SubscriptionPauseAt,
    send_mail: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[ErrorResultBase, Subscription]]:
    """Pause subscription

     Pause a subscription during the given time range. Only subscriptions with the same accounting period
    and term can be paused.

    Args:
        subscription_id (int):
        send_mail (Union[Unset, None, bool]):
        json_body (SubscriptionPauseAt):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResultBase, Subscription]
    """

    return (
        await asyncio_detailed(
            subscription_id=subscription_id,
            client=client,
            json_body=json_body,
            send_mail=send_mail,
        )
    ).parsed
