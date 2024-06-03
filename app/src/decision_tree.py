def tree(url_len, n_subdomains, url_depth, has_prefix_suffix, entropy, has_dns_record, web_traffic, sus_domain_age, tld_dev, tld_io, tld_net, tld_others, tld_pl):
    if url_len <= 82.5:
        if url_depth <= 1.5:
            return 0
        else:  # if url_depth > 1.5
            if sus_domain_age <= 0.5:
                return 1
            else:  # if sus_domain_age > 0.5
                if entropy <= -4.442240953445435:
                    if url_len <= 67.5:
                        if n_subdomains <= 1.5:
                            return 1
                        else:  # if n_subdomains > 1.5
                            if tld_io <= 0.5:
                                if has_dns_record <= 0.5:
                                    if tld_others <= 0.5:
                                        if has_prefix_suffix <= 0.5:
                                            if n_subdomains <= 2.5:
                                                return 0
                                            else:  # if n_subdomains > 2.5
                                                return 1
                                        else:  # if has_prefix_suffix > 0.5
                                            return 1
                                    else:  # if tld_others > 0.5
                                        if entropy <= -4.561221122741699:
                                            return 1
                                        else:  # if entropy > -4.561221122741699
                                            return 0
                                else:  # if has_dns_record > 0.5
                                    return 1
                            else:  # if tld_io > 0.5
                                return 1
                    else:  # if url_len > 67.5
                        if n_subdomains <= 2.5:
                            return 0
                        else:  # if n_subdomains > 2.5
                            return 0
                else:  # if entropy > -4.442240953445435
                    if tld_net <= 0.5:
                        if web_traffic <= 4299222.5:
                            return 0
                        else:  # if web_traffic > 4299222.5
                            return 0
                    else:  # if tld_net > 0.5
                        return 0
    else:  # if url_len > 82.5
        if web_traffic <= 1356360.5:
            if n_subdomains <= 1.5:
                if entropy <= -5.171638011932373:
                    return 0
                else:  # if entropy > -5.171638011932373
                    if url_depth <= 4.5:
                        if has_prefix_suffix <= 0.5:
                            if web_traffic <= 619852.5:
                                if tld_others <= 0.5:
                                    if tld_net <= 0.5:
                                        if url_len <= 156.0:
                                            return 0
                                        else:  # if url_len > 156.0
                                            return 1
                                    else:  # if tld_net > 0.5
                                        return 0
                                else:  # if tld_others > 0.5
                                    if url_depth <= 3.5:
                                        if entropy <= -4.780558347702026:
                                            if url_depth <= 2.5:
                                                if url_len <= 156.0:
                                                    return 1
                                                else:  # if url_len > 156.0
                                                    return 0
                                            else:  # if url_depth > 2.5
                                                return 0
                                        else:  # if entropy > -4.780558347702026
                                            return 0
                                    else:  # if url_depth > 3.5
                                        return 1
                            else:  # if web_traffic > 619852.5
                                return 1
                        else:  # if has_prefix_suffix > 0.5
                            if tld_others <= 0.5:
                                return 1
                            else:  # if tld_others > 0.5
                                return 0
                    else:  # if url_depth > 4.5
                        if url_len <= 83.5:
                            return 1
                        else:  # if url_len > 83.5
                            if url_depth <= 5.5:
                                if entropy <= -5.003771781921387:
                                    return 1
                                else:  # if entropy > -5.003771781921387
                                    return 0
                            else:  # if url_depth > 5.5
                                if entropy <= -4.146605730056763:
                                    if url_len <= 84.5:
                                        return 0
                                    else:  # if url_len > 84.5
                                        return 0
                                else:  # if entropy > -4.146605730056763
                                    return 0
            else:  # if n_subdomains > 1.5
                if url_depth <= 5.5:
                    if entropy <= -4.576188564300537:
                        if entropy <= -4.706776857376099:
                            if entropy <= -4.740638971328735:
                                return 0
                            else:  # if entropy > -4.740638971328735
                                if url_depth <= 4.5:
                                    if entropy <= -4.740541696548462:
                                        return 0
                                    else:  # if entropy > -4.740541696548462
                                        if n_subdomains <= 2.5:
                                            if has_prefix_suffix <= 0.5:
                                                if entropy <= -4.7144834995269775:
                                                    return 0
                                                else:  # if entropy > -4.7144834995269775
                                                    return 0
                                            else:  # if has_prefix_suffix > 0.5
                                                return 1
                                        else:  # if n_subdomains > 2.5
                                            return 1
                                else:  # if url_depth > 4.5
                                    return 0
                        else:  # if entropy > -4.706776857376099
                            if url_depth <= 2.5:
                                return 0
                            else:  # if url_depth > 2.5
                                if n_subdomains <= 2.5:
                                    if has_prefix_suffix <= 0.5:
                                        if tld_pl <= 0.5:
                                            if tld_others <= 0.5:
                                                if entropy <= -4.5807411670684814:
                                                    return 0
                                                else:  # if entropy > -4.5807411670684814
                                                    return 1
                                            else:  # if tld_others > 0.5
                                                return 1
                                        else:  # if tld_pl > 0.5
                                            return 1
                                    else:  # if has_prefix_suffix > 0.5
                                        return 1
                                else:  # if n_subdomains > 2.5
                                    return 1
                    else:  # if entropy > -4.576188564300537
                        if url_depth <= 2.5:
                            return 1
                        else:  # if url_depth > 2.5
                            if has_prefix_suffix <= 0.5:
                                if url_depth <= 4.5:
                                    if url_len <= 94.5:
                                        if entropy <= -4.510974407196045:
                                            if entropy <= -4.539118766784668:
                                                return 0
                                            else:  # if entropy > -4.539118766784668
                                                return 1
                                        else:  # if entropy > -4.510974407196045
                                            if tld_io <= 0.5:
                                                return 0
                                            else:  # if tld_io > 0.5
                                                return 1
                                    else:  # if url_len > 94.5
                                        if url_len <= 120.5:
                                            if url_len <= 98.5:
                                                return 1
                                            else:  # if url_len > 98.5
                                                return 0
                                        else:  # if url_len > 120.5
                                            return 1
                                else:  # if url_depth > 4.5
                                    return 0
                            else:  # if has_prefix_suffix > 0.5
                                if entropy <= -4.52222752571106:
                                    return 0
                                else:  # if entropy > -4.52222752571106
                                    return 1
                else:  # if url_depth > 5.5
                    if entropy <= -4.7587316036224365:
                        if entropy <= -5.3006720542907715:
                            return 1
                        else:  # if entropy > -5.3006720542907715
                            if url_len <= 178.0:
                                return 1
                            else:  # if url_len > 178.0
                                return 0
                    else:  # if entropy > -4.7587316036224365
                        if url_len <= 93.0:
                            if url_depth <= 8.5:
                                if has_prefix_suffix <= 0.5:
                                    return 0
                                else:  # if has_prefix_suffix > 0.5
                                    return 1
                            else:  # if url_depth > 8.5
                                return 1
                        else:  # if url_len > 93.0
                            if url_depth <= 13.5:
                                if entropy <= -4.35442328453064:
                                    if tld_dev <= 0.5:
                                        return 0
                                    else:  # if tld_dev > 0.5
                                        return 1
                                else:  # if entropy > -4.35442328453064
                                    if url_depth <= 8.0:
                                        if n_subdomains <= 2.5:
                                            if url_len <= 99.5:
                                                return 0
                                            else:  # if url_len > 99.5
                                                return 1
                                        else:  # if n_subdomains > 2.5
                                            return 0
                                    else:  # if url_depth > 8.0
                                        return 0
                            else:  # if url_depth > 13.5
                                return 1
        else:  # if web_traffic > 1356360.5
            if has_prefix_suffix <= 0.5:
                if web_traffic <= 4299536.5:
                    if entropy <= -5.098928213119507:
                        if web_traffic <= 4288410.5:
                            if web_traffic <= 4286232.0:
                                if url_len <= 103.5:
                                    if url_depth <= 1.5:
                                        return 1
                                    else:  # if url_depth > 1.5
                                        if entropy <= -5.445810079574585:
                                            return 1
                                        else:  # if entropy > -5.445810079574585
                                            return 0
                                else:  # if url_len > 103.5
                                    if entropy <= -5.409289598464966:
                                        if entropy <= -5.609228849411011:
                                            if entropy <= -5.996514320373535:
                                                return 1
                                            else:  # if entropy > -5.996514320373535
                                                return 0
                                        else:  # if entropy > -5.609228849411011
                                            return 1
                                    else:  # if entropy > -5.409289598464966
                                        return 0
                            else:  # if web_traffic > 4286232.0
                                if url_depth <= 3.5:
                                    return 1
                                else:  # if url_depth > 3.5
                                    return 0
                        else:  # if web_traffic > 4288410.5
                            if url_len <= 618.5:
                                if entropy <= -5.62476921081543:
                                    if entropy <= -5.67846941947937:
                                        if web_traffic <= 4299239.0:
                                            return 0
                                        else:  # if web_traffic > 4299239.0
                                            if url_depth <= 1.5:
                                                return 0
                                            else:  # if url_depth > 1.5
                                                return 1
                                    else:  # if entropy > -5.67846941947937
                                        return 1
                                else:  # if entropy > -5.62476921081543
                                    if url_len <= 144.5:
                                        if web_traffic <= 4298856.5:
                                            return 0
                                        else:  # if web_traffic > 4298856.5
                                            if url_len <= 99.0:
                                                if web_traffic <= 4299487.5:
                                                    return 0
                                                else:  # if web_traffic > 4299487.5
                                                    return 1
                                            else:  # if url_len > 99.0
                                                return 1
                                    else:  # if url_len > 144.5
                                        return 0
                            else:  # if url_len > 618.5
                                return 1
                    else:  # if entropy > -5.098928213119507
                        if tld_io <= 0.5:
                            if web_traffic <= 4299397.0:
                                if url_len <= 665.5:
                                    if web_traffic <= 2073563.0:
                                        if web_traffic <= 1496586.0:
                                            return 0
                                        else:  # if web_traffic > 1496586.0
                                            return 1
                                    else:  # if web_traffic > 2073563.0
                                        return 0
                                else:  # if url_len > 665.5
                                    if web_traffic <= 4294918.5:
                                        return 1
                                    else:  # if web_traffic > 4294918.5
                                        return 0
                            else:  # if web_traffic > 4299397.0
                                if web_traffic <= 4299400.5:
                                    return 1
                                else:  # if web_traffic > 4299400.5
                                    if web_traffic <= 4299440.5:
                                        if url_depth <= 3.0:
                                            return 0
                                        else:  # if url_depth > 3.0
                                            return 1
                                    else:  # if web_traffic > 4299440.5
                                        return 0
                        else:  # if tld_io > 0.5
                            if web_traffic <= 4291453.0:
                                return 1
                            else:  # if web_traffic > 4291453.0
                                return 0
                else:  # if web_traffic > 4299536.5
                    return 1
            else:  # if has_prefix_suffix > 0.5
                if entropy <= -4.609502553939819:
                    if url_depth <= 1.5:
                        return 0
                    else:  # if url_depth > 1.5
                        if url_depth <= 4.5:
                            if tld_net <= 0.5:
                                if web_traffic <= 4275989.5:
                                    return 1
                                else:  # if web_traffic > 4275989.5
                                    if web_traffic <= 4277421.5:
                                        return 0
                                    else:  # if web_traffic > 4277421.5
                                        return 1
                            else:  # if tld_net > 0.5
                                return 0
                        else:  # if url_depth > 4.5
                            if web_traffic <= 3013121.0:
                                return 1
                            else:  # if web_traffic > 3013121.0
                                return 0
                else:  # if entropy > -4.609502553939819
                    if entropy <= -4.570605278015137:
                        if url_len <= 97.0:
                            return 1
                        else:  # if url_len > 97.0
                            return 0
                    else:  # if entropy > -4.570605278015137
                        return 0
