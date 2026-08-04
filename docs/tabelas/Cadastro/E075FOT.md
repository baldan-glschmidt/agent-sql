# E075FOT

## Descrição

Cadastros - Produtos - Fotos

---

## Resumo

- Campos: 9
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| FotPro | String(014) | Não | Código da foto do produto |
| FotDer | String(007) | Não | Código da Derivação da Foto |
| SeqFot | Number(004,0) | Não | Sequência numérica p/ mais de uma Foto do produto |
| DesFot | String(240) | Não | Descrição da foto do produto - informativos e/ou detalhes técnicos |
| DatVal | Date | Sim | Data de Validade da Foto p/ o Produto |
| ImgFot | Image | Sim | Imagem da Foto |
| EndFot | String(255) | Sim | Endereço (caminho) da Foto (para busca automática) quando a foto não é gravada no Banco de Dados |
| VerFot | Number(008,0) | Sim | Versão da Foto p/ o Produto |

---

## Chave Primária

- CodEmp
- FotPro
- FotDer
- SeqFot

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
