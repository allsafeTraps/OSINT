

import requests
import argparse
from colored import fg, bg

API_KEY = "YOUR API KEY"
URL_API_SECURITY_TRAILS = "https://api.securitytrails.com/v1/"
HEADERS_API_SECURITY_TRAILS = {"Accept": "application/json", "user-agent": "trapsteo_milongas", "apikey": API_KEY}
COLOR = fg('#c0c0c0') + bg('#00005f')



def functionCallMethod():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--ping",  action='store_true', help="Request to ping method of securitytrails api")
    parser.add_argument("-u", "--usage", action='store_true', help="Request to usage method of securitytrails api")
    parser.add_argument("-s", "--scroll",type = str, help="Request to scroll method of securitytrails api")
    parser.add_argument("-c", "--company",type = str, help="Request to company method of securitytrails api")
    parser.add_argument("-a", "--associate",type = str, help="Request to company Associated IPs method of securitytrails api")
    parser.add_argument("-d", "--domain",type = str, help="Request to details domain method of securitytrails api")
    parser.add_argument("-su", "--subdomain",type = str, help="Request to details subdomain method of securitytrails api")
    parser.add_argument("-t", "--tags",type = str, help="Request to details tags method of securitytrails api")
    parser.add_argument("-w", "--whois",type = str, help="Request to details whois method of securitytrails api")
    parser.add_argument("-ad", "--associatedDomains",type = str, help="Request to details associated domains method of securitytrails api")
    parser.add_argument("-ssl", "--certificate",type = str, help="Request to details certificate domains method of securitytrails api")
    parser.add_argument("-ssl_stream", "--certificate_stream",type = str, help="Request to details certificate stream domains method of securitytrails api")
    parser.add_argument("-dns", "--dns_history",type = str, help="Request to details dns domains method of securitytrails api")
    parser.add_argument("-whois_h", "--whois_history",type = str, help="Request to details whois history domains method of securitytrails api")
    parser.add_argument("-ip", "--ip_neighbors",type = str, help="Request to details ip neighbors history domains method of securitytrails api")
    parser.add_argument("-dsl", "--dsl",type = str, help="Request to dsl domains method of securitytrails api")
    parser.add_argument("-stat", "--statistics",type = str, help="Request to statistics domains method of securitytrails api")
    parser.add_argument("-ipWhois", "--ip_whois",type = str, help="Request to ip whois statistics domains method of securitytrails api")
    parser.add_argument("-ipUserAgent", "--ip_user_agent",type = str, help="Request to user agent ip method of securitytrails api")
    parser.add_argument("-feeds", "--feeds_domain",type = str, help="Values (all, deleted, new, registered)")
    parser.add_argument("-dmarc", "--feeds_dmarc",type = str, help="Values (all, new)")
    parser.add_argument("-feeds_subdomain", "--feeds_subdomain",type = str, help="Values (all, deleted, new)")

    
    args = parser.parse_args()
    
    if args.ping:
        secTrailsApiPingMethod()
    elif args.usage:
        secTrailsApiUsageMethod()
    elif args.scroll:
        secTrailsApiScrollMethod(args.scroll)
    elif args.company:
        secTrailsApiCompanyDetailsMethod(args.company)
    elif args.associate:
        secTrailsApiCompanyAssociatedIpsDetailsMethod(args.associate)
    elif args.domain:
        secTrailsApiDomainAssociatedIpsDetailsMethod(args.domain)
    elif args.subdomain:
        secTrailsApiSubDomainAssociatedIpsDetailsMethod(args.subdomain)
    elif args.tags:
        secTrailsApiTagsDomainAssociatedIpsDetailsMethod(args.tags)
    elif args.whois:
        secTrailsApiWhoisDomainAssociatedIpsDetailsMethod(args.whois)
    elif args.associatedDomains:
        secTrailsApiAssociatedDomainAssociatedDetailsMethod(args.associatedDomains)
    elif args.certificate:
        secTrailsApisslCertificateDomainAssociatedDetailsMethod(args.certificate)
    elif args.certificate_stream:
        secTrailsApisslStreamCertificateDomainAssociatedDetailsMethod(args.certificate_stream)
    elif args.dns_history:
        secTrailsApiDNSDomainAssociatedDetailsMethod(args.dns_history)
    elif args.whois_history:
        secTrailsApiWHoisHistoryDomainAssociatedDetailsMethod(args.whois_history)
    elif args.ip_neighbors:
        secTrailsApiIpNeighborsMethod(args.ip_neighbors)
    elif args.dsl:
        secTrailsApiIpDSLMethod(args.dsl)
    elif args.statistics:
        secTrailsApiIpStatisticsMethod(args.statistics)
    elif args.ip_whois:
        secTrailsApiIpWhoisMethod(args.ip_whois)
    elif args.ip_user_agent:
        secTrailsApiUserAgentMethod(args.ip_user_agent)
    elif args.feeds_domain:
        secTrailsApiFeedstMethod(args.feeds_domain)
    elif args.feeds_dmarc:
        secTrailsApiDMARCtMethod(args.feeds_dmarc)
    elif args.feeds_subdomain:
        secTrailsApiSubdomainsDowloadCtMethod(args.feeds_subdomain)
    else:
        print(COLOR + "usage: SecurityTrailsApi.py [-h] for to select correct method")
    

#You can use this simple endpoint to test your authentication and access to the SecurityTrails API
def secTrailsApiPingMethod():
    
    try:
        
        ping = "ping"
        response = requests.request("GET", URL_API_SECURITY_TRAILS + "%s" % ping, headers=HEADERS_API_SECURITY_TRAILS)
            
        print(COLOR + response.text)
                        
    except Exception as inst:
        print(type(inst))    
        print(inst.args)     
        print(inst)
        

#Usage statistics of the API for the current month
def secTrailsApiUsageMethod():
    
    try:
        
        usage = "account/usage"
        response = requests.request("GET", URL_API_SECURITY_TRAILS + "%s" % usage, headers=HEADERS_API_SECURITY_TRAILS)
            
        print(COLOR +response.text)
                        
    except Exception as inst:
        print(type(inst))    
        print(inst.args)     
        print(inst)
    

#A fast and easy way to fetch many results. Currently only available for the DSL API endpoints.
def secTrailsApiScrollMethod(scroll_id):
    
    try:
        
        scroll = "scroll/%s" % scroll_id
        response = requests.request("GET", URL_API_SECURITY_TRAILS + "%s" % scroll, headers=HEADERS_API_SECURITY_TRAILS)
            
        print(COLOR + response.text)
                        
    except Exception as inst:
        print(type(inst))    
        print(inst.args)     
        print(inst)

#Returns details for a company domain.
#Necessary Upgrade Package  
def secTrailsApiCompanyDetailsMethod(company):
    
    try:
        
        domain = "company/%s" % company
        response = requests.request("GET", URL_API_SECURITY_TRAILS + "%s" % domain, headers=HEADERS_API_SECURITY_TRAILS)
            
        print(COLOR + response.text)
                        
    except Exception as inst:
        print(type(inst))    
        print(inst.args)     
        print(inst)
        
        
#Returns associated IPs for a company domain. The result is not paginated nor limited. The data is based on whois data with the names matched to the domains.
#Necessary Upgrade Package.
def secTrailsApiCompanyAssociatedIpsDetailsMethod(company):
    
    try:
        
        domain = "company/%s/associated-ips" % company
        response = requests.request("GET", URL_API_SECURITY_TRAILS + "%s" % domain, headers=HEADERS_API_SECURITY_TRAILS)
            
        print(COLOR +response.text)
                        
    except Exception as inst:
        print(type(inst))    
        print(inst.args)     
        print(inst)

#Returns the current data about the given hostname. In addition to the current data, you also get the current statistics associated with a particular record. For example, for a records you'll get how many other hostnames have the same IP.
def secTrailsApiDomainAssociatedIpsDetailsMethod(domain):
    
    try:
        
        domainName = "domain/%s" % domain
        response = requests.request("GET", URL_API_SECURITY_TRAILS + "%s" % domainName, headers=HEADERS_API_SECURITY_TRAILS)
            
        print(COLOR + response.text)
                        
    except Exception as inst:
        print(type(inst))    
        print(inst.args)     
        print(inst)

#Returns child and sibling subdomains for a given hostname. Limited to 2000 results for the Free plan and to 10000 for all paid subscriptions.
def secTrailsApiSubDomainAssociatedIpsDetailsMethod(domain):
    
    try:
        
        subDomainName = "domain/%s/subdomains" % domain
        response = requests.request("GET", URL_API_SECURITY_TRAILS + "%s" % subDomainName, headers=HEADERS_API_SECURITY_TRAILS)
            
        print(COLOR + response.text)
                        
    except Exception as inst:
        print(type(inst))    
        print(inst.args)     
        print(inst)

#Returns tags for a given hostname
def secTrailsApiTagsDomainAssociatedIpsDetailsMethod(domain):
    
    try:
        
        tags = "domain/%s/tags" % domain
        response = requests.request("GET", URL_API_SECURITY_TRAILS + "%s" % tags, headers=HEADERS_API_SECURITY_TRAILS)
            
        print(COLOR + response.text)
                        
    except Exception as inst:
        print(type(inst))    
        print(inst.args)     
        print(inst)

#Returns the current WHOIS data about a given hostname with the stats merged together.
#Necessary Upgrade Package  
def secTrailsApiWhoisDomainAssociatedIpsDetailsMethod(domain):
    
    try:
        
        whois = "domain/%s/whois" % domain
        response = requests.request("GET", URL_API_SECURITY_TRAILS + "%s" % whois, headers=HEADERS_API_SECURITY_TRAILS)
            
        print(COLOR + response.text)
                        
    except Exception as inst:
        print(type(inst))    
        print(inst.args)     
        print(inst)

#Find all domains that are related to a hostname you input. Limited to 10000 results.
#Necessary Upgrade Package  
def secTrailsApiAssociatedDomainAssociatedDetailsMethod(domain):
  
    try:
        
        associated = "domain/%s/associated" % domain
        response = requests.request("GET", URL_API_SECURITY_TRAILS + "%s" % associated, headers=HEADERS_API_SECURITY_TRAILS)
            
        print(COLOR + response.text)
                        
    except Exception as inst:
        print(type(inst))    
        print(inst.args)     
        print(inst)

#Fetch current and historical certificate information for any hostname. Limited to 10000 results.
#Necessary Upgrade Package  
def secTrailsApisslCertificateDomainAssociatedDetailsMethod(domain):
  
    try:
        
        ssl = "domain/%s/ssl" % domain
        
        querystring = {"include_subdomains":"true","status":"valid"}
        response = requests.request("GET", URL_API_SECURITY_TRAILS + "%s" % ssl, params = querystring, headers=HEADERS_API_SECURITY_TRAILS)
        
        print(COLOR + response.text)
                        
    except Exception as inst:
        print(type(inst))    
        print(inst.args)     
        print(inst)

#Fetch current and historical certificate information for any hostname. Returns all results.
#Necessary Upgrade Package  
def secTrailsApisslStreamCertificateDomainAssociatedDetailsMethod(domain):
  
    try:
        
        sslStream = "domain/%s/ssl_stream" % domain
        
        querystring = {"include_subdomains":"true","status":"valid"}
        response = requests.request("GET", URL_API_SECURITY_TRAILS + "%s" % sslStream, params = querystring, headers=HEADERS_API_SECURITY_TRAILS)
        
        print(COLOR + response.text)
                        
    except Exception as inst:
        print(type(inst))    
        print(inst.args)     
        print(inst)

#Lists out specific historical information about the given hostname parameter. In addition of fetching the historical data for a particular type, the count statistic is returned as well, which represents the number of that particular resource against current data. (a records will have an ip_count field which will represent the number of records that has the same IP as that particular record) The results are sorted first_seen descending. The number of results is not limited.
def secTrailsApiDNSDomainAssociatedDetailsMethod(domain):
  
    try:
        
        dnsHistory = "history/%s/dns/a" % domain
        
        response = requests.request("GET", URL_API_SECURITY_TRAILS + "%s" % dnsHistory, headers=HEADERS_API_SECURITY_TRAILS)
        
        print(COLOR + response.text)
                        
    except Exception as inst:
        print(type(inst))    
        print(inst.args)     
        print(inst)



#Returns historical WHOIS information about the given domain. The number of results is not limited.
def secTrailsApiWHoisHistoryDomainAssociatedDetailsMethod(domain):
  
    try:
        
        whoisHistory = "history/%s/whois" % domain
        
        response = requests.request("GET", URL_API_SECURITY_TRAILS + "%s" % whoisHistory, headers=HEADERS_API_SECURITY_TRAILS)
        
        print(COLOR + response.text)
                        
    except Exception as inst:
        print(type(inst))    
        print(inst.args)     
        print(inst)


#Returns the neighbors in any given IP level range and essentially allows you to explore closeby IP addresses. It will divide the range into 16 groups. Example: a /28 would be divided into 16 /32 blocks or a /24 would be divided into 16 /28 blocks
def secTrailsApiIpNeighborsMethod(ip):
  
    try:
        
        ipNeighbors = "ips/nearby/%s" % ip
        
        response = requests.request("GET", URL_API_SECURITY_TRAILS + "%s" % ipNeighbors, headers=HEADERS_API_SECURITY_TRAILS)
        
        print(COLOR + response.text)
                        
    except Exception as inst:
        print(type(inst))    
        print(inst.args)     
        print(inst)
        
        
#Search for IP addresses. A maximum of 10000 results can be retrieved.
#Necessary Upgrade Package 
def secTrailsApiIpDSLMethod(domain):
  
    try:
        
        ipDsl = "ips/list" 
        
        payload = {"query": "ptr_part = '%s'" % domain}
        
        response = requests.request("POST", URL_API_SECURITY_TRAILS + "%s" % ipDsl, json = payload, headers=HEADERS_API_SECURITY_TRAILS)
        
        print(COLOR + response.text)
                        
    except Exception as inst:
        print(type(inst))    
        print(inst.args)     
        print(inst)

#Statistics like Reverse DNS pattern identification (RDNS entries are grouped and displayed as x), ports (number of open ports found) or total results are returned
#Necessary Upgrade Package 
def secTrailsApiIpStatisticsMethod(domain):
  
    try:
        
        stats = "ips/stats" 
        
        payload = {"query": "ptr_part = '%s'" % domain}
        
        response = requests.request("POST", URL_API_SECURITY_TRAILS + "%s" % stats, json = payload, headers=HEADERS_API_SECURITY_TRAILS)
        
        print(COLOR + response.text)
                        
    except Exception as inst:
        print(type(inst))    
        print(inst.args)     
        print(inst)

#Fetch current IP information for a single IPv4 address.
#Necessary Upgrade Package 
def secTrailsApiIpWhoisMethod(ip):
  
    try:
        
        ipWhois = "ips/%s/whois" % ip
        
        response = requests.request("GET", URL_API_SECURITY_TRAILS + "%s" % ipWhois, headers=HEADERS_API_SECURITY_TRAILS)
        
        print(COLOR + response.text)
                        
    except Exception as inst:
        print(type(inst))    
        print(inst.args)     
        print(inst)

#Fetch user agents seen during the last 30 days for a specific IPv4 address. It shows devices with egressing traffic based on large scale web server logs. The number of results is not limited.
#Necessary Upgrade Package 
def secTrailsApiUserAgentMethod(ip):
  
    try:
        
        ipUserAgent = "ips/%s/whois" % ip
        
        response = requests.request("GET", URL_API_SECURITY_TRAILS + "%s" % ipUserAgent, headers=HEADERS_API_SECURITY_TRAILS)
        
        print(COLOR + response.text)
                        
    except Exception as inst:
        print(type(inst))    
        print(inst.args)     
        print(inst)

#Fetch zone files including authoritative nameservers with ease. The method returns a .csv.gz file if successful. If ns is true the columns are apex_domain,nameservers (namerservers delimiter: |) and just apex_domain if ns is false.
#Necessary Upgrade Package 
def secTrailsApiFeedstMethod(typeFedd):
  
    try:
        
        feeds = "feeds/domains/%s" % typeFedd
        
        headersAux = {"Accept": "application/gzip", "user-agent": "trapsteo_milongas", "apikey": API_KEY}
        
        response = requests.request("GET", URL_API_SECURITY_TRAILS + "%s" % feeds, headers=headersAux)
        
        print(COLOR + response.text)
                        
    except Exception as inst:
        print(type(inst))    
        print(inst.args)     
        print(inst)

#Download a list of DMARC records. The column is apex_domain.
#Necessary Upgrade Package 
def secTrailsApiDMARCtMethod(dmarc):
  
    try:
        
        typeDmarc = "feeds/dmarc/%s" % dmarc
        
        headersAux = {"Accept": "application/gzip", "user-agent": "trapsteo_milongas", "apikey": API_KEY}
        
        response = requests.request("GET", URL_API_SECURITY_TRAILS + "%s" % typeDmarc, headers=headersAux)
        
        print(COLOR + response.text)
                        
    except Exception as inst:
        print(type(inst))    
        print(inst.args)     
        print(inst)

#Download a list of subdomains, with the possibility of filtering by TLD. The response itself is streamed to a file, which means the data is received in chunks. When using filter you must specify the tld parameter and vise versa. The method returns a .csv.gz file if successful. The columns are apex_domain,hostname.
#Necessary Upgrade Package 
def secTrailsApiSubdomainsDowloadCtMethod(typeSubdomain):
  
    try:
        
        typeSubdomain = "feeds/subdomains/%s" % typeSubdomain
        
        headersAux = {"Accept": "application/gzip", "user-agent": "trapsteo_milongas", "apikey": API_KEY}
        
        response = requests.request("GET", URL_API_SECURITY_TRAILS + "%s" % typeSubdomain, headers=headersAux)
        
        print(COLOR + response.text)
                        
    except Exception as inst:
        print(type(inst))    
        print(inst.args)     
        print(inst)




if __name__ == '__main__':
    functionCallMethod()   
    
    
    
    
    
    
    
    
    
