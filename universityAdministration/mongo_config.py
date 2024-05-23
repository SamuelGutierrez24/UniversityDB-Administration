from mongoengine import connect

connect(
    db='db',
    username='<project>',
    password='<project>',
    host='mongodb+srv://<project>:<project>@datos.ltwggtv.mongodb.net/?retryWrites=true&w=majority&appName=Datos',
    alias='default'
)
