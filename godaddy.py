#!/usr/bin/env python

import logging
import pif
import pygodaddy

logging.basicConfig(filename='godaddy.log', format='%(asctime)s %(message)s', level=logging.INFO)
GODADDY_USERNAME="INSERT_USERNAME_HERE"
GODADDY_PASSWORD="INSERT_PASSWORD_HERE"
client = pygodaddy.GoDaddyClient()
client.login(GODADDY_USERNAME, GODADDY_PASSWORD)

for domain in client.find_domains():
    dns_records = client.find_dns_records(domain)
    public_ip = pif.get_public_ip()
    logging.debug("Domain '{0}' DNS records: {1}".format(domain, dns_records))
    if public_ip != dns_records[0].value:
        client.update_dns_record(domain, public_ip)
        logging.info("Domain '{0}' public IP set to '{1}'".format(domain, public_ip))
