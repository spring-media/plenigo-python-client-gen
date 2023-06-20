import logging
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx
from tenacity import RetryError, retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

log = logging.getLogger(__name__)

import datetime
from typing import Dict, Optional, Union

from ...models.error_result_base import ErrorResultBase
from ...models.mail_log_entries import MailLogEntries
from ...models.search_mail_logs_mail_template_type import SearchMailLogsMailTemplateType
from ...models.search_mail_logs_sort import SearchMailLogsSort
from ...types import UNSET, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    size: Union[Unset, None, int] = UNSET,
    start_time: Union[Unset, None, datetime.datetime] = UNSET,
    end_time: Union[Unset, None, datetime.datetime] = UNSET,
    starting_after: Union[Unset, None, str] = UNSET,
    ending_before: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, SearchMailLogsSort] = UNSET,
    mail_template_type: Union[Unset, None, SearchMailLogsMailTemplateType] = UNSET,
    error_only: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/mails/logs".format(client.api.value)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["size"] = size

    json_start_time: Union[Unset, None, str] = UNSET
    if not isinstance(start_time, Unset):
        json_start_time = start_time.isoformat() if start_time else None

    params["startTime"] = json_start_time

    json_end_time: Union[Unset, None, str] = UNSET
    if not isinstance(end_time, Unset):
        json_end_time = end_time.isoformat() if end_time else None

    params["endTime"] = json_end_time

    params["startingAfter"] = starting_after

    params["endingBefore"] = ending_before

    json_sort: Union[Unset, None, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value if sort else None

    params["sort"] = json_sort

    json_mail_template_type: Union[Unset, None, str] = UNSET
    if not isinstance(mail_template_type, Unset):
        json_mail_template_type = mail_template_type.value if mail_template_type else None

    params["mailTemplateType"] = json_mail_template_type

    params["errorOnly"] = error_only

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[ErrorResultBase, MailLogEntries]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = MailLogEntries.from_dict(response.json())

        return response_200
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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[ErrorResultBase, MailLogEntries]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )  # type: ignore


def sync_all(
    *,
    client: AuthenticatedClient,
    size: Union[Unset, None, int] = UNSET,
    start_time: Union[Unset, None, datetime.datetime] = UNSET,
    end_time: Union[Unset, None, datetime.datetime] = UNSET,
    starting_after: Union[Unset, None, str] = UNSET,
    ending_before: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, SearchMailLogsSort] = UNSET,
    mail_template_type: Union[Unset, None, SearchMailLogsMailTemplateType] = UNSET,
    error_only: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[ErrorResultBase, MailLogEntries]]:
    all_results = MailLogEntries(items=[])  # type: ignore

    while True:
        try:
            results = sync_detailed(
                client=client,
                size=size,
                start_time=start_time,
                end_time=end_time,
                starting_after=starting_after,
                ending_before=ending_before,
                sort=sort,
                mail_template_type=mail_template_type,
                error_only=error_only,
            ).parsed

            if results and not isinstance(results, ErrorResultBase) and not isinstance(results.items, Unset):
                all_results.items.extend(results.items)  # type: ignore

                cursor = results.additional_properties.get("startingAfterId")

                if not cursor:
                    break

                starting_after = cursor
            else:
                break
        except RetryError:
            break

    return all_results


@retry(
    retry=retry_if_exception_type(errors.RetryableError),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=30),
)
def sync_detailed(
    *,
    client: AuthenticatedClient,
    size: Union[Unset, None, int] = UNSET,
    start_time: Union[Unset, None, datetime.datetime] = UNSET,
    end_time: Union[Unset, None, datetime.datetime] = UNSET,
    starting_after: Union[Unset, None, str] = UNSET,
    ending_before: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, SearchMailLogsSort] = UNSET,
    mail_template_type: Union[Unset, None, SearchMailLogsMailTemplateType] = UNSET,
    error_only: Union[Unset, None, bool] = UNSET,
) -> Response[Union[ErrorResultBase, MailLogEntries]]:
    """Search

     Search all mail log entries that correspond to the given search conditions.

    Args:
        size (Union[Unset, None, int]):
        start_time (Union[Unset, None, datetime.datetime]):
        end_time (Union[Unset, None, datetime.datetime]):
        starting_after (Union[Unset, None, str]):
        ending_before (Union[Unset, None, str]):
        sort (Union[Unset, None, SearchMailLogsSort]):
        mail_template_type (Union[Unset, None, SearchMailLogsMailTemplateType]):
        error_only (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResultBase, MailLogEntries]]
    """

    kwargs = _get_kwargs(
        client=client,
        size=size,
        start_time=start_time,
        end_time=end_time,
        starting_after=starting_after,
        ending_before=ending_before,
        sort=sort,
        mail_template_type=mail_template_type,
        error_only=error_only,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    size: Union[Unset, None, int] = UNSET,
    start_time: Union[Unset, None, datetime.datetime] = UNSET,
    end_time: Union[Unset, None, datetime.datetime] = UNSET,
    starting_after: Union[Unset, None, str] = UNSET,
    ending_before: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, SearchMailLogsSort] = UNSET,
    mail_template_type: Union[Unset, None, SearchMailLogsMailTemplateType] = UNSET,
    error_only: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[ErrorResultBase, MailLogEntries]]:
    """Search

     Search all mail log entries that correspond to the given search conditions.

    Args:
        size (Union[Unset, None, int]):
        start_time (Union[Unset, None, datetime.datetime]):
        end_time (Union[Unset, None, datetime.datetime]):
        starting_after (Union[Unset, None, str]):
        ending_before (Union[Unset, None, str]):
        sort (Union[Unset, None, SearchMailLogsSort]):
        mail_template_type (Union[Unset, None, SearchMailLogsMailTemplateType]):
        error_only (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResultBase, MailLogEntries]
    """

    return sync_detailed(
        client=client,
        size=size,
        start_time=start_time,
        end_time=end_time,
        starting_after=starting_after,
        ending_before=ending_before,
        sort=sort,
        mail_template_type=mail_template_type,
        error_only=error_only,
    ).parsed


@retry(
    retry=retry_if_exception_type(errors.RetryableError),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=30),
)
async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    size: Union[Unset, None, int] = UNSET,
    start_time: Union[Unset, None, datetime.datetime] = UNSET,
    end_time: Union[Unset, None, datetime.datetime] = UNSET,
    starting_after: Union[Unset, None, str] = UNSET,
    ending_before: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, SearchMailLogsSort] = UNSET,
    mail_template_type: Union[Unset, None, SearchMailLogsMailTemplateType] = UNSET,
    error_only: Union[Unset, None, bool] = UNSET,
) -> Response[Union[ErrorResultBase, MailLogEntries]]:
    """Search

     Search all mail log entries that correspond to the given search conditions.

    Args:
        size (Union[Unset, None, int]):
        start_time (Union[Unset, None, datetime.datetime]):
        end_time (Union[Unset, None, datetime.datetime]):
        starting_after (Union[Unset, None, str]):
        ending_before (Union[Unset, None, str]):
        sort (Union[Unset, None, SearchMailLogsSort]):
        mail_template_type (Union[Unset, None, SearchMailLogsMailTemplateType]):
        error_only (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResultBase, MailLogEntries]]
    """

    kwargs = _get_kwargs(
        client=client,
        size=size,
        start_time=start_time,
        end_time=end_time,
        starting_after=starting_after,
        ending_before=ending_before,
        sort=sort,
        mail_template_type=mail_template_type,
        error_only=error_only,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio_all(
    *,
    client: AuthenticatedClient,
    size: Union[Unset, None, int] = UNSET,
    start_time: Union[Unset, None, datetime.datetime] = UNSET,
    end_time: Union[Unset, None, datetime.datetime] = UNSET,
    starting_after: Union[Unset, None, str] = UNSET,
    ending_before: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, SearchMailLogsSort] = UNSET,
    mail_template_type: Union[Unset, None, SearchMailLogsMailTemplateType] = UNSET,
    error_only: Union[Unset, None, bool] = UNSET,
) -> Response[Union[ErrorResultBase, MailLogEntries]]:
    all_results = []

    while True:
        try:
            results = (
                await asyncio_detailed(
                    client=client,
                    size=size,
                    start_time=start_time,
                    end_time=end_time,
                    starting_after=starting_after,
                    ending_before=ending_before,
                    sort=sort,
                    mail_template_type=mail_template_type,
                    error_only=error_only,
                )
            ).parsed

            if results and not isinstance(results, ErrorResultBase) and not isinstance(results.items, Unset):
                all_results.items.extend(results.items)  # type: ignore

                cursor = results.additional_properties.get("startingAfterId")

                if not cursor:
                    break

                starting_after = cursor
            else:
                break
        except RetryError:
            break

    return all_results


async def asyncio(
    *,
    client: AuthenticatedClient,
    size: Union[Unset, None, int] = UNSET,
    start_time: Union[Unset, None, datetime.datetime] = UNSET,
    end_time: Union[Unset, None, datetime.datetime] = UNSET,
    starting_after: Union[Unset, None, str] = UNSET,
    ending_before: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, SearchMailLogsSort] = UNSET,
    mail_template_type: Union[Unset, None, SearchMailLogsMailTemplateType] = UNSET,
    error_only: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[ErrorResultBase, MailLogEntries]]:
    """Search

     Search all mail log entries that correspond to the given search conditions.

    Args:
        size (Union[Unset, None, int]):
        start_time (Union[Unset, None, datetime.datetime]):
        end_time (Union[Unset, None, datetime.datetime]):
        starting_after (Union[Unset, None, str]):
        ending_before (Union[Unset, None, str]):
        sort (Union[Unset, None, SearchMailLogsSort]):
        mail_template_type (Union[Unset, None, SearchMailLogsMailTemplateType]):
        error_only (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResultBase, MailLogEntries]
    """

    return (
        await asyncio_detailed(
            client=client,
            size=size,
            start_time=start_time,
            end_time=end_time,
            starting_after=starting_after,
            ending_before=ending_before,
            sort=sort,
            mail_template_type=mail_template_type,
            error_only=error_only,
        )
    ).parsed
