echo -e "Nethosts Inventory File Updated (/mycode/inv/dev/nethosts)"
curl https://static.alta3.com/projects/ansible/deploy/nethosts --create-dirs -o ~/mycode/inv/dev/nethosts

echo -e ".ansible.cfg Updated (/home/student/.ansible.cfg)"
curl https://static.alta3.com/projects/ansible/deploy/ansiblecfg --create-dirs -o ~/.ansible.cfg
