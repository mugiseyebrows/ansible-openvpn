# ansible-openvpn

## Usage

1) Copy `inventory.yml.sample` to `inventory.yml`, edit host ip.

2) Copy `vars.yml.sample` to `vars.yml`, edit certificates list and routing option.

3) Open shell, cd to directory and run playbook.

```bash
ansible-playbook -i inventory.yml playbook.yml
```

Client configs are generated in two formats:

1) zipped bundle of files (conf ca cert key ta ovpn) 

2) self contained ovpn file with inline certs and keys

Configs are fetched to `/tmp` directory on local machine

## Note

Tested on Ubuntu 22.04 LTS

## Author

Stanislav Doronin <mugisbrows@gmail.com>

## License

ansible-openvpn is distributed under the terms of MIT license, check `LICENSE` file.
