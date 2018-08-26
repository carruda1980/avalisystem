# avalisystem

API em Rest para avaliação de produtos baseados em notas de 1 a 10 e retirando a média geral de acordo com os
votos de cada usuário.

## Usuário

Usuário previamente cadastrado no sistema poderá avaliar um produto.
Deve-se gerar um token para este usuário poder fazer as operações necessárias.

Separar os usuários comuns dos admins de acordo com as permissões.

## Produto

Uma entidade para identificar algo a ser avaliado. Pode ser apenas um campo texto genérico com slug.

### Permissões

Após fazer o CRUD completo, na primeira fase, podemos fazer com que somente os usuários admins da aplicação
possam deletar, alterar e até mesmo criar um produto.

## Voto

Dado um produto o usuário poderá avaliá-lo especificando uma pontuação 1 a 10 e também se for do
seu interesse escrever um ponto positivo e negativo sobre o produto.

## Computando os votos

Para termos a média geral podemos somar a pontuação dos votos e dividi-los pela quantidade. Seria uma média geral.

## Tecnologias

- Django + DRF

- Autenticação via Token

- Postgres/Mysql/Sqlite

- Testes unitários. Modelos, Serializers, metodos, Chamadas rest.

- Insomnia Rest Client


