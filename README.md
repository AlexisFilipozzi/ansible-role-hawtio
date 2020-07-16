Hawtio
=========

Install hawtio with systemctl.

Requirements
------------
Require Java, for instance you can use :
 * geerlingguy.java

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - role: alexisfilipozzi.hawtio

License
-------
MIT

How to run tests
------------------
### Prerequisite

 * docker
 * run the following command
   ```bash
   pip install molecule yamllint ansible-lint docker
   ```

### Run the tests

```bash
molecule test
```
