



def spotify_login():
    # Initialize SpotifyOAuth
    


    print(f"Please navigate to the following URL to log in: {auth_url}")

    # Prompt user to paste the redirect URL after login
    response_url = input("Paste the URL you were redirected to: ")

    # Extract the access token
    code = sp_oauth.parse_response_code(response_url)
    token_info = sp_oauth.get_access_token(code)

    # Initialize Spotipy client with the access token
    sp = spotipy.Spotify(auth=token_info['access_token'])
    
    # Fetch and display user profile information
    user_profile = sp.user_playlist()
    print(f"Logged in as: {user_profile['display_name']} ({user_profile['email']})")

if __name__ == "__main__":
    spotify_login()
