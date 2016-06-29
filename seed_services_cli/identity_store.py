import click
import json

from client import IdentityStoreApiClient
from demands import HTTPServiceError


def get_api_client(url, token):
    return IdentityStoreApiClient(
        api_url=url,
        auth_token=token
    )


@click.option(
    '--address_type', '-t',
    help='Address Type (e.g. msisdn)')
@click.option(
    '--address', '-a',
    help='Address (e.g. 27812345678)')
@click.pass_context
def search(ctx, address_type, address):
    """ Find an identity
    """
    api = get_api_client(ctx.obj.identity_store.api_url,
                         ctx.obj.identity_store.token)
    if not all((address_type, address)):
        raise click.UsageError(
            "Please specify address type and address. See --help.")
    click.echo("Looking for %s of %s." % (address_type, address))
    results = api.get_identity_by_address(address_type, address)
    click.echo("Found %s results:" % results["count"])
    if results["count"] > 0:
        for result in results["results"]:
            click.echo(result["id"])


@click.option(
    '--identity', '-i',
    help='Identity UUID')
@click.pass_context
def get_identity(ctx, identity):
    """ Find a specific identity
    """
    api = get_api_client(ctx.obj.identity_store.api_url,
                         ctx.obj.identity_store.token)
    if identity:
        # get a very particular identity
        try:
            result = api.get_identity(identity_id=identity)
        except HTTPServiceError:
            click.echo("Identity not found")
            ctx.abort()
    else:
        raise click.UsageError(
            "Please specify identity UUID. See --help.")
    click.echo(json.dumps(result))
