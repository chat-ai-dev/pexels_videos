import os

from dotenv import load_dotenv
import requests
from mad_hatter.decorators import tool

load_dotenv()
PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")


@tool(return_direct=True)
def get_pexels_videos(tool_input, bot):
	"""Get the pexels videos. Replies to 'pexels tigers', 'pexels nature', etc. Input is the search string."""

	api_key = PEXELS_API_KEY
	url = 'https://api.pexels.com/videos/search'
	headers = {
		'Authorization': api_key
	}
	params = {
		'query': tool_input,
		'per_page': 1
	}

	# Send the GET request
	response = requests.get(url, headers=headers, params=params)

	results = None
	# Check if the request was successful (status code 200)
	if response.status_code == 200:
		data = response.json()
		results = data['videos'][0]['video_files'][0]['link']
		results = results + 'pexels.com'
	else:
		error_message = f"Request failed with status code {response.status_code}"
		return error_message

	return results
