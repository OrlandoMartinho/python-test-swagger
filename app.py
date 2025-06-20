from flask import Flask, request
from flask_restx import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy
from config import Config
from pydantic import BaseModel, ValidationError

app = Flask(__name__)
app.config.from_object(Config)

api = Api(app, title='API Livros', version='1.0')
db = SQLAlchemy(app)

# Modelo ORM (tabela livros)
class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    publicado_em = db.Column(db.String(10), nullable=False)

# Validação com Pydantic
class LivroSchema(BaseModel):
    titulo: str
    autor: str
    publicado_em: str

# Swagger model
livro_model = api.model('Livro', {
    'id': fields.Integer(readonly=True),
    'titulo': fields.String(required=True),
    'autor': fields.String(required=True),
    'publicado_em': fields.String(required=True),
})

@api.route('/livros')
class LivrosResource(Resource):
    @api.marshal_list_with(livro_model)
    def get(self):
        livros = Livro.query.all()
        return livros

    @api.expect(livro_model)
    def post(self):
        try:
            data = request.json
            livro_validado = LivroSchema(**data)
            livro = Livro(**livro_validado.dict())
            db.session.add(livro)
            db.session.commit()
            return {'mensagem': 'Livro criado com sucesso'}, 201
        except ValidationError as e:
            return {'erro': e.errors()}, 400

@api.route('/livros/<int:id>')
class LivroResource(Resource):
    def delete(self, id):
        livro = Livro.query.get_or_404(id)
        db.session.delete(livro)
        db.session.commit()
        return {'mensagem': 'Livro excluído com sucesso'}

    @api.expect(livro_model)
    def put(self, id):
        livro = Livro.query.get_or_404(id)
        data = request.json
        try:
            validado = LivroSchema(**data)
            for campo, valor in validado.dict().items():
                setattr(livro, campo, valor)
            db.session.commit()
            return {'mensagem': 'Livro atualizado'}
        except ValidationError as e:
            return {'erro': e.errors()}, 400

# Rodar o servidor
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
