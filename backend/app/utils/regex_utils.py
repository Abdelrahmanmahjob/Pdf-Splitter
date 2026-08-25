import re


REQUEST_PATTERN = re.compile(

    r"(ADF\d)-RFI-(AR|ME|ELC|CI)-(\d+)-R(\d+)"

)

def extract_request(text):

    match = REQUEST_PATTERN.search(text)

    if not match:

        return None

    return {

        "project": match.group(1),

        "discipline": match.group(2),

        "request_number": match.group(3),

        "revision": f"R{match.group(4)}"

    }