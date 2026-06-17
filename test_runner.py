import requests

from api_scanner import (
    APIScanner
)


def generate_report(
    results
):

    report = """

    <html>

    <head>

    <title>
    API Test Report
    </title>

    </head>

    <body>

    <h1>
    API Test Report
    </h1>

    <table border="1">

    <tr>

    <th>URL</th>

    <th>Status</th>

    </tr>

    """

    for item in results:

        report += f"""

        <tr>

        <td>
        {item['url']}
        </td>

        <td>
        {item['status']}
        </td>

        </tr>

        """

    report += """

    </table>

    </body>

    </html>

    """

    with open(
        "test_report.html",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            report
        )


def run_tests():

    print(
        "\n====================="
    )

    print(
        "SMART API TESTER"
    )

    print(
        "====================="
    )

    api_url = input(
        "\nAPI URL:\n"
    )

    scanner = APIScanner()

    endpoints = scanner.scan(
        api_url
    )

    results = []

    print(
        "\nRunning Tests..."
    )

    for endpoint in endpoints:

        try:

            response = requests.get(
                endpoint["url"],
                timeout=5
            )

            results.append({

                "url":
                endpoint["url"],

                "status":
                response.status_code

            })

            print(
                f"✓ "
                f"{endpoint['url']}"
            )

        except:

            results.append({

                "url":
                endpoint["url"],

                "status":
                "FAILED"

            })

            print(
                f"✗ "
                f"{endpoint['url']}"
            )

    generate_report(
        results
    )

    print(
        "\nReport Generated:"
    )

    print(
        "test_report.html"
    )


if __name__ == "__main__":

    run_tests()