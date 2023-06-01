if session_id is not None:
        fetch_token_call = 'FetchToken' 
        use_fetch_token = True
        if use_fetch_token:
          call_name = fetch_token_call
          call_header['X-EBAY-API-CALL-NAME'] = call_name

        header = call_header    