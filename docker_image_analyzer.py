import subprocess

SIZE_LIMIT_MB = 500

def get_docker_images():
    result = subprocess.run(
        ["docker", "images", "--format", "{{.Repository}} {{.Tag}} {{.Size}}"],
        capture_output=True,
        text=True
    )
    return result.stdout.strip().split("\n")

print("🐳 Docker Image Analyzer\n")

images = get_docker_images()

for image in images:
    repo, tag, size = image.split()
    size_mb = float(size.replace("MB", "").replace("GB", "")) * (1024 if "GB" in size else 1)

    print(f"Image: {repo}:{tag} | Size: {size}")

    if size_mb > SIZE_LIMIT_MB:
        print("⚠️  Warning: Image size too large\n")
