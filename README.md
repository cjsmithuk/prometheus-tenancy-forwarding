# prometheus-tenancy-forwarding
Example of simple tenancy and forwarding with prometheus

# Structure

    [ met1 :9021 ] --> [ prom1 :9121 / label ] --\
                                                  >---> [ prom3 :9221 ] --> query interface
    [ met2 :9022 ] --> [ prom2 :9122 / label ] --/


# Set up

1. Install prometheus 2.0 branch latest version in /opt/prometheus/
2. Create a python virtual environment: `python3 -m venv venv`
3. Enter the virtual environment `source venv/bin/activate`
4. Install required packages `python3 -m pip install prometheus_client`
5. Run met1 tenant `./met.py 1 &`. `curl http://localhost:9021/metrics` to check.
6. Run met2 tenant `./met.py 2 &`. `curl http://localhost:9022/metrics` to check.
7. Run met1 prometheus `./prom1 &`. `curl http://localhost:9121` to check.
8. Run met2 prometheus `./prom2 &`. `curl http://localhost:9122` to check.
