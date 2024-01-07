# -*- coding: utf-8 -*-
import requests
import json
import matplotlib.pyplot as plt
import logging

token = userdata.get('git_token')

# Logging Config

logging.basicConfig(level=logging.WARNING)

def top_followers():

    """
    GitHub Top Followers Visualization Script

    This script retrieves information about GitHub users with the most followers, fetches their follower counts,
    and visualizes the data using a bar chart.

    Parameters:
    - token (str): GitHub API token for authentication.
    - num_users (int): Number of top GitHub users to retrieve and visualize.

    """

    url = 'https://api.github.com/search/users?q=followers:%3E0&sort=followers&order=desc' # Checks for users and sort in descending order
    headers = {'Authorization': 'Bearer ' + token}
    
    try:
        num_users = int(input("Enter the number of top users to display (1-20): "))
        
        if 1 <= num_users <= 20:
            r = requests.get(url, headers=headers)
            r.raise_for_status()

            data = r.json()
            followers_count = []

            top_users = data['items'][:num_users] # Display number of users selected

            for index, user in enumerate(top_users, start=1):

                try:
                    # Get detailed user information using the user's URL
                    user_url = user['url']
                    user_response = requests.get(user_url, headers=headers)
                    user_response.raise_for_status() 

                    # Check if the request for individual user details was successful
                    user_data = user_response.json()
                    follower_count = user_data.get('followers', 'not found')
                    followers_count.append(follower_count)

                    print(f"{index}. {user['login']} - Followers: {follower_count}")

                except requests.exceptions.RequestException as user_error:
                  logging.warning(f"Error fetching individual user data for {user['login']}: {user_error}")

            ## Visualization:
            usernames = [user['login'] for user in top_users]
            plt.figure(figsize=(30, 16))
            plt.bar(usernames, followers_count)
            plt.xlabel('Top Github Users')
            plt.ylabel('Number of Followers')
            plt.title('20 Github Users with the most followers', fontsize=20)
            plt.show()

        else:
          logging.warning("Please enter a number between 1 and 20.")

    except ValueError:
      logging.warning("Please enter a valid integer.")

top_followers()
