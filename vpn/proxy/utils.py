from urllib.parse import urlparse, urlunparse
from django.urls import reverse
from .models import Site, VpnUsageStat
from bs4 import BeautifulSoup



def get_original_url(response, site_name, routes_on_original_site):

    parsed_url = urlparse(routes_on_original_site)
    cleaned_url = urlunparse((parsed_url.scheme, parsed_url.netloc, '', '', '', ''))
    soup = BeautifulSoup(response.content, 'html.parser')

    for a_tag in soup.find_all('a', href=True):
        original_href = a_tag['href']
        parsed_original_href = urlparse(original_href)
        cleaned_original_href = urlunparse((parsed_original_href.scheme, parsed_original_href.netloc, '', '', '', ''))

        if cleaned_url != cleaned_original_href and cleaned_original_href.strip():
            ...
        else:
            new_href = reverse('proxy:proxy_view', args=[site_name, (cleaned_url + original_href)])
            a_tag['href'] = new_href


    for a_tag in soup.find_all('link', href=True):
        original_href = a_tag['href']
        parsed_original_href = urlparse(original_href)

        cleaned_original_href = urlunparse((parsed_original_href.scheme, parsed_original_href.netloc, '', '', '', ''))

        if cleaned_url == cleaned_original_href and cleaned_original_href.strip() or cleaned_url != cleaned_original_href and cleaned_original_href.strip():
            ...
        else:
            new_href = cleaned_url + original_href
            a_tag['href'] = new_href



    for img_tag in soup.find_all('img', src=True):
        original_src = img_tag['src']
        parsed_original_src = urlparse(original_src)
        print(original_src)
        cleaned_original_src = urlunparse((parsed_original_src.scheme, parsed_original_src.netloc, '', '', '', ''))

        if cleaned_url != cleaned_original_src and cleaned_original_src.strip():
            ...
        else:
            new_src = cleaned_url + original_src
            img_tag['src'] = new_src

    return soup



def traffic_count(request, site_name, original_size, modified_size):
    vpn_stat, created = VpnUsageStat.objects.get_or_create(
        user=request.user,
        site_name=site_name,
        defaults={'page_transitions': 0, 'data_volume_sent': 0, 'data_volume_received': 0}
    )
    vpn_stat.page_transitions += 1
    vpn_stat.data_volume_sent += original_size
    vpn_stat.data_volume_received += modified_size
    vpn_stat.save()
    return None