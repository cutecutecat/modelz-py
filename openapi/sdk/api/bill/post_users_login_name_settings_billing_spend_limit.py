from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.spend_limit import SpendLimit
from ...types import Response


def _get_kwargs(
    login_name: str,
    *,
    json_body: SpendLimit,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/users/{login_name}/settings/billing/spend_limit".format(
            login_name=login_name,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SpendLimit]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = SpendLimit.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SpendLimit]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    login_name: str,
    *,
    client: AuthenticatedClient,
    json_body: SpendLimit,
) -> Response[SpendLimit]:
    """Create spend limit

     Create spend limit

    Args:
        login_name (str):
        json_body (SpendLimit):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SpendLimit]
    """

    kwargs = _get_kwargs(
        login_name=login_name,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    login_name: str,
    *,
    client: AuthenticatedClient,
    json_body: SpendLimit,
) -> Optional[SpendLimit]:
    """Create spend limit

     Create spend limit

    Args:
        login_name (str):
        json_body (SpendLimit):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SpendLimit
    """

    return sync_detailed(
        login_name=login_name,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    login_name: str,
    *,
    client: AuthenticatedClient,
    json_body: SpendLimit,
) -> Response[SpendLimit]:
    """Create spend limit

     Create spend limit

    Args:
        login_name (str):
        json_body (SpendLimit):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SpendLimit]
    """

    kwargs = _get_kwargs(
        login_name=login_name,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    login_name: str,
    *,
    client: AuthenticatedClient,
    json_body: SpendLimit,
) -> Optional[SpendLimit]:
    """Create spend limit

     Create spend limit

    Args:
        login_name (str):
        json_body (SpendLimit):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SpendLimit
    """

    return (
        await asyncio_detailed(
            login_name=login_name,
            client=client,
            json_body=json_body,
        )
    ).parsed
