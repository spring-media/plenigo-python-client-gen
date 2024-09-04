import logging
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.customer_google_sso_authentication import CustomerGoogleSsoAuthentication
from ...models.customer_session_token import CustomerSessionToken
from ...models.error_result import ErrorResult
from ...models.error_result_base import ErrorResultBase
from ...models.next_step import NextStep
from ...models.session_limit_reached import SessionLimitReached
from ...types import Response

log = logging.getLogger(__name__)


def _get_kwargs(
    *,
    body: CustomerGoogleSsoAuthentication,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/processes/ssoProvider/verify",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers

    log.debug(_kwargs)

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CustomerSessionToken, ErrorResult, ErrorResultBase, Union["NextStep", "SessionLimitReached"]]]:
    if response.status_code == HTTPStatus.OK:

        def _parse_response_200(data: object) -> Union["NextStep", "SessionLimitReached"]:
            # Try to parse the data as NextStep
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = NextStep.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass

            # In order to parse the one remaining property in the union,
            # data must be a dict
            if not isinstance(data, dict):
                raise TypeError()

            # Finally, parse the data as SessionLimitReached
            response_200_type_1 = SessionLimitReached.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = CustomerSessionToken.from_dict(response.json())

        return response_202
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResult.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ErrorResult.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorResultBase.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.PRECONDITION_FAILED:
        response_412 = ErrorResult.from_dict(response.json())

        return response_412
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
) -> Response[Union[CustomerSessionToken, ErrorResult, ErrorResultBase, Union["NextStep", "SessionLimitReached"]]]:
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
    client: Union[AuthenticatedClient, Client],
    body: CustomerGoogleSsoAuthentication,
) -> Response[Union[CustomerSessionToken, ErrorResult, ErrorResultBase, Union["NextStep", "SessionLimitReached"]]]:
    """Verify sso login

     This functionality verifies the log in data of a customer over a sso provider and executes the log
    in. The caller must decide if a
    customer name or email address is provided for login. If both are provided only the email address
    will be used.

    Args:
        body (CustomerGoogleSsoAuthentication):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CustomerSessionToken, ErrorResult, ErrorResultBase, Union['NextStep', 'SessionLimitReached']]]
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
    client: Union[AuthenticatedClient, Client],
    body: CustomerGoogleSsoAuthentication,
) -> Optional[Union[CustomerSessionToken, ErrorResult, ErrorResultBase, Union["NextStep", "SessionLimitReached"]]]:
    """Verify sso login

     This functionality verifies the log in data of a customer over a sso provider and executes the log
    in. The caller must decide if a
    customer name or email address is provided for login. If both are provided only the email address
    will be used.

    Args:
        body (CustomerGoogleSsoAuthentication):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CustomerSessionToken, ErrorResult, ErrorResultBase, Union['NextStep', 'SessionLimitReached']]
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
    client: Union[AuthenticatedClient, Client],
    body: CustomerGoogleSsoAuthentication,
) -> Response[Union[CustomerSessionToken, ErrorResult, ErrorResultBase, Union["NextStep", "SessionLimitReached"]]]:
    """Verify sso login

     This functionality verifies the log in data of a customer over a sso provider and executes the log
    in. The caller must decide if a
    customer name or email address is provided for login. If both are provided only the email address
    will be used.

    Args:
        body (CustomerGoogleSsoAuthentication):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CustomerSessionToken, ErrorResult, ErrorResultBase, Union['NextStep', 'SessionLimitReached']]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CustomerGoogleSsoAuthentication,
) -> Optional[Union[CustomerSessionToken, ErrorResult, ErrorResultBase, Union["NextStep", "SessionLimitReached"]]]:
    """Verify sso login

     This functionality verifies the log in data of a customer over a sso provider and executes the log
    in. The caller must decide if a
    customer name or email address is provided for login. If both are provided only the email address
    will be used.

    Args:
        body (CustomerGoogleSsoAuthentication):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CustomerSessionToken, ErrorResult, ErrorResultBase, Union['NextStep', 'SessionLimitReached']]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
