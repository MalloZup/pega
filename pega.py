#!/usr/bin/env python3

import json

# remove this later

SALT_JSON = "salt-events.json"

## {
#   "fun" : "state.sls",
#   "id" : "4cb256385a9c45a0a1e3e619b2a78150",
#   "_stamp" : "2019-03-01T11:23:52.895913",
#   "cmd" : "_return",
#   "fun_args" : [
#      "etc-hosts",
#      {
#         "queue" : false,
#         "concurrent" : false
#      }
#   ],
#   "success" : true,
#   "out" : "highstate",
#   "return" : {
#      "caasp_hosts_|-/etc/hosts_|-/etc/hosts_|-managed" : {
#         "name" : "/etc/hosts",
#         "result" : false,
#         "changes" : {},
#  "comment" : "State 'caasp_hosts.managed' was not found in SLS 'etc-hosts'\nReason: 'caasp_hosts.managed' is not available.\n",
#         "__run_num__" : 0
#      }
#   },
#   "jid" : "20190301112348620779",
#   "retcode" : 2
#},
#
    
def _read_salt_json(json_file):
    with open(json_file, 'r') as json_data:
        return json.load(json_data)

def extract_failures(json_file):
    """
    take as input a salt-json file
    and extract failures
    """
    salt_events = _read_salt_json(json_file)
    for event in salt_events:
        try:
           salt_returner = event["return"]
           for item in salt_returner:
                   print(list(item.values())
           print("---------------")

        except Exception:
            pass
        except KeyError:
            pass
        except TypeError:
            pass
def main():
    """
    parse json and extract failures.
    """
    extract_failures(SALT_JSON)

if __name__ == "__main__":
    main()
