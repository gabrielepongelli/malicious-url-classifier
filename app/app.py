import re
import whois
import math
from tranco import Tranco
from urllib.parse import urlparse, unquote, urlunparse
from datetime import datetime
from pydantic import BaseModel, AnyHttpUrl, ValidationError

from flask import Flask, request, render_template, jsonify

from src.decision_tree import tree as is_malicious

app = Flask(__name__)

class UrlValidator(BaseModel):
    url: AnyHttpUrl

def get_website_rank(url: str) -> int:
    if not hasattr(get_website_rank, 'rank_list'):
        t = Tranco(cache=True)
        get_website_rank.rank_list = t.list(full=True)
        get_website_rank.n_ranks = len(get_website_rank.rank_list.list)
    rank = get_website_rank.rank_list.rank(url)
    return get_website_rank.n_ranks-rank+1 if rank != -1 else 0

class UrlBuilder:
    def __init__(self, url: str):
        self.url = url

        self.parsed = urlparse(url)
        self.scheme = unquote(self.parsed.scheme)
        self.netloc = unquote(self.parsed.netloc)
        self.path = unquote(self.parsed.path)
        self.params = unquote(self.parsed.params)
        self.query = unquote(self.parsed.query)
        self.fragment = unquote(self.parsed.fragment)
        self.unquoted_url = urlunparse((
            self.scheme,
            self.netloc,
            self.path,
            self.params,
            self.query,
            self.fragment
        ))

        try:
            self.whois = whois.whois(url=self.netloc)
        except:
            self.whois = None
    
    def domain_name(self) -> str:
        return re.sub(r"^www\.", "", self.parsed.netloc).split(':')[0]

    def url_len(self) -> int:
        return len(self.url)

    def n_subdomains(self) -> int:
        stripped_domain = self.domain_name()
        stripped_domain = stripped_domain.split('.')[:-1]
        return len(stripped_domain)

    def url_depth(self) -> int:
        return len(self.parsed.path.split("/")) - 1
    
    def has_prefix_suffix(self) -> int:
        return 1 if "-" in self.netloc else 0
    
    def entropy(self) -> float:
        string = self.unquoted_url.strip()
        prob = [float(string.count(c)) / len(string) for c in dict.fromkeys(list(string))]
        entropy = sum([(p * math.log(p) / math.log(2.0)) for p in prob])
        return entropy

    def tld(self) -> str:
        return self.parsed.netloc.split('.')[-1].split(':')[0]
    
    def has_dns_record(self) -> int:
        return 1 if self.whois is None else 0
    
    def web_traffic(self) -> int:
        return get_website_rank(self.parsed.netloc)
    
    def sus_domain_age(self) -> int:
        if self.whois is None:
            return 1

        creation_date = self.whois.creation_date
        expiration_date = self.whois.expiration_date
        if (expiration_date is None) or (creation_date is None):
            return 1
        
        if not isinstance(expiration_date, datetime):
            if type(expiration_date) is list:
                expiration_date = expiration_date[0]

            if type(expiration_date) is str:
                splitted = expiration_date.split(' ')
                expiration_date = ' '.join([splitted[0], splitted[1]])
                expiration_date = expiration_date.split('.')[0]
                expiration_date = datetime.strptime(
                    expiration_date.split('+')[0], 
                    "%Y-%m-%d %H:%M:%S")

        expiration_date = expiration_date.replace(tzinfo=None)

        if not isinstance(creation_date, datetime):
            if type(creation_date) is list:
                creation_date = creation_date[0]

            if type(creation_date) is str:
                splitted = creation_date.split(' ')
                creation_date = ' '.join([splitted[0], splitted[1]])
                creation_date = creation_date.split('.')[0]
                creation_date = datetime.strptime(
                    creation_date.split('+')[0], 
                    "%Y-%m-%d %H:%M:%S")

        creation_date = creation_date.replace(tzinfo=None)
        
        age = abs((expiration_date - creation_date).days)
        return 1 if age/30 < 12 else 0

    def build(self):
        data = {}
        data['url_len'] = self.url_len()
        data['n_subdomains'] = self.n_subdomains()
        data['url_depth'] = self.url_depth()
        data['has_prefix_suffix'] = self.has_prefix_suffix()
        data['entropy'] = self.entropy()

        accepted_tlds = ['dev', 'io', 'net', 'pl']
        tld = self.tld()

        data['tld_others'] = 1 if tld not in accepted_tlds else 0
        for t in accepted_tlds:
            data['tld_'+t] = 1 if data['tld_others'] == 0 and tld == t else 0
        
        data['has_dns_record'] = self.has_dns_record()
        data['web_traffic'] = self.web_traffic()
        data['sus_domain_age'] = self.sus_domain_age()
    
        return data

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    input_url = request.json.get('url')
    
    if not input_url:
        return jsonify({"error": "No input url provided"}), 400

    if type(input_url) is not str:
        return jsonify({"error": "Invalid url"}), 400
    
    input_url = input_url.strip()

    try:
        UrlValidator(url=input_url)
    except ValidationError:
        return jsonify({"error": "Invalid url"}), 400
    
    url_builder = UrlBuilder(input_url)
    data = url_builder.build()
    res = is_malicious(**data)
    
    return jsonify({"output": res})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
