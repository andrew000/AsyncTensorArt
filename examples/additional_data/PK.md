# Private Key Generation

***

### [Optional] Create a password file

```shell
password_length=256
password_file='passwd'

openssl rand -hex -out $password_file $password_length
```

### Create a new private key

```shell
key_length=4096
key_file='private_key.pem'
password_file='passwd'

# Without password
openssl genrsa -out $key_file $key_length
# With password
openssl genrsa -des3 -out $key_file -passout file:$password_file $key_length
```

### Extract public key from private key

```shell
key_file='private_key.pem'
public_key_file='public_key.pem'
password_file='passwd'

# Without password
openssl rsa -pubout -in $key_file -out $public_key_file
# With password
openssl rsa -pubout -in $key_file -out $public_key_file -passin file:$password_file
```
