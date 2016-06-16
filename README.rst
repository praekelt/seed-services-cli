Seed Services command line interface
====================================

A command line interface for `Seed Services`_ HTTP APIs.

.. _Seed Services: https://github.com/praekelt?utf8=%E2%9C%93&query=seed


Installation
------------

Install with::

  $ pip install --user seed-services-cli

Then run::

  $ seed-services-cli --help

and read the usage instructions.


Configuration
----------------

The configuration can be passed in using a YAML file. An example is provided::

  hub:
    api_url: http://hub.example.org/api/v1
    token: TEMP
  identity_store:
    api_url: http://idstore.example.org/api/v1
    token: TEMP2

Then run the following to use::

  $ seed-services-cli --conf=config.yaml command-to-run



Finding identities
------------------

Run::

  $ seed-services-cli identity-search --help

to learn about the options available for searching.

Example search::

  $ seed-services-cli identity-search --address_type msisdn --address +27001


Developing
----------------

Run::

  $ pip install --editable .

Testing::

  $ pip install -r requirements-dev.txt
  $ py.test seed_services_cli



Reporting issues
----------------

Issues can be filed in the GitHub issue tracker. Please don't use the issue
tracker for general support queries.
