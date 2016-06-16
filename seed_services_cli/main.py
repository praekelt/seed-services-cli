from __future__ import print_function
import click
import click_config

import seed_services_cli.identity_store


class config(object):
    class hub(object):
        api_url = 'http://hub.fqdn/api/v1'
        token = 'REPLACEME'

    class identity_store(object):
        api_url = 'http://id.example.org/api/v1'
        token = 'REPLACEME'


@click.group(name="seed-services-cli")
@click.version_option()
@click_config.wrap(module=config, sections=('hub', 'identity_store'))
@click.pass_context
def cli(ctx):
    """ Seed Services command line utility. """
    ctx.obj = config

cli.command('identity-search')(seed_services_cli.identity_store.search)
