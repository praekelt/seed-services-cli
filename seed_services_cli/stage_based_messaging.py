import click

from client import StageBasedMessagingApiClient


def get_api_client(url, token):
    return StageBasedMessagingApiClient(
        api_url=url,
        auth_token=token
    )


@click.option(
    '--csv', type=click.File('wb+'),
    help=('Export schedules to the named file in CSV format. NOT SUPPORTED.'))
@click.option(
    '--json', type=click.File('wb+'),
    help=('Export schedules to the named file as new-line separated'
          ' JSON objects. NOT SUPPORTED.'))
@click.pass_context
def schedules(ctx, csv, json):
    """ List all schedules
    """
    api = get_api_client(ctx.obj.stage_based_messaging.api_url,
                         ctx.obj.stage_based_messaging.token)
    click.echo("Getting schedules")
    results = api.get_schedules()
    click.echo("Found %s results:" % results["count"])
    for result in results["results"]:
        click.echo("%s: %s %s %s %s %s (m/h/d/dM/MY)" % (
                   result["id"], result["minute"], result["hour"],
                   result["day_of_week"], result["day_of_month"],
                   result["month_of_year"]))


@click.option(
    '--csv', type=click.File('wb+'),
    help=('Export messagesets to the named file in CSV format.'
          ' NOT SUPPORTED.'))
@click.option(
    '--json', type=click.File('wb+'),
    help=('Export messagesets to the named file as new-line separated'
          ' JSON objects. NOT SUPPORTED.'))
@click.pass_context
def messagesets(ctx, csv, json):
    """ List all messagesets
    """
    api = get_api_client(ctx.obj.stage_based_messaging.api_url,
                         ctx.obj.stage_based_messaging.token)
    click.echo("Getting messagesets")
    results = api.get_messagesets()
    click.echo("Found %s results (id, short_name, content_type, next_set,"
               " default_schedule, notes):" % results["count"])
    for result in results["results"]:
        click.echo("%s,%s,%s,%s,%s,%s" % (
                   result["id"], result["short_name"], result["content_type"],
                   result["next_set"], result["default_schedule"],
                   result["notes"]))


@click.option(
    '--csv', type=click.File('wb+'),
    help=('Export messages to the named file in CSV format.'
          ' NOT SUPPORTED.'))
@click.option(
    '--json', type=click.File('wb+'),
    help=('Export messages to the named file as new-line separated'
          ' JSON objects. NOT SUPPORTED.'))
@click.option('--messageset', '-m', type=click.INT,
              help='Filter by Messageset')
@click.option('--lang', '-l', type=click.STRING, help='Filter by language')
@click.option('--seqno', '-s', type=click.INT,
              help='Filter by sequence number')
@click.pass_context
def messages(ctx, csv, json, messageset, lang, seqno):
    """ List all messages
    """
    api = get_api_client(ctx.obj.stage_based_messaging.api_url,
                         ctx.obj.stage_based_messaging.token)
    click.echo("Getting messages")
    params = {}
    if messageset:
        params["messageset"] = messageset
    if lang:
        params["lang"] = lang
    if seqno:
        params["sequence_number"] = seqno
    results = api.get_messages(params=params)
    click.echo("Found %s results (id, messageset, sequence_number, lang,"
               " text_content, binary_content):" % results["count"])
    for result in results["results"]:
        click.echo("%s,%s,%s,%s,\"%s\",%s" % (
                   result["id"], result["messageset"],
                   result["sequence_number"],
                   result["lang"], result["text_content"],
                   result["binary_content"]))
