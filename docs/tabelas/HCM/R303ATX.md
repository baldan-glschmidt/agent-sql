# R303ATX

## Descrição

e-Sfinge - Módulo Genérico/Arquivo Texto

---

## Resumo

- Campos: 8
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| AnoBas | Number(004,0) | Não | Ano |
| BimAno | Number(001,0) | Não | Código Bimestre Ano |
| TipTex | Number(002,0) | Não | Tipo do texto jurídico |
| NumTex | String(016) | Não | Número do texto jurídico |
| NomArq | String(100) | Não | Nome do arquivo onde está gravado o texto jurídico |
| NatTex | Number(002,0) | Não | Natureza do arquivo texto |
| OriReg | String(001) | Sim | Origem do Registro (G-Gerado, D-Digitado, I-Importado) |

---

## Chave Primária

- NumEmp
- AnoBas
- BimAno
- TipTex
- NumTex
- NomArq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
