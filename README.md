# McDonald-s-APP

> Please note that this app might stop working in the near future, as
> they have changed the hashing algorithm from simple MD5 to
> AES encryption + Base64 hashing using a differently formatted string.

API wrapper for interacting with the Taiwan McDaily app.

## Example

Obtain login token
```sh
python3 mask.py
```

Login and interact with the McDaily app
```py
from McDonald import McDonald

# Creat a object
Account = McDonald('Your token')

# Get lottery
Account.Lottery()

# Get the coupon list
list = Account.Coupon_List()
```