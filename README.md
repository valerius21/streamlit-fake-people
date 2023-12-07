# Streamlit Demo

This demo shows how to use Streamlit to create a simple web app to process
some [fake people](https://github.com/fthuin/fakepeople).

## Docker

Build the docker image with the following command:

```bash
docker build . -t stdemo
```

Run the docker image with the following command:

```bash
docker run --rm -p 8501:8501 stdemo
```

## Development

Remember to keep the `requirements.txt` file up to date!

## Theming

https://blog.streamlit.io/introducing-theming/
