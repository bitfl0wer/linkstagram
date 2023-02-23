import instaloader

loader = instaloader.Instaloader()
post = instaloader.Post.from_shortcode(loader.context, "CnEypZLq61B")

loader.download_post(post, "test")
