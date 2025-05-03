import os

from cloudflare import Cloudflare
from dotenv import load_dotenv

load_dotenv()

cloudflare_token = os.getenv("CLOUDFLARE_API_TOKEN", "")
tunnel_id = os.getenv("TUNNEL_ID", "")
account_id = os.getenv("ACCOUNT_ID", "")
zone_id = os.getenv("ZONE_ID", "")


cf = Cloudflare(api_token=cloudflare_token)


def update_public_url(new_name, name):
    dns_record_id = cf.dns.records.list(zone_id=zone_id, search=name).result[0].id
    cf.dns.records.update(
        dns_record_id=dns_record_id,
        zone_id=zone_id,
        name=new_name,
        type="CNAME",
        content=f"{tunnel_id}.cfargotunnel.com",
        proxied=True,
    )

    tunnel = cf.zero_trust.tunnels.cloudflared.configurations.get(
        tunnel_id=tunnel_id, account_id=account_id
    )

    if tunnel is None:
        return
    if tunnel.config is None:
        return
    if tunnel.config.ingress is None:
        return

    ingress = tunnel.config.ingress
    fallback = ingress.pop()

    updated_ingress = []
    for public_hostname in ingress:
        if public_hostname.hostname != f"{name}.tysonjenkins.dev":
            updated_ingress.append(public_hostname)

    updated_ingress.append(
        {
            "hostname": f"{new_name}.tysonjenkins.dev",
            "service": f"https://{new_name}.home.tysonjenkins.dev",
        }
    )

    updated_ingress.append(fallback)
    data = {"config": {"ingress": updated_ingress}}

    cf.zero_trust.tunnels.cloudflared.configurations.update(
        tunnel_id=tunnel_id, account_id=account_id, **data
    )


def delete_public_url(name):
    try:
        dns_record_id = cf.dns.records.list(zone_id=zone_id, search=name).result[0].id

        cf.dns.records.delete(
            zone_id=zone_id,
            dns_record_id=dns_record_id,
        )

        tunnel = cf.zero_trust.tunnels.cloudflared.configurations.get(
            account_id=account_id,
            tunnel_id=tunnel_id,
        )

        if tunnel is None:
            return
        if tunnel.config is None:
            return
        if tunnel.config.ingress is None:
            return

        ingress = tunnel.config.ingress
        fallback = ingress.pop()

        updated_ingress = []
        for public_hostname in ingress:
            if public_hostname.hostname != f"{name}.tysonjenkins.dev":
                updated_ingress.append(public_hostname)

        updated_ingress.append(fallback)

        data = {"config": {"ingress": updated_ingress}}

        cf.zero_trust.tunnels.cloudflared.configurations.update(
            tunnel_id=tunnel_id,
            account_id=account_id,
            **data,
        )

    except NameError:
        print(NameError)


def create_public_url(name):
    try:
        tunnel = cf.zero_trust.tunnels.cloudflared.configurations.get(
            account_id=account_id,
            tunnel_id=tunnel_id,
        )

        if tunnel is None:
            return
        if tunnel.config is None:
            return
        if tunnel.config.ingress is None:
            return

        ingress = tunnel.config.ingress
        fallback = ingress.pop()

        ingress.append(
            {
                "hostname": f"{name}.tysonjenkins.dev",
                "service": f"https://{name}.home.tysonjenkins.dev",
            }
        )
        ingress.append(fallback)

        data = {"config": {"ingress": ingress}}

        cf.zero_trust.tunnels.cloudflared.configurations.update(
            tunnel_id=tunnel_id, account_id=account_id, **data
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
