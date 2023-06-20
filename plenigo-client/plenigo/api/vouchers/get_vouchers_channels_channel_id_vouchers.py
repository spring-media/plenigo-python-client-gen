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

from ...models.api_voucher_page import ApiVoucherPage
from ...models.error_result_base import ErrorResultBase
from ...models.get_vouchers_channels_channel_id_vouchers_voucher_status import (
    GetVouchersChannelsChannelIdVouchersVoucherStatus,
)
from ...types import UNSET, Unset


def _get_kwargs(
    channel_id: str,
    *,
    client: AuthenticatedClient,
    starting_after: Union[Unset, None, str] = UNSET,
    ending_before: Union[Unset, None, str] = UNSET,
    size: Union[Unset, None, int] = UNSET,
    voucher_status: Union[Unset, None, GetVouchersChannelsChannelIdVouchersVoucherStatus] = UNSET,
) -> Dict[str, Any]:
    url = "{}/vouchers/channels/{channelId}/vouchers".format(client.api.value, channelId=channel_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["startingAfter"] = starting_after

    params["endingBefore"] = ending_before

    params["size"] = size

    json_voucher_status: Union[Unset, None, str] = UNSET
    if not isinstance(voucher_status, Unset):
        json_voucher_status = voucher_status.value if voucher_status else None

    params["voucherStatus"] = json_voucher_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    kwargs = {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }

    log.debug(kwargs)

    return kwargs


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[ApiVoucherPage, ErrorResultBase]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiVoucherPage.from_dict(response.json())

        return response_200
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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[ApiVoucherPage, ErrorResultBase]]:
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
    channel_id: str,
    *,
    client: AuthenticatedClient,
    starting_after: Union[Unset, None, str] = UNSET,
    ending_before: Union[Unset, None, str] = UNSET,
    size: Union[Unset, None, int] = UNSET,
    voucher_status: Union[Unset, None, GetVouchersChannelsChannelIdVouchersVoucherStatus] = UNSET,
) -> Response[Union[ApiVoucherPage, ErrorResultBase]]:
    """Returns vouchers

     Returns all vouchers of the selected channel page, depending on query parameters

    Args:
        channel_id (str):
        starting_after (Union[Unset, None, str]):
        ending_before (Union[Unset, None, str]):
        size (Union[Unset, None, int]):
        voucher_status (Union[Unset, None, GetVouchersChannelsChannelIdVouchersVoucherStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiVoucherPage, ErrorResultBase]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        client=client,
        starting_after=starting_after,
        ending_before=ending_before,
        size=size,
        voucher_status=voucher_status,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    channel_id: str,
    *,
    client: AuthenticatedClient,
    starting_after: Union[Unset, None, str] = UNSET,
    ending_before: Union[Unset, None, str] = UNSET,
    size: Union[Unset, None, int] = UNSET,
    voucher_status: Union[Unset, None, GetVouchersChannelsChannelIdVouchersVoucherStatus] = UNSET,
) -> Optional[Union[ApiVoucherPage, ErrorResultBase]]:
    """Returns vouchers

     Returns all vouchers of the selected channel page, depending on query parameters

    Args:
        channel_id (str):
        starting_after (Union[Unset, None, str]):
        ending_before (Union[Unset, None, str]):
        size (Union[Unset, None, int]):
        voucher_status (Union[Unset, None, GetVouchersChannelsChannelIdVouchersVoucherStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiVoucherPage, ErrorResultBase]
    """

    return sync_detailed(
        channel_id=channel_id,
        client=client,
        starting_after=starting_after,
        ending_before=ending_before,
        size=size,
        voucher_status=voucher_status,
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
    starting_after: Union[Unset, None, str] = UNSET,
    ending_before: Union[Unset, None, str] = UNSET,
    size: Union[Unset, None, int] = UNSET,
    voucher_status: Union[Unset, None, GetVouchersChannelsChannelIdVouchersVoucherStatus] = UNSET,
) -> Response[Union[ApiVoucherPage, ErrorResultBase]]:
    """Returns vouchers

     Returns all vouchers of the selected channel page, depending on query parameters

    Args:
        channel_id (str):
        starting_after (Union[Unset, None, str]):
        ending_before (Union[Unset, None, str]):
        size (Union[Unset, None, int]):
        voucher_status (Union[Unset, None, GetVouchersChannelsChannelIdVouchersVoucherStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiVoucherPage, ErrorResultBase]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        client=client,
        starting_after=starting_after,
        ending_before=ending_before,
        size=size,
        voucher_status=voucher_status,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    channel_id: str,
    *,
    client: AuthenticatedClient,
    starting_after: Union[Unset, None, str] = UNSET,
    ending_before: Union[Unset, None, str] = UNSET,
    size: Union[Unset, None, int] = UNSET,
    voucher_status: Union[Unset, None, GetVouchersChannelsChannelIdVouchersVoucherStatus] = UNSET,
) -> Optional[Union[ApiVoucherPage, ErrorResultBase]]:
    """Returns vouchers

     Returns all vouchers of the selected channel page, depending on query parameters

    Args:
        channel_id (str):
        starting_after (Union[Unset, None, str]):
        ending_before (Union[Unset, None, str]):
        size (Union[Unset, None, int]):
        voucher_status (Union[Unset, None, GetVouchersChannelsChannelIdVouchersVoucherStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiVoucherPage, ErrorResultBase]
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            client=client,
            starting_after=starting_after,
            ending_before=ending_before,
            size=size,
            voucher_status=voucher_status,
        )
    ).parsed
