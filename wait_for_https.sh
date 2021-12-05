echo -n "Waiting for HTTPS/5000 on app "
i=0

while ! curl --output /dev/null --silent --head --fail --insecure https://localhost:5000 && [ $i -lt $1 ]; do
    # wait 1 sec, print a peiod (no newline) to measure progress
    sleep 1
    echo -n "."
    i=$((i + 1))
done

# print if failed or success
if [ $i -eq $1 ]; then
    echo "FAILED!"
    exit 1
else
    echo "OK!"
fi
