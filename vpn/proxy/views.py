from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Site, VpnUsageStat
from .forms import SiteForm
from .utils import get_original_url, traffic_count
import requests
from django.http import HttpResponse

from django.shortcuts import get_object_or_404


@login_required
def create_site(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            site = form.save(commit=False)
            site.user_site = request.user
            site.save()
            return redirect('proxy:view_sites')
    else:
        form = SiteForm()

    return render(request, 'proxy/create_site.html', {'form': form})


@login_required
def view_sites(request):
    sites = Site.objects.filter(user_site=request.user)
    return render(request, 'proxy/view_sites.html', {'sites': sites})

@login_required
def update_site(request, site_id):
    site = get_object_or_404(Site, id=site_id, user_site=request.user)

    if request.method == 'POST':
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect('proxy:view_sites')
    else:
        form = SiteForm(instance=site)

    return render(request, 'proxy/update.html', {'form': form, 'site': site})


@login_required
def site_detail(request, site_id):
    site = get_object_or_404(Site, id=site_id, user_site=request.user)

    print("User:", request.user)
    print("Site Name:", site.name)

    vpn_usage_stat = VpnUsageStat.objects.filter(user=request.user, site_name=site.name).first()

    print("VpnUsageStat:", vpn_usage_stat)

    return render(request, 'proxy/detail.html', {'site': site, 'vpn_usage_stat': vpn_usage_stat})



@login_required
def proxy_view(request, site_name, routes_on_original_site):
    response = requests.get(routes_on_original_site)
    soup = get_original_url(response, site_name, routes_on_original_site)

    original_content = response.content
    modified_content = soup.prettify().encode()
    original_url = soup.prettify()

    traffic_count(request, site_name, len(original_content), len(modified_content))


    return HttpResponse(original_url, content_type=response.headers['content-type'])



def site_statistics(request):
    sites_with_stats = []

    user_sites = Site.objects.filter(user_site=request.user)

    for site in user_sites:
        vpn_stat = VpnUsageStat.objects.filter(user=request.user, site_name=site.name).first()
        sites_with_stats.append({
            'site': site,
            'stat': vpn_stat
        })

    return render(request, 'proxy/statistics.html', {'sites_with_stats': sites_with_stats})
