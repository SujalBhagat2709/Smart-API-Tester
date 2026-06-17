import requests


class APIScanner:

    def scan(self, base_url):

        endpoints = []

        common_endpoints = [

            "/",
            "/users",
            "/posts",
            "/products",
            "/orders",
            "/login",
            "/register"

        ]

        print(
            "\nScanning Endpoints..."
        )

        for endpoint in common_endpoints:

            url = (
                base_url.rstrip("/")
                + endpoint
            )

            try:

                response = requests.get(
                    url,
                    timeout=3
                )

                endpoints.append({

                    "url": url,

                    "status": response.status_code

                })

                print(
                    f"Found: {url}"
                )

            except:

                pass

        return endpoints


if __name__ == "__main__":

    scanner = APIScanner()

    url = input(
        "API URL: "
    )

    endpoints = scanner.scan(
        url
    )

    print(
        endpoints
    )