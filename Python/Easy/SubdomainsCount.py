class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domains = {}
        for domain in cpdomains:
            count_and_domain = domain.split(' ')
            count = int(count_and_domain[0])
            domain = count_and_domain[1]
            subdomains = domain.split('.')
            
            for idx, subdomain in enumerate(subdomains):
                this_subdomain = ".".join(subdomains[idx:])
                if this_subdomain in domains:
                    domains[this_subdomain] += count
                else:
                    domains[this_subdomain] = count
                 
        return ["{} {}".format(count, domain) for domain, count in domains.items()]