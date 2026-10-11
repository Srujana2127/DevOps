import docker

client = docker.from_env()

container = client.containers.run(
    "flask-apparmor",
    name="apparmor-restriction-test",
    security_opt=["apparmor=my-apparmor-profile"],
    detach=True,
)

try:
    print(f"Container started: {container.short_id}")

    tests = [
        ("Read /etc/shadow", "cat /etc/shadow"),
        ("Execute /bin/bash", "/bin/bash --version"),
    ]

    for description, command in tests:
        result = container.exec_run(
            ["sh", "-c", command]
        )
        print(f"\n{description}")
        print(f"Exit code: {result.exit_code}")
        print(result.output.decode(errors="replace"))

finally:
    container.stop()
    container.remove()
    print("\nContainer stopped and removed.")
