class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_g, email_m = collections.defaultdict(set), {}
        for account in accounts:
            for email in account[1:]:
                if email != account[1]:
                    email_g[account[1]].add(email)
                    email_g[email].add(account[1])
                email_m[email] = account[0]
        rslt, visited = [], set()
        def dfs(email):
            if email not in email_g:
                visited.add(email)
                return [email]
            else:
                rslt = [email]
                for em in email_g[email]:
                    if em not in visited:
                        visited.add(em)
                        rslt += dfs(em)
                return rslt
        for email, holder in email_m.items():
            if email not in visited:
                visited.add(email)
                rslt.append([holder]+sorted(dfs(email)))

        return rslt  
