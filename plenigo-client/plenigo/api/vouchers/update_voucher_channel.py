import logging
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

logger = logging.getLogger(__name__)

from ...models.api_channel import ApiChannel
from ...models.channel_update import ChannelUpdate
from ...models.error_result import ErrorResult
from ...models.error_result_base import ErrorResultBase
from ...models.success_status import SuccessStatus
from ...types import Unset


def _get_kwargs(
    channel_id: str,
    *,
    body: ChannelUpdate,
    callback: Union[Unset, bool] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["callback"] = callback

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/vouchers/channels/{channel_id}",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiChannel, ErrorResult, ErrorResultBase, SuccessStatus]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiChannel.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = SuccessStatus.from_dict(response.json())

        return response_202
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResult.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ErrorResultBase.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.PAYMENT_REQUIRED:
        response_402 = ErrorResult.from_dict(response.json())

        return response_402
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
) -> Response[Union[ApiChannel, ErrorResult, ErrorResultBase, SuccessStatus]]:
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
    channel_id: str,
    *,
    client: AuthenticatedClient,
    body: ChannelUpdate,
    callback: Union[Unset, bool] = UNSET,
) -> Response[Union[ApiChannel, ErrorResult, ErrorResultBase, SuccessStatus]]:
    """Update channel

     *ASYNC* Update channel that is identified by the passed channel id. ATTENTION - this process is
    async.

    Args:
        channel_id (str):
        callback (Union[Unset, bool]):
        body (ChannelUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiChannel, ErrorResult, ErrorResultBase, SuccessStatus]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        body=body,
        callback=callback,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    channel_id: str,
    *,
    client: AuthenticatedClient,
    body: ChannelUpdate,
    callback: Union[Unset, bool] = UNSET,
) -> Optional[Union[ApiChannel, ErrorResult, ErrorResultBase, SuccessStatus]]:
    """Update channel

     *ASYNC* Update channel that is identified by the passed channel id. ATTENTION - this process is
    async.

    Args:
        channel_id (str):
        callback (Union[Unset, bool]):
        body (ChannelUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiChannel, ErrorResult, ErrorResultBase, SuccessStatus]
    """

    return sync_detailed(
        channel_id=channel_id,
        client=client,
        body=body,
        callback=callback,
    ).parsed


@retry(
    retry=retry_if_exception_type(errors.RetryableError),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=30),
)
async def asyncio_detailed(
    channel_id: str,
    *,
    client: AuthenticatedClient,
    body: ChannelUpdate,
    callback: Union[Unset, bool] = UNSET,
) -> Response[Union[ApiChannel, ErrorResult, ErrorResultBase, SuccessStatus]]:
    """Update channel

     *ASYNC* Update channel that is identified by the passed channel id. ATTENTION - this process is
    async.

    Args:
        channel_id (str):
        callback (Union[Unset, bool]):
        body (ChannelUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiChannel, ErrorResult, ErrorResultBase, SuccessStatus]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        body=body,
        callback=callback,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    channel_id: str,
    *,
    client: AuthenticatedClient,
    body: ChannelUpdate,
    callback: Union[Unset, bool] = UNSET,
) -> Optional[Union[ApiChannel, ErrorResult, ErrorResultBase, SuccessStatus]]:
    """Update channel

     *ASYNC* Update channel that is identified by the passed channel id. ATTENTION - this process is
    async.

    Args:
        channel_id (str):
        callback (Union[Unset, bool]):
        body (ChannelUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiChannel, ErrorResult, ErrorResultBase, SuccessStatus]
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            client=client,
            body=body,
            callback=callback,
        )
    ).parsed
