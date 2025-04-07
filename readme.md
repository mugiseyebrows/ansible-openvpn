# ansible-openvpn

## Usage

1) Edit `inventory.yml`.

2) Edit `vars.yml`.

3) Open shell, cd to directory and run playbook.

```bash
ansible-playbook -i inventory.yml playbook.yml
```

Client configs are generated in two formats:

1) zipped bundle of files (conf ca cert key ta) 

2) ovpn file

Configs are fetched to `/tmp` directory on local machine

## Note

Tested on Ubuntu 22.04 LTS

## Author

Stanislav Doronin <mugisbrows@gmail.com>

## License

ansible-openvpn is distributed under the terms of MIT license, check `LICENSE` file.
