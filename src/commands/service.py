import click
import subprocess


@click.command()
@click.option("--option", help="ECS CLI configuration")
def service(option):
    """AWS ECS-CLI commands for Zenoo processes"""
    main_command = "source ./config.sh && ecs-cli compose --project-name $PROJECT_NAME service %s --cluster-config $CONFIG_NAME --ecs-profile $PROFILE_NAME"
    subprocess.run(main_command % option, shell=True, executable="/bin/bash")
