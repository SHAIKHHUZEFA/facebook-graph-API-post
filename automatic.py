import facebook
post_id='112106753795630'
profile_id='109502100722762'

token='EAAJ0HTX3Xo8BANRGKS4qNvomqoe84KU2lZCfQxCjCZAEx51JEmZC2q52PY5VpYV8nemHr6p8GZBqytqRaUqKX3FiaZCg5bmTFBhiDTaZCNrZBSLJIHJAQKyZANATQPtI3rbUXFmZBNUvuiAFHtjZAgMtCes0IOd07rWTzHjpyZAAkw1oZA2ONESJvSwaBERGPJ3MbKgZD'


fb=facebook.GraphAPI(access_token=token)

def post_image():
    fb.put_photo(open('image450.png','rb'),message='hello this is first image on facebook')

if __name__=="__main__":
    post_image()