import docker

client = docker.from_env()

container = client.containers.run(
    "flask-apparmor",
    detach=True,
    security_opt=["apparmor=my-apparmor-profile"],
    name="apparmor-restriction-test",
)

try:
    for command in [
        ["cat", "/etc/passwd"],
        ["/bin/bash"],
    ]:
        print(f"\nTesting command: {command}")

        result = container.exec_run(command)
        print("Exit code:", result.exit_code)
        print("Output:", result.output.decode(errors="replace"))

finally:
    container.stop()
    container.remove()
    print("\nTest container cleaned up.")