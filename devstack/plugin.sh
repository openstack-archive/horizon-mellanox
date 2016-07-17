# plugin.sh

if [[ "$1" == "stack" && "$2" == "pre-install" ]]; then
    # no-op
    :
fi

if [[ "$1" == "stack" && "$2" == "post-config" ]]; then
    setup_develop $DEST/horizon_mellanox
    cp ${DEST}/horizon_mellanox/enabled/_7000_mlx.py /opt/stack/horizon/openstack_dashboard/local/enabled/
    cd /opt/stack/horizon
    python manage.py collectstatic --clear --noinput
    python manage.py compress --force
    service apache2 restart
fi
