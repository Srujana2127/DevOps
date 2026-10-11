import docker

client = docker.from_env()

print("Building image...")
client.images.build(path=".", tag="flask-apparmor")

print("Starting container with AppArmor profile...")
container = client.containers.run(
    "flask-apparmor",
    name="flask-apparmor-demo",
    ports={"5000/tcp": 5000},
    security_opt=["apparmor=my-apparmor-profile"],
    detach=True,
)

try:
    container.reload()
    print(f"Container started: {container.short_id}")

    info = client.api.inspect_container(container.id)
    print("Configured security options:",
          info["HostConfig"]["SecurityOpt"])

    print("Actual process AppArmor label:")
    try:
        print(container.exec_run(
            "cat /proc/self/attr/current"
        ).output.decode().strip())
    except docker.errors.APIError as error:
        print(f"Could not inspect process label: {error}")

finally:
    container.stop()
    container.remove()
    print("Container stopped and removed.")
