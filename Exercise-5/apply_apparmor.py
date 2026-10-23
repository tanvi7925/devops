import docker

client = docker.from_env()

image, build_logs = client.images.build(
    path=".",
    tag="flask-apparmor"
)
print("Docker image built:", image.tags)

container = client.containers.run(
    "flask-apparmor",
    detach=True,
    ports={"5000/tcp": 5000},
    security_opt=["apparmor=my-apparmor-profile"],
    name="flask-apparmor-test"
)

print("Container started:", container.short_id)

container.reload()
print("Security options:", container.attrs["HostConfig"]["SecurityOpt"])

container.stop()
container.remove()
print("Container stopped and removed.")