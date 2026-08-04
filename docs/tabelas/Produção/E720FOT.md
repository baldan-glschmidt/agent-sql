# E720FOT

## Descrição

Ficha - Roteiro - Fotos (Imagem) Detalhes Técnicos

---

## Resumo

- Campos: 7
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| FotDet | String(014) | Não | Código da Foto do detalhe (Imagem) |
| SeqFot | Number(004,0) | Não | Sequência numérica p/ mais de uma Foto (Imagem) |
| DesFot | String(240) | Não | Descrição  - informativos e/ou detalhes técnicos |
| DatVal | Date | Sim | Data de validade até |
| ImgFot | Image | Sim | Imagem da Foto |
| EndFot | String(255) | Sim | Endereço (caminho) da Foto (para busca automática) quando a foto não é gravada no Banco de Dados |

---

## Chave Primária

- CodEmp
- FotDet
- SeqFot

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
