import os

from cloudflare import Cloudflare
from dotenv import load_dotenv

# fix retrieving record ids for deletion

load_dotenv()

cloudflare_token = os.getenv("CLOUDFLARE_API_TOKEN")
tunnel_id = os.getenv("TUNNEL_ID")
account_id = os.getenv("ACCOUNT_ID")
zone_id = os.getenv("ZONE_ID")


cf = Cloudflare(api_token=cloudflare_token)


def delete_public_url(name):
    try:
        config = cf.zero_trust.tunnels.cloudflared.configurations.get(
            account_id=account_id,
            tunnel_id=tunnel_id,
        )

        ingress = []
        for public_hostname in config.config.ingress:
            if (
                public_hostname.hostname != None
                and public_hostname.hostname != f"{name}.tysonjenkins.dev"
            ):
                ingress.append(public_hostname)

        ingress.append({"service": "http_status:404"})

        new_config = {"config": {"ingress": ingress}}

        cf.zero_trust.tunnels.cloudflared.configurations.update(
            tunnel_id=tunnel_id,
            account_id=account_id,
            **new_config,
        )

        dns_records = cf.dns.records.list(zone_id=zone_id)
        dns_record_id = ""
        for record in dns_records:
            if record.name == f"{name}.tysonjenkins.dev":
                dns_record_id = record.id
                break

        cf.dns.records.delete(
            zone_id=zone_id,
            dns_record_id=dns_record_id,
        )
    except NameError:
        print(NameError)


def create_public_url(name):
    try:
        config = cf.zero_trust.tunnels.cloudflared.configurations.get(
            account_id=account_id,
            tunnel_id=tunnel_id,
        )

        ingress = []
        for public_hostname in config.config.ingress:
            if public_hostname.hostname != None:
                ingress.append(public_hostname)

        ingress.append(
            {
                "hostname": f"{name}.tysonjenkins.dev",
                "service": f"https://{name}.home.tysonjenkins.dev",
            }
        )

        ingress.append({"service": "http_status:404"})

        new_config = {"config": {"ingress": ingress}}

        cf.zero_trust.tunnels.cloudflared.configurations.update(
            tunnel_id=tunnel_id,
            account_id=account_id,
            **new_config,
        )

        cf.dns.records.create(
            zone_id=zone_id,
            name=name,
            type="CNAME",
            content=f"{tunnel_id}.cfargotunnel.com",
            proxied=True,
        )
    except NameError:
        print(NameError)
