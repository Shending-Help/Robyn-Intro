from robyn import Robyn, static_file

app = Robyn(__file__)

@app.get("/")
async def h(request):
    return static_file("./index.html")

app.start(port=5000)