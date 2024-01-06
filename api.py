# -*- coding: utf-8 -*-
"""API.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zADv6JcjYDmeeq2NmAO0zyJ9kIUCzKgX
"""

import requests
import json
import matplotlib.pyplot as plt

from google.colab import userdata
token = userdata.get('git_token')

def top_followers():

  """
  GitHub Top Followers Visualization Script

  This script retrieves information about GitHub users with the most followers, fetches their follower counts, and visualizes the data using a bar chart.

  Parameters:
  - token (str): GitHub API token for authentication.
  - num_users (int): Number of top GitHub users to retrieve and visualize.

  """

  url = 'https://api.github.com/search/users?q=followers:%3E0&sort=followers&order=desc' # Checks for users and sort in descending order
  headers = {'Authorization': 'Bearer ' + token}

  r = requests.get(url, headers=headers)
  data = r.json()
  followers_count = []

    # Check if the request was successful (status code 200)
  if r.status_code == 200:
        top_users = data['items'][:20] # Get the top 20 users

        for index, user in enumerate(top_users, start=1):
            # Get detailed user information using the user's URL
            user_url = user['url']
            user_response = requests.get(user_url, headers=headers)

            # Check if the request for individual user details was successful
            if user_response.status_code == 200:
                user_data = user_response.json()
                follower_count = user_data.get('followers', 'not found')
                followers_count.append(follower_count)

                print(f"{index}. {user['login']} - Followers: {follower_count}")
            else:
                print(f"Error fetching individual user data for {user['login']}: {user_response.status_code}, {user_response.text}")
       ## Visualization:
        usernames = [user['login'] for user in top_users]
        plt.figure(figsize=(30, 16))
        plt.bar(usernames, followers_count)
        plt.xlabel('Top Github Users')
        plt.ylabel('Number of Followers')
        plt.title('20 Github Users with the most followers', fontsize=20)
        plt.show()

  else:
    # Print an error message if the request for top users was unsuccessful
      print(f"Error: {r.status_code}, {r.text}")

top_followers()