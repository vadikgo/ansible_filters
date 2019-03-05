# ansible_filters

test command

```bash
ansible localhost -m debug -a "msg={{ jenkins_plugins | unionattr(jenkins_plugins_custom, 'name') }}" -e @test.yml
```