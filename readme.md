# ansible-openvpn

## Usage

1) Copy `inventory.yml.sample` to `inventory.yml`, edit host ip.

2) Copy `vars.yml.sample` to `vars.yml`, edit certificates list and routing option.

3) Open shell, cd to directory and run playbook.

```bash
ansible-playbook -i inventory.yml playbook.yml
```

## Note

Tested on Ubuntu 22.04 LTS

## Author

Stanislav Doronin <mugisbrows@gmail.com>

## License

ansible-openvpn is distributed under the terms of MIT license, check `LICENSE` file.
