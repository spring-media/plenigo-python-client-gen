import logging
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_base_date import ApiBaseDate
from ...models.corporate_account_user_creation import CorporateAccountUserCreation
from ...models.error_result_base import ErrorResultBase
from ...types import UNSET, Response, Unset

log = logging.getLogger(__name__)


def _get_kwargs(
    customer_id: str,
    corporate_account_id: int,
    *,
    body: CorporateAccountUserCreation,
    send_mail: Union[Unset, bool] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["sendMail"] = send_mail

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/corporateAccounts/{customer_id}/{corporate_account_id}/users",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers

    log.debug(_kwargs)

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiBaseDate, ErrorResultBase]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = ApiBaseDate.from_dict(response.json())

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
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = ErrorResultBase.from_dict(response.json())

        return response_422
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
) -> Response[Union[ApiBaseDate, ErrorResultBase]]:
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
    customer_id: str,
    corporate_account_id: int,
    *,
    client: AuthenticatedClient,
    body: CorporateAccountUserCreation,
    send_mail: Union[Unset, bool] = UNSET,
) -> Response[Union[ApiBaseDate, ErrorResultBase]]:
    """Create

     Create a corporate account user for the given corporate account.

    Args:
        customer_id (str):
        corporate_account_id (int):
        send_mail (Union[Unset, bool]):
        body (CorporateAccountUserCreation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBaseDate, ErrorResultBase]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        corporate_account_id=corporate_account_id,
        body=body,
        send_mail=send_mail,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_id: str,
    corporate_account_id: int,
    *,
    client: AuthenticatedClient,
    body: CorporateAccountUserCreation,
    send_mail: Union[Unset, bool] = UNSET,
) -> Optional[Union[ApiBaseDate, ErrorResultBase]]:
    """Create

     Create a corporate account user for the given corporate account.

    Args:
        customer_id (str):
        corporate_account_id (int):
        send_mail (Union[Unset, bool]):
        body (CorporateAccountUserCreation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiBaseDate, ErrorResultBase]
    """

    return sync_detailed(
        customer_id=customer_id,
        corporate_account_id=corporate_account_id,
        client=client,
        body=body,
        send_mail=send_mail,
    ).parsed


@retry(
    retry=retry_if_exception_type(errors.RetryableError),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=30),
)
async def asyncio_detailed(
    customer_id: str,
    corporate_account_id: int,
    *,
    client: AuthenticatedClient,
    body: CorporateAccountUserCreation,
    send_mail: Union[Unset, bool] = UNSET,
) -> Response[Union[ApiBaseDate, ErrorResultBase]]:
    """Create

     Create a corporate account user for the given corporate account.

    Args:
        customer_id (str):
        corporate_account_id (int):
        send_mail (Union[Unset, bool]):
        body (CorporateAccountUserCreation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBaseDate, ErrorResultBase]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        corporate_account_id=corporate_account_id,
        body=body,
        send_mail=send_mail,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_id: str,
    corporate_account_id: int,
    *,
    client: AuthenticatedClient,
    body: CorporateAccountUserCreation,
    send_mail: Union[Unset, bool] = UNSET,
) -> Optional[Union[ApiBaseDate, ErrorResultBase]]:
    """Create

     Create a corporate account user for the given corporate account.

    Args:
        customer_id (str):
        corporate_account_id (int):
        send_mail (Union[Unset, bool]):
        body (CorporateAccountUserCreation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiBaseDate, ErrorResultBase]
    """

    return (
        await asyncio_detailed(
            customer_id=customer_id,
            corporate_account_id=corporate_account_id,
            client=client,
            body=body,
            send_mail=send_mail,
        )
    ).parsed
