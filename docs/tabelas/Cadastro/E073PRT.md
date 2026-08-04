# E073PRT

## Descrição

Cadastros - Transportadoras - Veículos - Proprietário

---

## Resumo

- Campos: 8
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdePrt | Number(009,0) | Não | Código do proprietário |
| NomPrt | String(100) | Não | Nome do proprietário |
| CgcCpf | Number(014,0) | Sim | Número do CNPJ ou CPF |
| DocIde | String(014) | Sim | Número do CNPJ ou CPF |
| NrnTrc | String(014) | Sim | Registro nacional de transportadores rodoviários de carga - RNTRC |
| InsEst | String(025) | Sim | Inscrição estadual do proprietário |
| SigUfs | String(002) | Sim | Sigla do estado do proprietário |
| TipPrt | Number(001,0) | Sim | Tipo proprietário |

---

## Chave Primária

- IdePrt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
