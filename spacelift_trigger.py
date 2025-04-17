import os
import requests
import logging

SPACELIFT_API_URL = os.environ.get("SPACELIFT_API_URL")
SPACELIFT_API_KEY_ID = os.environ.get("SPACELIFT_API_KEY_ID")
SPACELIFT_API_KEY_SECRET = os.environ.get("SPACELIFT_API_KEY_SECRET")
SPACELIFT_STACK_ID = os.environ.get("SPACELIFT_STACK_ID")

CI_COMMIT_SHORT_SHA = os.environ.get("CI_COMMIT_SHORT_SHA")


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def get_spacelift_token(url, id, secret):
    """
    Get a Spacelift token."""

    query = """
    mutation GetSpaceliftToken($id: ID!, $secret: String!) {
        apiKeyUser(id: $id, secret: $secret) {
            jwt
        }
    }
    """
    variables = {"id": id, "secret": secret}
    response = requests.post(
        url,
        json={"query": query, "variables": variables},
        headers={"Content-Type": "application/json"}
    )
    if response.status_code == 200:
        return response.json()["data"]["apiKeyUser"]["jwt"]
    else:
        raise Exception(f'''Query failed with status code
                        {response.status_code}''')


def trigger_spacelift_run(url, token, stack, commit_sha, run_type):
    """
    Trigger a Spacelift run.

    :param url: Spacelift GraphQL API endpoint
    :param token: Authentication token
    :param stack: Stack ID
    :param commit_sha: Commit SHA
    :param run_type: Run type (e.g., TRACKED or UNTRACKED)
    :return: Run ID and state
    """
    query = """
    mutation TriggerRun($stack: ID!, $commitSha: String, $runType: RunType) {
      runTrigger(stack: $stack, commitSha: $commitSha, runType: $runType) {
        id
        state
      }
    }
    """
    variables = {
        "stack": stack,
        "commitSha": commit_sha,
        "runType": run_type
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.post(
            url,
            json={"query": query, "variables": variables},
            headers=headers
        )
        response.raise_for_status()

        response_json = response.json()

        # Check for errors in the response
        if "errors" in response_json:
            raise Exception(f"""GraphQL errors:
                {response_json['errors']}""")

        # Extract the data
        data = response_json.get("data", {}).get("runTrigger", None)
        if not data:
            raise Exception("No runTrigger data found in the response")

        return data["id"], data["state"]

    except requests.exceptions.RequestException as e:
        raise Exception(f"HTTP request failed: {e}")

    except Exception as e:
        raise Exception(f"An error occurred: {e}")


if __name__ == "__main__":
    token = get_spacelift_token(SPACELIFT_API_URL, SPACELIFT_API_KEY_ID,
                                SPACELIFT_API_KEY_SECRET)
    run_id, run_state = trigger_spacelift_run(
        SPACELIFT_API_URL,
        token,
        SPACELIFT_STACK_ID,
        CI_COMMIT_SHORT_SHA,
        "TRACKED"
    )

    logger.info(f"Triggered run {run_id} with state {run_state}")