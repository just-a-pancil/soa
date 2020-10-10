import qrcode
qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=1,)
qr.add_data("https://login.microsoftonline.com/common/oauth2/authorize?client_id=4345a7b9-9a63-4910-a426-35363201d503&redirect_uri=https%3A%2F%2Fwww.office.com%2Flanding&response_type=code%20id_token&scope=openid%20profile&response_mode=form_post&nonce=637374930683189571.ZmNlZTc2YzEtMGYyMC00N2M5LWE5MGYtMjNjM2NjZDQ2NGI4NTVhM2E3YjEtMmYxNy00YjNiLTk2ZWEtYjJlZWIwYTg3NzM4&ui_locales=en-US&mkt=en-US&client-request-id=23738e56-4bc2-4428-a37d-55e945c9ca64&state=VVPBqqZ2kCnKXuLpprQPVAL6fpu62pq96lAEJzE_3XrV8vvjnPaQJ5Ez1B3F5Sicf4vRZaBlkcEZ5N77zzbo4DOFquDrS7mXeZcLnsEs7xf4eoPk7AquRd42bgbmZRKvd_LkXkV-1P_Qsa8xVCTRhT7WyzbU_Mh6pv3TGZraAzKZG_d68JXnUTBUbFwcMa4TFLrhYyzjcfEFa1RVTN1ghdkni3CZu2WHYBZf1agc3_2DNawCnxLr5w6KBcZf98p7GG9AsmIZXfZefZMGqUmyeql7B6oP-WHEt2Xgvu5RxAAU0KYosJiSqx4byfD0zsIT&x-client-SKU=ID_NETSTANDARD2_0&x-client-ver=6.6.0.0")
qr.make()
img=qr.make_image()
img.save("1qr.jpg")
